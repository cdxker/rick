import threading
import requests
from afk import catchInMatch
import time

def checkSheets():
    global updateInMatch
    x = 0
    while x < 1000000:
        value = requests.get()

        if values and int(values[0][0]) == 1:
            print("yes")
            updateInMatch = 1
            catchInMatch(updateInMatch)

        else:
            updateInMatch = 0
            catchInMatch(updateInMatch)
            print("nawl")

        x+=1
        time.sleep(3)

scriptThread = threading.Thread(target=catchInMatch)
sheetThread = threading.Thread(target=checkSheets)

scriptThread.start()
sheetThread.start()

scriptThread.join()
sheetThread.join()
