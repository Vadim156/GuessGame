import random
import json
import requests
from NumberAlgo import NumberAlgo


playGame = NumberAlgo()
playGame.setNumber()

while True:
    
    payload = int(playGame.currentNumber)
    json_dump = json.dumps(payload)

    r = requests.post('http://127.0.0.1:7777/',data=json_dump)

    respone = json.loads(r.text)
    result = playGame.NumberAlgo(respone)
    
    if result == playGame.winMessage or result == playGame.LoseMessage:
        break
    


        