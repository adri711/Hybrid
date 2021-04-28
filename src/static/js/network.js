import {socket} from "./app.js";
import { selected_user } from "./chat.js";
import { add_message, show_notification, update_last_message } from "./utils.js";

socket.on('direct_message', function(data) {
    console.log(data);
	if(selected_user == data.from) {
        add_message(data.text, true);
    }
    update_last_message(data.text, data.from, true);
    show_notification("You received a new message", `<b>${data.sender_username}:</b> ${data.text}`, 5);
    var audio = new Audio('/static/sounds/notif.mp3');
    audio.play();
});