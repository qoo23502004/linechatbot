import requests
import re
import json
from bs4 import BeautifulSoup

def checkState():
    url = "https://decapi.me/twitch/uptime?channel=vv0z1"
    content = requests.get(url).text
    
    return content


def googleSearch(keyword):
	
    # Google 搜尋 URL
	google_url = 'https://www.google.com.tw/search'

	# 查詢參數
	my_params = {'q': keyword}

	# 下載 Google 搜尋結果
	r = requests.get(google_url, params = my_params)

	# 確認是否下載成功
	if r.status_code == requests.codes.ok:
  	# 以 BeautifulSoup 解析 HTML 原始碼
		soup = BeautifulSoup(r.text, 'html.parser')

  		# 觀察 HTML 原始碼
  		# print(soup.prettify())

  		# 以 CSS 的選擇器來抓取 Google 的搜尋結果
		items = soup.select('div.g > h3.r > a[href^="/url"]')
		
		for i in items:
    			# 標題
			#print("標題：" + i.text)
    			# 網址
			#print("網址：" + i.get('href'))
			final=i.text+" "+i.get('href')
			return final

def musicSearch(keyword):
	
	url = "https://www.youtube.com/results?search_query=" + keyword
	res = requests.get(url, verify=False)
	soup = BeautifulSoup(res.text,'html.parser')
	last = None

	for entry in soup.select('a'):
		m = re.search("v=(.*)",entry['href'])
		if m:
			target = m.group(1)
			if target == last:
				continue
			if re.search("list",target):
				continue
			youtubecode = str(target)
			return youtubecode


def weatherSearch(Num):
	r=requests.get('https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWB-F6A47420-AC70-4467-96CB-B94C0E1BDA11&format=JSON')
	weatherData=json.loads(r.text)
	#cityDict={"!嘉義縣":0,"!新北市":1,"!嘉義市":2,"!新竹縣":3,"!新竹市":4,"!台北市":5,"!台南市":6,"!宜蘭縣":7,"!苗栗縣":8,"!雲林縣":9,"!花蓮縣":10,"!台中市":11,"!台東縣":12,"!桃園市":13,"!南投縣":14,"!高雄市":15,"!金門縣":16,"!屏東縣":17,"!基隆市":18,"!澎湖縣":19,"!彰化縣":20,"!連江縣":21}
	cityNum=cityDict[Num]
	CT=weatherData['records']['location'][cityNum]['locationName']
	AMst=weatherData['records']['location'][cityNum]['weatherElement'][0]['time'][0]['startTime']
	AMstate=weatherData['records']['location'][cityNum]['weatherElement'][0]['time'][0]['parameter']['parameterName']
	AMrain="降雨機率"+weatherData['records']['location'][cityNum]['weatherElement'][1]['time'][0]['parameter']['parameterName']+"%"
	AMMT="最高溫度"+weatherData['records']['location'][cityNum]['weatherElement'][4]['time'][0]['parameter']['parameterName']
	AMmT="最低溫度"+weatherData['records']['location'][cityNum]['weatherElement'][2]['time'][0]['parameter']['parameterName']
	AMfeel="體感:"+weatherData['records']['location'][cityNum]['weatherElement'][3]['time'][0]['parameter']['parameterName']

	PMst=weatherData['records']['location'][cityNum]['weatherElement'][0]['time'][1]['startTime']
	PMstate=weatherData['records']['location'][cityNum]['weatherElement'][0]['time'][1]['parameter']['parameterName']
	PMrain="降雨機率"+weatherData['records']['location'][cityNum]['weatherElement'][1]['time'][1]['parameter']['parameterName']+"%"
	PMMT="最高溫度"+weatherData['records']['location'][cityNum]['weatherElement'][4]['time'][1]['parameter']['parameterName']
	PMmT="最低溫度"+weatherData['records']['location'][cityNum]['weatherElement'][2]['time'][1]['parameter']['parameterName']
	PMfeel="體感:"+weatherData['records']['location'][cityNum]['weatherElement'][3]['time'][1]['parameter']['parameterName']
	total=CT+"\n"+AMst+"\n"+AMstate+"\n"+AMrain+"\n"+AMMT+"\n"+AMmT+"\n"+AMfeel+"\n\n"+PMst+"\n"+PMstate+"\n"+PMrain+"\n"+PMMT+"\n"+PMmT+"\n"+PMfeel
	return total

if __name__ == "__main__":
    print(musicSearch("despocito"))
    

