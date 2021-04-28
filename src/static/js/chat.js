import { clear_chat_box, set_chat_box_title, add_message, update_last_message} from "./utils.js";
import {socket} from "./app.js";

export var selected_user = null;

// When a contact gets clicked
$(document).on('click', '.contact', function() {
    if($(this).attr("name") != selected_user) {
        let contact_elem = $(this);
        let selected_user_name = $(this).attr("name");
        selected_user = $(this).data("userid");
        set_chat_box_title(selected_user_name);
        clear_chat_box();
        $.post(`/directmessages/${$(this).data("userid")}`, function(messages) {
            messages.forEach(message => {
                add_message(message.message, $(contact_elem).data("userid") == message.sender_id);
            });
        });
    }
});

// Message send
$(document).keyup(function (e) {
    if(e.keyCode == 13 && $('#message_input:focus')) { // 13 is the enter key
        let message = $('#message_input').val();
        if(selected_user && message) {
            socket.emit('direct_message', {'target': selected_user, 'message': message});
            add_message(message, false);
        }
        // Clear chat input
        $('#message_input').val("");
        update_last_message(message, selected_user,false);
    }
});