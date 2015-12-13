$(document).ready(function () {
	$.post('/editor/data', {actionType: 'list'}, function (data, status) {
		console.log(data);
		var html = "";
		$.each(data.detail, function (index, item) {
			html += "<li><a href='/editor/edit?scriptName=" + item + "' target='_blank'>" + item + "</a></li>"
		});
		$('#scriptContainer').append(html);
	});
});



// END
