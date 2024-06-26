const express = require("express");
const { createClient } = require("redis");
import { promisify } from "util";
const cli = createClient();
cli.on("error", (err) => {
  console.log("Redis encounter error: ", err);
});
const app = express();

const listProducts = [
  { id: 1, name: "Suitcase 250", price: 50, stock: 4 },
  { id: 2, name: "Suitcase 450", price: 100, stock: 10 },
  { id: 3, name: "Suitcase 650", price: 350, stock: 2 },
  { id: 3, name: "Suitcase 1050", price: 550, stock: 5 },
];

function getItemById(getID) {
  return listProducts.find(({ id }) => id === getID);
}
/* Get list of all products */
app.get("/list_products", (_req, res) => {
  res.send(
    listProducts.map((product) => ({
      itemId: product.id,
      itemName: product.name,
      price: product.price,
      initialAvailableQuantity: product.stock,
    }))
  );
});

function reserveStockById(itemId, stock) {
  cli.set(`item.${itemId}`, stock);
}
async function getCurrentReservedStockById(itemId) {
  const getAsync = promisify(cli.get).bind(cli);
  const value = await getAsync(`item.${itemId}`);
  return value;
}

app.get("/list_products/:itemId", async (req, res) => {
  const { itemId } = req.params;
  const product = getItemById(Number(itemId));
  if (product === undefined) {
    res.statusCode = 404;
    res.send({ status: "Product not found" });
  } else {
    const reserveStock = await getCurrentReservedStockById(product.id);
    res.send({
      itemId: product.id,
      itemName: product.name,
      price: product.price,
      initialAvailableQuantity: product.stock,
      currentQuantity:
        reserveStock === null ? product.stock : Number(reserveStock),
    });
  }
});

app.get("/reserve_product/:itemId", async (req, res) => {
  const { itemId } = req.params;
  const product = getItemById(Number(itemId));
  if (product === undefined) {
    res.statusCode = 404;
    res.send({ status: "Product not found" });
    return;
  }
  let reserveStock = await getCurrentReservedStockById(product.id);
  reserveStock = reserveStock === null ? product.stock : Number(reserveStock);
  if (!reserveStock) {
    res.send({ status: "Not enough stock available", ItemId: product.id });
  } else {
    reserveStockById(product.id, reserveStock - 1);
    res.send({ status: "Reservation confirmed", ItemId: product.id });
  }
});

app.listen(1245, "127.0.0.1", () => {
  console.log(`Server is live at 127.0.0.1:1245`);
});