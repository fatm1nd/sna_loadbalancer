import requests
import threading
import datetime
import time

url = "URL_OF_SERVICE"

def requestTinyGPT():
    data = {"text":"Write+long+essay+about+WWII"}
    print("Start downloading")
    startTime = datetime.datetime.now()
    r = requests.post(url,data)
    endTime = datetime.datetime.now()
    print("End downloading:",endTime - startTime,"s")

sessionN = 0

requestTinyGPT()


while True:
    print("session #",sessionN)
    threads = [threading.Thread(target=requestTinyGPT) for i in range(200)]

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    time.sleep(5)
    session += 1