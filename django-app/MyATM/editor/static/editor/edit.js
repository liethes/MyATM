// 重要变量
var name = getQueryString('scriptName');
var editor = ace.edit("theEditor");



// 初始化ACE EDITOR
editor.setTheme("ace/theme/twilight");
editor.session.setMode("ace/mode/tradeblazer");

editor.setOptions({
	enableBasicAutocompletion: true,
	enableSnippets: true,
	enableLiveAutocompletion: false
});

editor.setPrintMarginColumn(240);
editor.setShowPrintMargin(false);

editor.commands.addCommand({
	name: 'myCommand',
	bindKey: {win: 'Ctrl-1', mac: 'Ctrl-1'},
	exec: function (editor) {
		alert('fuck');
	},
	readOnly: true // false if this command should not apply in readOnly mode
});

editor.focus();



// JQUERY部分
$(document).ready(function () {
	// 页面初始化: 获取code
	$.post('/editor/data', {actionType: 'get', scriptName: name}, function (data, status) {
		console.log(data);
		editor.setValue(data.detail);
		editor.navigateTo(0, 0);
	});



	// 按钮: SAVE
	$('#btnSave').click(function () {
		var scriptName = name;
		var scriptContent = editor.getValue();

		$.post('/editor/data', {actionType: 'save', scriptName: scriptName, scriptContent: scriptContent}, function (data, status) {
		});
	});

	// 按钮: SYNC
	$('#btnSync').click(function () {
		var scriptName = name;
		var scriptContent = editor.getValue();

		var bgnTime = new Date();
		$.post('/editor/data', {actionType: 'sync', scriptName: scriptName, scriptContent: scriptContent}, function (data, status) {
			var endTime = new Date();
			var duration = Math.round((endTime - bgnTime) / 100) / 10;
			alert('DONE in ' + duration + ' seconds');
		});
	});
});



// END
