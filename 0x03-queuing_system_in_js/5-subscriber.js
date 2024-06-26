import { createClient, print as pt } from "redis";

const cli = createClient();
cli.on("connect", () => console.log("Redis client connected to the server"));
cli.on("error", (err) =>
  console.log("Redis client not connected to the server: " + err)
);

cli.subscribe("holberton school channel");
cli.on("message", (_channel, message) => {
  if (message === "KILL_SERVER") {
    cli.unsubscribe("holberton school channel");
    cli.quit(() => {});
  }
  console.log(message);
});
