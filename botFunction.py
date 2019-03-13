import requests
import re
import json
import random
from bs4 import BeautifulSoup

def checkState():
    url = "https://decapi.me/twitch/uptime?channel=vv0z1"
    content = requests.get(url).text
    
    return content


def googleSearch(keyword):
	a=""
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
		
		#for i in items:
    			# 標題
			#print("標題：" + i.text)
    			# 網址
			#print("網址：" + i.get('href'))
		z=items[0].get('href')
		x=len(z)
		for i in range(7,x):
			a=a+z[i]
		final=items[0].text+" "+a
		print(final)
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
	cityDict={"!嘉義縣":0,"!新北市":1,"!嘉義市":2,"!新竹縣":3,"!新竹市":4,"!台北市":5,"!台南市":6,"!宜蘭縣":7,"!苗栗縣":8,"!雲林縣":9,"!花蓮縣":10,"!台中市":11,"!台東縣":12,"!桃園市":13,"!南投縣":14,"!高雄市":15,"!金門縣":16,"!屏東縣":17,"!基隆市":18,"!澎湖縣":19,"!彰化縣":20,"!連江縣":21}
	cityNum=cityDict[Num]
	CT=weatherData['records']['location'][cityNum]['locationName']
	AMst=weatherData['records']['location'][cityNum]['weatherElement'][0]['time'][-3]['startTime']
	AMstate="天氣狀況："+weatherData['records']['location'][cityNum]['weatherElement'][0]['time'][0]['parameter']['parameterName']
	AMrain="降雨機率："+weatherData['records']['location'][cityNum]['weatherElement'][1]['time'][0]['parameter']['parameterName']+"%"
	AMMT="最高溫度："+weatherData['records']['location'][cityNum]['weatherElement'][4]['time'][0]['parameter']['parameterName']
	AMmT="最低溫度："+weatherData['records']['location'][cityNum]['weatherElement'][2]['time'][0]['parameter']['parameterName']
	AMfeel="體感："+weatherData['records']['location'][cityNum]['weatherElement'][3]['time'][0]['parameter']['parameterName']
	
	total=CT+"\n"+AMstate+"\n"+AMrain+"\n"+AMmT+"\n"+AMMT+"\n"+AMfeel+"\n"+"更新時間："+AMst	
	return total

def food(text):
	breakfirst=['起司蛋餅','火腿蛋餅','鮪魚蛋土司','小籠包','御飯糰','火腿蛋土司','豆漿+油條','燒餅,鰻頭','培根蛋土司','薯餅','雞塊','雞腿堡','今天當神仙，別吃了啦','燻雞蛋餅','貝果']
	lunch=['鍋燒意麵','雞腿便當','雞排便當','排骨飯','涼麵','炒麵','麥當勞','肯德基','鐵板麵','咖哩飯','義大利麵','燉飯','今天當神仙，別吃了啦']
	dinner=['牛肉丼飯','豬排丼飯','親子丼','滷味','林東芳牛肉麵','滷肉飯','排骨飯','雞腿便當','水餃','煎餃','鍋貼','蝦仁蛋炒飯','米粉羹','土魠魚羹','鍋燒意麵','握壽司','錢櫃牛肉麵','麻辣鍋']
	aftermoontea=['鬆餅','烤土司','乳酪蛋糕','檸檬派','義大利麵','烤雞腿','炸雞塊','脆薯','洋蔥圈','起司塔']
	latenightmeal=['鹹酥雞','香雞排','林東芳牛肉麵','鼎王','老四川','滷味','烤雞腿','麥當勞歡樂送','魷魚羹','米粉','潤餅','當歸鴨','蚵仔煎','炒花枝','肉羹','米糕','甜不辣']
	if text=="!早餐":
		count=len(breakfirst)
		feedback=breakfirst[random.randint(0,len(breakfirst)-1)]
		return feedback
	elif text=="!午餐":
		count=len(lunch)
		feedback=lunch[random.randint(0,len(lunch)-1)]
		return feedback
	elif text=="!下午茶":
		count=len(aftermoontea)
		feedback=aftermoontea[random.randint(0,len(aftermoontea)-1)]
		return feedback
	elif text=="!晚餐":
		count=len(dinner)
		feedback=dinner[random.randint(0,len(dinner)-1)]
		return feedback
	elif text=="!消夜" or text=="!宵夜":
		count=len(latenightmeal)
		feedback=latenightmeal[random.randint(0,len(latenightmeal)-1)]
		return feedback
	



if __name__ == "__main__":
    print(food("!午餐"))
    

