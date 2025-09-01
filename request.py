import requests

proxies = {
    "http": "http://localhost:3128",
    "https": "http://localhost:3128",
}

r = requests.get("https://httpbin.org/ip", proxies=proxies)
print(r.text)
