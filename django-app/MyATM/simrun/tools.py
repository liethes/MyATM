from bs4 import BeautifulSoup



# 【类】报告抓取器 - TB
class ReportExtractorTb:
	# 【方法】 读取文件内容
	@staticmethod
	def getFileContent():
		filePath = '/Users/TANG/Downloads/测试报告/性能测试报告_IF888_M1.files/交易记录.htm'
		dataFile = open(filePath, 'r', encoding='GBK')
		content = dataFile.read()
		dataFile.close()
		return content



	# 【方法】 RUN
	@staticmethod
	def run():
		rslt = []
		soup = BeautifulSoup(ReportExtractorTb.getFileContent(), 'html.parser')

		lineNum = 0
		for line in soup.find_all(name='tr'):
			# 不要前三行
			lineNum += 1
			if lineNum <= 3:
				continue

			# 处理内容行
			tdList = []
			for td in line.find_all(name='td'):
				tdList.append(td.string)
			rslt.append([tdList[0], tdList[2], tdList[4], tdList[5], tdList[6], tdList[7], tdList[8]])

		return rslt



# END
