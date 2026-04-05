import requests 
import json

URL  = "https://official-joke-api.appspot.com/random_joke"
req_counter  = 0 

def do_Request() : 
    res = requests.get(url=URL)
    data = res.json()
    return data

def writeToFile(): 
    with open("jokes.txt", "a") as file:
        data = do_Request()
        file.write(str(data))
        file.write("\n\n")

while req_counter<15:
    writeToFile()

    req_counter+=1

    


    