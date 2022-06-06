import { createClient, print } from 'redis';

const client = createClient();

client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));
client.on('connect', () => console.log(`Redis client connected to the server`));

client.subscribe("holberton school channel");

client.on('message', (chn, mess) => {
  console.log(mess);
  if (mess === "KILL_SERVER") {
    client.unsubscribe(chn);
    process.exit(0);
  }
});
