import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient();
const asyn = promisify(client.get).bind(client);

client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));
client.on('connect', () => console.log(`Redis client connected to the server`));

function setNewSchool(schoolName, value) {
	client.set(schoolName, value, (err, res) => {
		print(`Reply: ${res}`)
	});
}

async function displaySchoolValue(schoolName) {
	const res = await asyn(schoolName);
	console.log(res);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
