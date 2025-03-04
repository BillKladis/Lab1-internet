import requests  # εισαγωγή της βιβλιοθήκης

def more(text):
    count = 0
    for line in text.split('\n'):
        print(line)
        count += 1
        if count % 30 == 0:
            reply = input('Show more (y/n)? ')
            if reply == 'n':
                break

url = input("give url:\t")
 
if not url.startswith("https://"):
    url= "https://" + url
print(url)

with requests.get(url) as response:

    print(f"Server{response.headers.get('Server')}")
    print(f"Cookies:{'Set-Cookies' in response.headers}")
    for cookies in response.cookies:
        print(f"Name: {cookies.name}")
        print(f"Expiration:{cookies.expires}\n")