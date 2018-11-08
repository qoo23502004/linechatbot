import requests
def say():
    url = "https://www.google.com.tw"
    content = requests.get(url)
    
    return content
    


if __name__ == "__main__":
    a=say()

