import { createClient, print as pt } from "redis";

const cli = createClient();
cli.on("connect", () => console.log("Redis client connected to the server"));
cli.on("error", (err) =>
  console.log("Redis client not connected to the server: " + err)
);

function setNewSchool(schoolName, value) {
  cli.set(schoolName, value, pt);
}

function displaySchoolValue(schoolName) {
  cli.get(schoolName, (_e, val) => console.log(val));
}
displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");
