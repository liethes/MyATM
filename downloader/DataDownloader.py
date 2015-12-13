from io import BytesIO
import pycurl
import json
import time



def fetchOnePage(pageNum):
	url = 'http://trader.7hcn.com/module/trader/ajax.shtml?action=fetch_org_data&role=4039&page=' + str(pageNum) + '&callback=xxx'

	buffer = BytesIO()

	c = pycurl.Curl()
	c.setopt(c.URL, url)
	c.setopt(c.WRITEDATA, buffer)
	c.perform()
	c.close()

	body = buffer.getvalue()
	content = body.decode('utf8')
	bgnLen = 4
	endLen = len(content) - 2
	contentData = content[bgnLen:endLen]
	# print(contentData)

	jsonData = json.loads(contentData)
	# print(jsonData['data'])

	for oneDay in jsonData['data']:
		print(oneDay['dateline'] + ',' + oneDay['today_in'] + ',' + oneDay['today_out'])

	print('========')
	time.sleep(1)



for i in range(1, 40):
	fetchOnePage(i)



# END
