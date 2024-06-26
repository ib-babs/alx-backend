import { createClient, print as pt } from "redis";

const cli = createClient();
cli.on("connect", () => console.log("Redis client connected to the server"));
cli.on("error", (err) =>
  console.log("Redis client not connected to the server: " + err)
);

function setHash(field, value) {
  cli.hset("HolbertonSchools", field, value, pt);
}
function getAllHash(schoolNames) {
  cli.hgetall(schoolNames, (_, val) => console.log(val));
}

setHash("Portland", 50);
setHash("Seattle", 80);
setHash("New York", 20);
setHash("Bogota", 20);
setHash("Cali", 40);
setHash("Paris", 2);

getAllHash("HolbertonSchools");
