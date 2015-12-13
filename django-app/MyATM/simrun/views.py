from django.shortcuts import render
from django.http import HttpResponse
from .tools import ReportExtractorTb
from .models import *



# 测试【报告抓取器】
def test(request):
	infoList = ReportExtractorTb.run()
	print(infoList.__len__())
	for info in infoList:

		print(info)
	return HttpResponse('fuck')



# END
