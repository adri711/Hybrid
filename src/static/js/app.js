// Page switcher
const page_container = $("#container");
load_page("home");
selected_page = null;


function set_page_title(new_title) {
	new_title = new_title[0].toUpperCase() + new_title.substring(1);
	document.title = "Hybrid | " + new_title;
	$('.topnav p').html(new_title);
}

function load_page(page_name) {
	selected_page = page_name;
	selected_page = $(this).attr('name');
	set_page_title(page_name);
	$.post("app/" + page_name, function(data) {
		page_container.html(data);
	});
}

$(document).ready(function() {
	$('.sidenav a').click(function(e) {
		if($(this).attr('name') != selected_page) {
			load_page($(this).attr("name"));
			$(".active").removeClass("active");
			$(this).addClass("active");
		};
	});
});