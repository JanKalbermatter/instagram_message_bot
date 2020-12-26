const fs = require("fs");
const { IgApiClient } = require("instagram-private-api");
const config = require("./config.json");

console.log("users.json auslesen");
let rawData = fs.readFileSync("users.json");
let users = JSON.parse(rawData);
console.log(users);

const ig = new IgApiClient();
ig.state.generateDevice(config.InstaUser);

(async () => {
    await ig.simulate.preLoginFlow();
    const loggedInUser = await ig.account.login(config.InstaUser, config.InstaPassword);
    console.log("Logged int")
    process.nextTick(async () => await ig.simulate.postLoginFlow());

    
    
    users.forEach(async (user) => {
        const userID = await ig.user.getIdByUsername(user);
        console.log("userID: ", userID);

        const thread = ig.entity.directThread([userID.toString()]);
        await thread.broadcastText(config.Message);
    });
})();