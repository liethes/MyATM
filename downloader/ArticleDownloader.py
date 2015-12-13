from io import BytesIO
import pycurl
from bs4 import BeautifulSoup
import time



# 工具函数:根据URL获取HTML内容
def getHtmlString(url):
	buffer = BytesIO()
	c = pycurl.Curl()
	c.setopt(c.URL, url)
	c.setopt(c.WRITEDATA, buffer)
	c.perform()
	c.close()

	body = buffer.getvalue()
	content = body.decode('utf8')
	return content



# 函数: 处理一名交易者的一页
def processOnePage(url):
	print('----' + url + '----')

	rslt = ''

	html = getHtmlString(url)
	html = html.replace('<div class="box-show-new"></P>', '<div class="box-show-new">')
	html = html.replace('<div class="box-show-new"></p>', '<div class="box-show-new">')
	html = html.replace('<div class="box-show-new"></DIV>', '<div class="box-show-new">')
	html = html.replace('<div class="box-show-new"></div>', '<div class="box-show-new">')
	soup = BeautifulSoup(html, 'html.parser')

	text = soup.find(name='div', attrs={'class': 'box-show-new'})
	# text = text.div
	# lines = text.find_all('div')
	rslt = text.get_text()

	# lines = soup.find_all(name='div', attrs={'style': 'text-indent: 2em; '})
	# for line in lines:
	# 	rslt += line.get_text() + '\n'

	# text = soup.find(name='div', attrs={'class': 'bd-2 box-list mt10'})
	# # print(text.prettify())
	# # print(text.get_text())
	# text = text.find(name='table')
	# rslt = text.get_text()

	print(rslt[0:50].replace('\n', ''))

	time.sleep(1)

	return rslt



# 函数: 处理一名交易者
def processOneTrader(url, traderName):
	print('fuck ' + traderName)

	html = getHtmlString(url)
	soup = BeautifulSoup(html, 'html.parser')

	pager = soup.find(name='div', attrs={'id': 'pager'})
	pager = pager.find(name='em')
	pageCount = pager.get_text().split(':')[1]

	baseUrl = url.split('1.html')[0]

	traderId = url.replace('/', '').split('article')[1].split('-1.html')[0]
	traderId = ('000000' + traderId)[-6:]
	thisTrader = open('TRADER_' + traderId + '_' + traderName + '.md', 'a')
	for i in range(int(pageCount)):
		subUrl = baseUrl + str(i + 1) + '.html'
		text = processOnePage(subUrl)
		thisTrader.write(text)
	thisTrader.close()



################################################################
url_list = []

content = getHtmlString('http://www.7hcn.com/article/97143-1.html')
soup = BeautifulSoup(content, "html.parser")

output = open('traderList.txt', 'w')

for link in soup.find_all(name='a', attrs={'class': 'ib-a'}):
	if link.get('href') == '/www.7hcn.com/article/88145-1.html':
		continue
	data = link.get('href') + ',' + link.string
	output.write(data + '\n')
	url_list.append(data)

output.close()



# 去重&排序
new_url_list = list(set(url_list))
new_url_list.sort()



# 输出
i = 0
for data in new_url_list:
	i += 1
	if i > 300:
		break
	try:
		processOneTrader(data.split(',')[0], data.split(',')[1])
	except:
		print('!!!发生错误!!!')
################################################################



# 临时DEBUG测试
# processOneTrader('http://www.7hcn.com/article/79083-1.html', 'TEST')
# processOnePage('http://www.7hcn.com/article/79083-1.html')



# END
