import { createClient } from "redis";
import { promisify } from "util";
import { createQueue } from "kue";
import express from "express";

const cli = createClient(),
  queue = createQueue(),
  app = express();
cli.on("error", (err) => {
  console.log("Redis encounter error: ", err);
});

const reserveSeat = (number) => {
  cli.set("available_seat", number);
};
async function getCurrentAvailableSeats() {
  const getSeat = promisify(cli.get).bind(cli);
  const seat = await getSeat("available_seat");
  return seat;
}
let reservationEnabled = true;
app.get("/available_seat", async (_req, res) => {
  let seat = await getCurrentAvailableSeats();
  res.send({ numberOfAvailableSeats: seat });
});

app.get("/reserve_seat", (_req, res) => {
  if (!reservationEnabled) res.send({ status: "Reservation are blocked" });
  const job = queue.create("reserve_seat").save(function (err) {
    if (!err) res.send({ status: "Reservation in process" });
    else res.send({ status: "Reservation failed" });
  });
  job.on("complete", () =>
    console.log(`Seat reservation job ${job.id} completed`)
  );
  job.on("failed", (err) =>
    console.log(`Seat reservation job ${job.id} failed: ${err}`)
  );
});

//Processing reserve_seat
app.get("/process", async (_req, res) => {
  queue.process("reserve_seat", async (job, done) => {
    // reserveSeat(50);
    const seat = await getCurrentAvailableSeats();
    cli.decr("available_seat");
    console.log(job);
    if (seat === 0) reservationEnabled = false;
    else if (seat >= 1) done();
    else done(new Error("Not enough seats available"));
  });
  res.send({ status: "Queue processing" });
});

// Listen
app.listen(1245, "127.0.0.1", () => {
  console.log(`Server is live at 127.0.0.1:1245`);
});
