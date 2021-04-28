/* Utils file */
export const set_main_size = (new_size) => {
	$(".main").css("width", new_size + '%');
	$(".topnav").css("width", new_size + '%');
	$(".right_side").css("margin-left", new_size + '%');
}

export function set_page_title(new_title) {
	new_title = new_title[0].toUpperCase() + new_title.substring(1);
	document.title = "Hybrid | " + new_title;
	$('.topnav p').html(new_title);
}

export function clear_chat_box() {
    $("#chat_box").html(''); // Clears chat box container
}

export function set_chat_box_title(new_title) {
	$(".chat_box_top h3").html(new_title);
}

export function add_message(message, received) {
	let message_elem = document.createElement("div");
	let message_container = document.createElement("div");
	if (received) {
			message_elem.className = "received";
			message_container.className = "grey_msg";
			message_container.appendChild(document.createTextNode(message));
			message_elem.appendChild(message_container);
	}
	else {

			message_elem.className = "sent";
			message_container.className = "blue_msg";
			message_container.appendChild(document.createTextNode(message));
			message_elem.appendChild(message_container);
	}
	// Append the element to the chat box
	document.querySelector("#chat_box").appendChild(message_elem);
	$('.chat_box').scrollTop(10000);
}

export function update_last_message(new_message,user_id, received) {
	if(!received) {
		new_message = "You: " + new_message;
	}
	$(`#u${user_id} .last_message`).html(new_message);
}

export function show_notification(title, message, time) {
	$("#notification .title").html(title);
	$("#notification .text").html(message)
	$("#notification").css("display", "block");
	setTimeout(function() { 
		$("#notification").css("display", "none");
	}, time*1000);
}