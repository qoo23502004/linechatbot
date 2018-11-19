import requests
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



if __name__ == "__main__":
    print(googleSearch("test"))
    

