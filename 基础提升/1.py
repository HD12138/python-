import requests

def requeseTest():
    try:
        url = "https://www.baidu.com"
        r = requests.get(url)
        print(r.headers)
        print(r.status_code)
        print(r.encoding)
        print(r.text)
        print(r.cookies)

        print("success")
    except Exception as e:
        print("Request failed:", e)

requeseTest()