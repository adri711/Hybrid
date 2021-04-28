import {set_main_size, set_page_title} from "./utils.js";

// Page switcher
const page_container = $("#container");
const next_page = $(".app-text").data("nextpage");
load_page(next_page);
let selected_page = null;
export const socket = io.connect('http://' + document.domain + ':' + location.port);
socket.on('connect', function() {
	console.log("Connected to the network server.");
});

function load_page (page_name) {
	let selected_page = page_name;
	selected_page = $(this).attr('name');
	set_page_title(page_name);
	$.post("/app/" + page_name, function(data) {
		page_container.html(data);
		set_main_size($(".right_side").data("size"));
		window.history.pushState("", "", "/app/" + page_name);
		$(".active").removeClass("active");
		$(`#${page_name}`).addClass("active");
	});
}

$(document).ready(function() {
	$('.sidenav a').click(function(e) {
		if($(this).attr('name') != selected_page) {
			load_page($(this).attr("name"));
			//$(this).addClass("active");
		};
	});
});