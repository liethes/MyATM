# 转换文件编码集
# 唐峰 2015-12-07

# 函数: 处理一个文件
def convertOneFile(fileName_in):
	inputFile = open(fileName_in, 'r', encoding='GBK')
	content = inputFile.read()
	inputFile.close()

	fileNameMain = fileName_in.split('.')[0]
	fileNameExt = fileName_in.split('.')[1]
	fileInfo1 = ''
	fileInfo2 = ''

	lineArray = content.split('\n')
	for line in lineArray:
		if line[:7] == '// 简称: ':
			fileInfo1 = line[7:]
		if line[:7] == '// 名称: ':
			fileInfo2 = line[7:]
	fileInfo2 = fileInfo2.replace('/', '-')
	print('SUCKS: ' + fileInfo1 + '/' + fileInfo2)

	# newFileName = 'new_' + fileNameMain + '_' + fileInfo1 + '_' + fileInfo2 + '.' + fileNameExt
	newFileName = 'new_' + fileNameMain + '.' + fileNameExt
	outputFile = open(newFileName, 'w', encoding='UTF8')
	outputFile.write(content)
	outputFile.close()

	print('====DONE ' + fileName_in + '====')



# 函数: 处理一个类别（共function和strategy两类）
def processOneCat(catName, fileCount):
	for i in range(fileCount):
		fileNum = ('000' + str(i + 1))[-3:]
		fileName = catName + '/' + catName + '_' + fileNum + '.tbs'
		convertOneFile(fileName)



# 主程序
processOneCat('function', 122)
processOneCat('strategy', 139)



# END
