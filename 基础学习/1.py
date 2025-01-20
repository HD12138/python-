import requests
from utils import urlManager

def requestTest():
    try:
        url = "https://www.baidu.com"
        r = requests.get(url)
        r.encoding = "UTF-8"
        
        # 打印响应信息
        print("Headers:", r.headers)
        print("Status Code:", r.status_code)
        print("Response Text:", r.text[:200] + "...")  # 只打印前200个字符
        print("Cookies:", r.cookies, "\n")
        
        # 不要尝试解析非JSON响应
        # print(r.json())  # 删除这行，因为百度返回的是HTML而不是JSON
        
        print("Request successful")
    except Exception as e:
        print("Request failed:", e)

requestTest()