# 将TradeBlazer函数列表导入Atom的Sinppet定义文件
# 唐峰 2015-12-07

# 读入
file = open('tbFunctionList.txt', 'r')
content = file.read()
file.close()

# 写出
output = open('output/result-snippet.txt', 'w')

output.write("'.source.tbs':\n")

lineArray = content.split('\n')
for oneLine in lineArray:
	if oneLine.__len__() > 0:
		if oneLine[0] == '#':
			print('')
		else:
			fieldArray = oneLine.split('\t')
			nameField = fieldArray[0]
			if fieldArray.__len__() > 1:
				descField = fieldArray[1]
			else:
				descField = '关键字'
			print(nameField + ':' + descField)
			rslt = ""
			rslt += "\t'" + descField + "':\n"
			rslt += "\t\t'prefix': '" + nameField + "'\n"
			rslt += "\t\t'body': '" + nameField + "'\n"
			output.write(rslt + '\n')

output.close()



# END
