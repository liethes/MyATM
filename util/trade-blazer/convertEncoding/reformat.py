# 格式化代码
# 唐峰 2015-12-07

import jsbeautifier



# 函数: 格式化一个文件
def formatOneFile(fileName):
	# 输入
	inFile = open(fileName, 'r')
	inString = inFile.read()
	inFile.close()

	# 预处理
	inString = inString.replace('If', 'if')
	inString = inString.replace('Else', 'else')
	inString = inString.replace('For', 'for')
	inString = inString.replace('To', 'to')
	inString = inString.replace('DownTo', 'downto')
	inString = inString.replace('While', 'while')
	inString = inString.replace('Break', 'break')
	inString = inString.replace('Continue', 'continue')
	inString = inString.replace('True', 'true')
	inString = inString.replace('False', 'false')

	inString = inString.replace('Params', 'PARAMS')
	inString = inString.replace('Vars', 'VARS')
	inString = inString.replace('Begin', 'BEGIN')
	inString = inString.replace('End', 'END')

	inString = inString.replace('Return', 'RETURN')

	# 输出
	outFile = open('formatted_' + fileName, 'w')

	option = jsbeautifier.BeautifierOptions()
	option.indent_with_tabs = True
	option.brace_style = 'end-expand'
	option.preserve_newlines = True
	option.max_preserve_newlines = 3
	# option.end_with_newline = True
	outString = jsbeautifier.beautify(inString, option)  # ★★★

	outLineArray = outString.split('\n')
	for outLine in outLineArray:
		if (not outLine.upper() == 'PARAMS') and (not outLine.upper() == 'VARS') and (not outLine.upper() == 'BEGIN') and (not outLine.upper() == 'END') and (not outLine[:2] == '//') and (not outLine[:2] == ''):
			outLine = '\t' + outLine
		outFile.write(outLine + '\n')

	outFile.close()



# 函数: 处理一个类别
def processOneCat(catName, fileCount):
	for i in range(fileCount):
		fileNum = ('000' + str(i + 1))[-3:]
		fileName = 'new_' + catName + '/' + catName + '_' + fileNum + '.tbs'
		formatOneFile(fileName)



# 主程序
processOneCat('function', 122)
processOneCat('strategy', 139)



# END
