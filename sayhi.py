import requests
def say():
    url = "https://decapi.me/twitch/uptime?channel=vv0z1"
    content = requests.get(url).text
    
    return content
    


if __name__ == "__main__":
    a=say()
    print(a)

