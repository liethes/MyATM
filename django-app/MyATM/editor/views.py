from django.shortcuts import render
from django.http import HttpResponse
import httplib2, json
from urllib import parse
from .models import Script
from .myutil import Logger



# 列表
def list(request):
	return render(request, 'list.html')



# 编辑
def edit(request):
	scriptName = request.GET['scriptName']
	return render(request, 'edit.html', {'scriptName': scriptName})



# 数据
def data(request):
	cfg_baseUrl = 'http://172.16.51.100:8000/script/'
	result = {}

	# 获取参数
	actionType = request.POST['actionType']

	scriptName = ''
	if request.POST.__contains__('scriptName'):
		scriptName = request.POST['scriptName']

	scriptContent = ''
	if request.POST.__contains__('scriptContent'):
		scriptContent = parse.quote(request.POST['scriptContent'])

	Logger.info('actionType: ' + actionType)
	Logger.info('scriptName: ' + scriptName)
	Logger.info('scriptContent: ' + scriptContent)

	# 分支: 获取脚本List
	if actionType == 'list':
		scriptList = Script.objects.all()
		resultList = []
		for script in scriptList:
			resultList.append(script.name)
		result = {
			'result': 'OK',
			'detail': resultList
		}

	# 分支: 获取脚本内容
	if actionType == 'get':
		scriptList = Script.objects.filter(name=scriptName)
		result = {
			'result': 'OK',
			'detail': scriptList[0].code
		}

	# 分支: 保存脚本
	if actionType == 'save':
		# 更新框架DB
		theScript = Script.objects.filter(name=scriptName)[0]
		theScript.code = parse.unquote(scriptContent)
		theScript.save()

		# 设置返回值
		result = {
			'result': 'OK',
			'detail': ''
		}

	# 分支: 同步脚本
	if actionType == 'sync':
		# 更新RUN ENGINE
		h2 = httplib2.Http()
		resp, content = h2.request(cfg_baseUrl + 'update' + '?scriptName=' + scriptName + '&scriptContent=' + scriptContent)
		print(content)

		# 设置返回值
		result = {
			'result': 'OK',
			'detail': ''
		}

	# 返回数据
	return HttpResponse(json.dumps(result), content_type='application/json')



# END
