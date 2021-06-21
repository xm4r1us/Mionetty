import os
from discord.ext import commands
import discord
from replit import db
import json
import requests
import random
from flask import request
import functools
orangeid = 677214856109359118
from keepalive import keep_alive

import time









#///////////////////////////////

def isValidTCID(value):
    value = str(value)
    
    # 11 hanelidir.
    if not len(value) == 11:
        return False
    
    # Sadece rakamlardan olusur.
    if not value.isdigit():
        return False
    
    # Ilk hanesi 0 olamaz.
    if int(value[0]) == 0:
        return False
    
    digits = [int(d) for d in str(value)]
    
    # 1. 2. 3. 4. 5. 6. 7. 8. 9. ve 10. hanelerin toplamından elde edilen sonucun
    # 10'a bölümünden kalan, yani Mod10'u bize 11. haneyi verir.
    if not sum(digits[:10]) % 10 == digits[10]:
        return False
    
    # 1. 3. 5. 7. ve 9. hanelerin toplamının 7 katından, 2. 4. 6. ve 8. hanelerin toplamı çıkartıldığında,
    # elde edilen sonucun 10'a bölümünden kalan, yani Mod10'u bize 10. haneyi verir.
    if not (((7 * sum(digits[:9][-1::-2])) - sum(digits[:9][-2::-2])) % 10) == digits[9]:
        return False
    
    # Butun kontrollerden gecti.
    return True

kod = random.randint(0, 20)
kod1 = random.randint(0, 20)
kod2 = random.randint(0, 20)
kod3 = random.randint(0, 20)
kod4 = random.randint(0, 20)
kod5 = random.randint(0, 20)
kod6 = random.randint(0, 20)
kod7 = random.randint(0, 20)
kod8 = random.randint(0, 20)
viprol = 798814648447139853
vipkanal = 843079485074309160
message = ""
bot = commands.Bot(command_prefix="+", intents=discord.Intents.all())
bot.author_id = 798799401555460126 and 751531315689553920  # Change to your discord id!!!


def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)


@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier


token = os.environ.get("DISCORD_BOT_SECRET")


def getvalue(kullanici_id=None):
    try:
        value = db[f"{kullanici_id}"]
        if value or value != None:
            return value
        else:
            return None
    except KeyError:
        return None

@bot.event

async def on_member_remove(member):
  del db[f"{member.id}"]
  channel = bot.get_channel(802195211844976731)
  await channel.send(f"<@{member.id}> Left The Server and I deleted him/her wallet :anger:")
@bot.event
async def on_message(message):
    if message.content ==  'Sa' :
        await message.channel.send('Aleyküm Selam :anger:')
  
    if message.content.startswith( '+dailycoin' ):
      if  str(message.channel.id) != "841351290452836394":
        await message.delete()
        return
    
    if message.content.startswith( 'kontrol' ):
      if  str(message.author.id) == "798824139783143426":
        deneme216 = message.content.split(" eksilt ")
        kontrolling = getvalue(deneme216[1])
        await message.channel.send(kontrolling)
    if message.content.startswith( 'miocoin' ):
      if  str(message.author.id) == "798824139783143426":
        deneme216 = message.content.split(" eksilt ")
        await message.channel.send("Deleting.."+deneme216[1])
        userid = int(deneme216[1])
        value = db[f"{userid}"]
        puanint = int(value)
        paraint = puanint - 100
        parastr = str(paraint)
        db[f"{userid}"] = parastr
        await message.channel.send("Coin deleted")
        
        value2 = db[f"677214856109359118"]
        puanint2 = int(value2)
        paraint2 = puanint2 + 100
        parastr2 = str(paraint2)
        db[f"677214856109359118"] = parastr2
        await message.channel.send("Coin deleted")
    if message.content.startswith( '+balance' ):
      if  str(message.channel.id) != "841351290452836394":
        await message.delete()
        return
    if message.content.startswith( '+bal' ):
      if  str(message.channel.id) != "841351290452836394":
        await message.delete()
        return
    await bot.process_commands(message)
    koko = random.randint(0,10)
    koko2 = random.randint(0,10)
    if koko == koko2:
      if str(message.channel.id) == "852481487123120138":
        userid = message.author.id
        value = db[f"{userid}"]
        puanint = int(value)
        paraint = puanint + koko
        parastr = str(paraint)
        db[f"{userid}"] = parastr
def createaccount(id):
    db[id] = 0
@bot.command()
async def CheckTC(ctx, tcno):
  koko = isValidTCID(tcno)
  await ctx.reply(str(koko))

def check():
    return os.system("python main2.py combolist.txt 100 ")
#/////////////// MAIL ////////////////////
@bot.command()
async def checkmail(ctx,ekstrakomut=""):
  attachments = ctx.message.attachments
  for attachment in attachments:
    await attachment.save("combolist.txt")
  with open('combolist.txt') as my_file:
    Koko = sum(1 for _ in my_file)
    if Koko > 10000:
      await ctx.reply("Only 10000 lines")
      return
  money = getvalue(f"{ctx.author.id}")
  if  int(money) >= 80:
    userid = ctx.author.id
    value = db[f"{userid}"]
    puanint = int(value)
    paraint = puanint - 80
    parastr = str(paraint)
    db[f"{userid}"] = parastr
    money2 = getvalue(f"{ctx.author.id}")
    await ctx.reply("Your new coin ---> "+ money2)
  else:
    await ctx.reply("This checker using cost is 100 Miocoin")
    return


  print("Starting...")
  await ctx.reply("Starting...")
  await bot.loop.run_in_executor(None, functools.partial(check))
  await ctx.reply("Checking Finished")
  try:
    if ekstrakomut == "-pazarekle":
      await ctx.reply(file=discord.File(r'hits.txt'))
      os.rename(r'hits.txt',"markets/"+str(ctx.author.id)+"mail.txt")
    if ekstrakomut == "-paylas":
      channel = bot.get_channel(842845869720338482)
      await channel.send("Paylaşım <@"+str(ctx.author.id)+"> tarafından yapıldı...")
      await channel.send(file=discord.File(r'hits.txt'))
      await ctx.reply(file=discord.File(r'hits.txt'))
      os.remove("hits.txt")
    else:
      await ctx.reply(file=discord.File(r'hits.txt'))
      os.remove("hits.txt")
    

    
  except Exception as e:
    print(e)
    await ctx.reply("No Hits ;(")
def checkk():
    return os.system("python exxen.py combolist1.txt 100 ")
#////////////////// EXXEN ////////////////////////
@bot.command()
async def checkexxen(ctx, ekstrakomut=""):
  attachments = ctx.message.attachments
  for attachment in attachments:
    await attachment.save("combolist1.txt")
  with open('combolist1.txt') as my_file:
    Koko = sum(1 for _ in my_file)
    if Koko > 10000:
      await ctx.reply("Only 10000 lines")
      return
  money = getvalue(f"{ctx.author.id}")
  if  int(money) >= 100:
    userid = ctx.author.id
    value = db[f"{userid}"]
    puanint = int(value)
    paraint = puanint - 100
    parastr = str(paraint)
    db[f"{userid}"] = parastr
    money2 = getvalue(f"{ctx.author.id}")
    await ctx.reply("Your new coin ---> "+ money2)
  else:
    await ctx.reply("This checker using cost is 100 Miocoin")
    return


  print("Starting...")
  await ctx.reply("Starting...")
  await bot.loop.run_in_executor(None, functools.partial(checkk))
  await ctx.reply("Checking Finished")
  
  try:
    if ekstrakomut == "-pazarekle":
      await ctx.reply(file=discord.File(r'hitss.txt'))
      os.rename(r'hitss.txt',"markets/"+str(ctx.author.id)+"exxen.txt")
    elif ekstrakomut == "-paylas":
      channel = bot.get_channel(842845869720338482)
      await channel.send("Paylaşım <@"+str(ctx.author.id)+"> tarafından yapıldı...")
      await channel.send(file=discord.File(r'hitss.txt'))
      await ctx.reply(file=discord.File(r'hitss.txt'))
      os.remove("hitss.txt")
    else:
      await ctx.reply(file=discord.File(r'hitss.txt'))
      os.remove("hitss.txt")

    os.remove("combolist1.txt")

    
  except Exception as e:
    print(e)
    await ctx.reply("No Hits ;(")


def checksmart():
    return os.system("python dsmartgo.py combolist1.txt 100 ")
#////////////////// dsmart ////////////////////////
@bot.command()
async def checkdsmart(ctx, ekstrakomut=""):
  attachments = ctx.message.attachments
  for attachment in attachments:
    await attachment.save("combolist1.txt")
  with open('combolist1.txt') as my_file:
    Koko = sum(1 for _ in my_file)
    if Koko > 10000:
      await ctx.reply("Only 10000 lines")
      return
  money = getvalue(f"{ctx.author.id}")
  if  int(money) >= 100:
    userid = ctx.author.id
    value = db[f"{userid}"]
    puanint = int(value)
    paraint = puanint - 100
    parastr = str(paraint)
    db[f"{userid}"] = parastr
    money2 = getvalue(f"{ctx.author.id}")
    await ctx.reply("Your new coin ---> "+ money2)
  else:
    await ctx.reply("This checker using cost is 100 Miocoin")
    return


  print("Starting...")
  await ctx.reply("Starting...")
  await bot.loop.run_in_executor(None, functools.partial(checksmart))
  await ctx.reply("Checking Finished")
  
  try:
    if ekstrakomut == "-pazarekle":
      await ctx.reply(file=discord.File(r'HitDsmart.txt'))
      os.rename(r'HitDsmart.txt',"markets/"+str(ctx.author.id)+"dsmart.txt")
    elif ekstrakomut == "-paylas":
      channel = bot.get_channel(842845869720338482)
      await channel.send("Paylaşım <@"+str(ctx.author.id)+"> tarafından yapıldı...")
      await channel.send(file=discord.File(r'HitDsmart.txt'))
      await ctx.reply(file=discord.File(r'HitDsmart.txt'))
      os.remove("HitDsmart.txt")
    else:
      await ctx.reply(file=discord.File(r'HitDsmart.txt'))
      os.remove("HitDsmart.txt")

    os.remove("combolist1.txt")

    
  except Exception as e:
    print(e)
    await ctx.reply("No Hits ;(")























#///////////////////////TONGUÇ////////////
def checkks():
    return os.system("python lna.py combolisttonguc.txt 100 ")
@bot.command()
async def checktonguc(ctx,ekstrakomut=""):
  attachments = ctx.message.attachments
  for attachment in attachments:
    await attachment.save("combolisttonguc.txt")
  with open('combolisttonguc.txt') as my_file:
    Koko = sum(1 for _ in my_file)
    if Koko > 10000:
      await ctx.reply("Only 10000 lines")
      return
  money = getvalue(f"{ctx.author.id}")
  if  int(money) >= 50:
    userid = ctx.author.id
    value = db[f"{userid}"]
    puanint = int(value)
    paraint = puanint - 50
    parastr = str(paraint)
    db[f"{userid}"] = parastr
    money2 = getvalue(f"{ctx.author.id}")
    await ctx.reply("Your new coin ---> "+ money2)
    userid = ctx.author.id
    value = db[f"712605555470106664"]
    puanint = int(value)
    paraint = puanint + 50
    parastr = str(paraint)
    db[f"712605555470106664"] = parastr
  else:
    await ctx.reply("This checker using cost is 50 Miocoin")
    return


  print("Starting...")
  await ctx.reply("Starting...")
  await bot.loop.run_in_executor(None, functools.partial(checkks))
  await ctx.reply("Checking Finished")
  try:
    if ekstrakomut == "-pazarekle":
      await ctx.reply(file=discord.File(r'hitst.txt'))
      os.rename(r'hitst.txt',"markets/"+str(ctx.author.id)+"tonguc.txt")
    elif ekstrakomut == "-paylas":
      channel = bot.get_channel(842845869720338482)
      await channel.send("Paylaşım <@"+str(ctx.author.id)+"> tarafından yapıldı...")
      await channel.send(file=discord.File(r'hitst.txt'))
      await ctx.reply(file=discord.File(r'hitst.txt'))
      os.remove("hitst.txt")
    else:
      await ctx.reply(file=discord.File(r'hitst.txt'))
      os.remove("hitst.txt")

    

    
  except Exception as e:
    print(e)
    await ctx.reply("No Hits ;(")
@bot.command()
async def allshop(ctx):
  
  dirs  = os.listdir("markets/")
  for file in dirs:
    if "exxen" in file:
      datas = file.split("exxen")
      user = bot.get_user(int(datas[0]))
      await ctx.reply(user.name+ " Selling Exxen Accounts.")
    if "mail" in file:
      datas = file.split("mail")
      user = bot.get_user(int(datas[0]))
      await ctx.reply(user.name+ " Selling Mail Accounts.")
    if "tonguc" in file:
      datas = file.split("tonguc")
      user = bot.get_user(int(datas[0]))
      await ctx.reply(user.name + " Selling Tonguc Accounts.")

   
@bot.command()
async def balance(ctx):
    money = getvalue(f"{ctx.author.id}")
    if money != None:
        await ctx.reply("Your MioCoin Balance ----> " + str(money)+ " <a:miocoin:852831494279397376>")
    else:
        createaccount(f"{ctx.author.id}")
        await ctx.reply("Hesabınız Açıldı birdaha deneyin")
@bot.command()
async def bal(ctx):
    money = getvalue(f"{ctx.author.id}")
    if money != None:
        await ctx.reply("Your MioCoin Balance ----> " + str(money)+ " <a:miocoin:852831494279397376>")
    else:
        createaccount(f"{ctx.author.id}")
        await ctx.reply("Hesabınız Açıldı birdaha deneyin")
@bot.command()
async def trademiotoalpha(ctx, AlphaPoints, KEY):
  Alphacoin1 = int(AlphaPoints)
  AlphaCoin = Alphacoin1 * 2
  userid2 = ctx.author.id
  value2 = db[f"{userid2}"]
  if  int(value2) >= int(AlphaCoin):
    print("sa")
  else:
    await ctx.reply("Missing Miocoin Balance.")
    return
  try:
        userid = ctx.author.id
        value = db[f"{userid}"]
        puanint = int(value)
        paraint = puanint - AlphaCoin
        parastr = str(paraint)
        db[f"{userid}"] = parastr
        await ctx.reply("Your Miocoin Reduced Successfully.")
        requests.get("https://api.alphacracking.com/miocointoalphakeyapi1H4AKLF629A6CW7.php?eklenecek_puan=" + AlphaPoints+"&alphakey="+ KEY)
        await ctx.reply("Your AlphaCoin balance updated Succesfully.")
  except:
        await ctx.reply("Trade can't completed")

@bot.command()
@commands.cooldown(1, 86400, commands.BucketType.user)
async def dailycoin(ctx):
    rol = discord.utils.get(ctx.guild.roles,name="VIP")
    if rol in ctx.author.roles:
      try:
          
          userid = ctx.author.id
          value = db[f"{userid}"]
          puanint = int(value)
          paraint = puanint + 80
          parastr = str(paraint)
          db[f"{userid}"] = parastr
          await ctx.reply("Daily Coin Redeemed Successfully")
          return
      except:
          createaccount(ctx.author.id)
          userid = ctx.author.id
          value = db[f"{userid}"]
          puanint = int(value)
          paraint = puanint + 80
          parastr = str(paraint)
          db[f"{userid}"] = parastr
          await ctx.reply("Daily Coin Redeemed Successfully")
          return
    try:
        
        userid = ctx.author.id
        value = db[f"{userid}"]
        puanint = int(value)
        paraint = puanint + 40
        parastr = str(paraint)
        db[f"{userid}"] = parastr
        await ctx.reply("Daily Coin Redeemed Successfully")
    except:
        createaccount(ctx.author.id)
        userid = ctx.author.id
        value = db[f"{userid}"]
        puanint = int(value)
        paraint = puanint + 40
        parastr = str(paraint)
        db[f"{userid}"] = parastr
        await ctx.reply("Daily Coin Redeemed Successfully")



@dailycoin.error
async def dailycoin(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        err_desc = ":x: You Already Redeemed Your MioCoin. Wait `{:.2f}` Seconds.".format(
            error.retry_after)
        await ctx.reply(err_desc)
    else:
        raise error


@bot.command()
async def balancehim(ctx, member: discord.Member):
    arg1 = member.id
    if arg1 == None:
        await ctx.reply("Give ID")
    else:
        money = getvalue(f"{arg1}")
        if money != None:
            await ctx.reply("Him/Her MioCoin Balance ----> " + str(money)+ " <a:miocoin:852831494279397376>")
            return str(money)
        else:
            await ctx.reply("No Wallet :anger:")
            return


@bot.command()
async def market(ctx):
    em = discord.Embed(title="Market")
    mainshop = [{
        "name": "VIP",
        "price": str(1500) + " <a:miocoin:852831494279397376>",
        "description": "Extra Points, Cheap Checkers. :anger:",
        "command":"+buy VIP "
    },
    {
        "name": "SteamCode",
        "price": str(100) + " <a:miocoin:852831494279397376>",
        "description": "Generate A Steam Code. :anger:",
        "command":"+gen steamcode "

    },
        {
        "name": "Exxen",
        "price": str(100) + " <a:miocoin:852831494279397376>",
        "description": "If Anyone Selling Exxen Accounts You Can Buy With This Command",
        "command":"+shop exxen @User"

    
    },{
        "name": "Mail",
        "price": str(25) + " <a:miocoin:852831494279397376>",
        "description": "If Anyone Selling Mail Accounts You Can Buy With This Command",
        "command":"+shop mail @User"

    }

    
    ]
    for item in mainshop:
        name = item["name"]
        price = item["price"]
        desc = item["description"]
        command = item["command"]
        em.add_field(name=name, value=f" {price} \n  {desc}\n How Can I buy it: {command}")

    await ctx.reply(embed=em)


@bot.command()
async def buy(ctx, arg1):
    if str(arg1) == "VIP" or "vip":
        userid = ctx.author.id
        try:
            value = db[f"{userid}"]
        except:
            await ctx.reply("Did you open a wallet ??")
            return
        puanint = int(value)
        if puanint >= 1500:
            rol = discord.utils.get(ctx.guild.roles, id=798814648447139853)
            if not rol in ctx.author.roles:
                puanguncel = puanint - 1500
                db[f"{userid}"] = str(puanguncel)
                await bot.add_roles(ctx.author, name="VIP")
            else:
                await ctx.reply("You still give role")
        else:
            await ctx.reply("Pls make money :moneybag: (VIP is 1500 points)")
            return


@bot.command()
async def sendcoin(ctx, member : discord.Member, arg2):
    arg1 = member.id
    if str(arg1) == str(ctx.author.id):
        await ctx.reply("Are You Stupid ? ")
        return
    if int(arg2) <= 0:
        await ctx.reply("0 değerinin altında para mı gönderiliyor")
        return
    moneyg = getvalue(f"{ctx.author.id}")
    if int(arg2) >= int(moneyg):
        await ctx.reply("Are You Stupid ? ")
        return
    try:
        moneya = getvalue(f"{arg1}")
    except:
        await ctx.reply("Galiba Gönderdiğiniz Kişi hesap açmamış")
    if int(moneyg) > 0:
        paraint = int(moneyg)
        yenipara = paraint - int(arg2)
        db[str(ctx.author.id)] = str(yenipara)
        gyenipara = int(moneya) + int(arg2)
        db[str(arg1)] = str(gyenipara)
        await ctx.reply("Sent :smile: ")


@bot.command()
async def addmiocoin(ctx, arg1):
    with open("kodlar.txt", "r+") as rs:
        if str(arg1) in rs:
            await ctx.reply("Code Dedected..")
        else:
            await ctx.reply("You writed unwork code")
            return
    with open('kodlar.txt', 'w+') as f:
        veriler = f.read()
        veriler.replace(arg1, "")

    userid = ctx.author.id
    value = db[f"{userid}"]
    puanint = int(value)
    paraint = puanint + 10000
    parastr = str(paraint)
    db[f"{userid}"] = parastr
    print("Para Gönderildi ")
    await ctx.reply(
        f"Please Look Your wallet. Your old balance is {value} miocoin")


@bot.command()
async def deletewallet(ctx):
    del db[f"{ctx.author.id}"]
    await ctx.reply("Your Wallet Successfully Deleted")


@bot.command(pass_context=True)
async def alluser(ctx):
  allusers = db.prefix("")
  for i in allusers:
    value = db[i]
    print(i + " = " + str(value))
    with open("Veritabani.txt","a+") as yazim:
      yazim.write(i + " = " + str(value) + "\n")

  await ctx.reply(file=discord.File(r'Veritabani.txt'))
  with open("Veritabani.txt","w") as koko:
      koko.write("")
      






@bot.command()
async def deletehimwallet(ctx, arg1):
    rol = discord.utils.get(ctx.guild.roles, name="Admin | Yönetici")
    if rol in ctx.author.roles:
        del db[str(arg1)]
        await ctx.reply("Deleted Successfullly")
    else:
        await ctx.reply("You Are Not Admin")


@bot.command()
async def transfer(ctx, arg1, arg2, arg3):
    rol = discord.utils.get(ctx.guild.roles, name="Admin | Yönetici")
    if not rol in ctx.author.roles:
        await ctx.reply("You Are Not Admin")
        return
    moneyg = getvalue(f"{arg3}")
    moneya = getvalue(f"{arg1}")
    paraint = int(moneyg)
    yenipara = paraint - int(arg2)
    db[str(arg3)] = str(yenipara)
    gyenipara = int(moneya) + int(arg2)
    db[str(arg1)] = str(gyenipara)
    await ctx.reply("Gönderildi :D ")



#####################################################
@bot.command()
async def checkshop(ctx,tur,member : discord.Member):
  pazarsahibi = member.id
  try:
    okumak = open("markets/"+str(pazarsahibi)+tur+".txt").readlines()
    await ctx.reply("This User has " +str(len(okumak))+ " "+ tur+ " account")
  except:
    await ctx.reply("No Shop")
@bot.command()
async def shop(ctx,tur,member : discord.Member):
  try:
    pazarsahibi = member.id
    gonderilicekhesap = random_line("markets/"+str(pazarsahibi)+tur+".txt")
    with open("markets/"+str(pazarsahibi)+tur+".txt", "r") as f:
      lines = f.readlines()
    with open("markets/"+str(pazarsahibi)+tur+".txt", "w") as f:
      for line in lines:
          if line.strip("\n") != str(gonderilicekhesap):
              f.write(line)
    if str(tur) == "mail":
      ucret = 25
    if str(tur) == "exxen":
      ucret = 100
    if str(tur) == "tonguc":
      ucret = 75
      
    money = getvalue(f"{ctx.author.id}")
    if  int(money) >= int(ucret):
      userid = ctx.author.id
      value = db[f"{userid}"]
      puanint = int(value)
      paraint = puanint - int(ucret)
      parastr = str(paraint)
      db[f"{userid}"] = parastr
      money2 = getvalue(f"{ctx.author.id}")
      await ctx.reply("Your new coin ---> "+ money2)
      userid = ctx.author.id
      
      value = db[f"{pazarsahibi}"]
      puanint = int(value)
      paraint = puanint + int(ucret)
      parastr = str(paraint)
      db[f"{pazarsahibi}"] = parastr
    else:
      await ctx.reply("This checker using cost is 50 Miocoin")
      return
    guild = bot.get_guild(798814648447139850)

    anamember= guild.get_member(ctx.author.id)
    channel = await anamember.create_dm()
    await ctx.reply("Look Your PM")
    await channel.send(gonderilicekhesap)
  except:
    await ctx.reply("Error :/")
    os.remove("markets/"+str(pazarsahibi)+tur+".txt")
#####################################################

@bot.command()
@commands.cooldown(1, 20, commands.BucketType.user)
async def coinflip(ctx,miktar="0"):
  koko = getvalue(ctx.author.id)
  if int(miktar) > int(koko):
    return await ctx.reply("Are You Stupid")
  if miktar == None:
    return await ctx.reply("How Many MioCoin ? <a:miocoin:852831494279397376> ")
  message =   await ctx.reply("Flipping.. <a:coinflip:854350846557028412>")
  time.sleep(0)
  a = random.randint(1,2)
  b = random.randint(1,2)
  if a == b:
      await ctx.reply("Win :coin: \n A = "+str(a) + " B = " + str(b))
      userid = ctx.author.id
      value = db[f"{userid}"]
      puanint = int(value)
      paraint = puanint + int(miktar)
      parastr = str(paraint)
      db[f"{userid}"] = parastr
      money2 = getvalue(f"{ctx.author.id}")
      await ctx.reply("Your new coin ---> "+ money2)
  else:
      await ctx.reply("Sorry Sir. :sob: \n A = "+str(a) + " B = " + str(b))
      userid = ctx.author.id
      value = db[f"{userid}"]
      puanint = int(value)
      paraint = puanint - int(miktar)
      parastr = str(paraint)
      db[f"{userid}"] = parastr
      money2 = getvalue(f"{ctx.author.id}")
      await ctx.reply("Your new coin ---> "+ money2)



@coinflip.error
async def coinflip(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        err_desc = ":x: You Already Played Your CoinFlip . Wait `{:.2f}` Seconds.".format(
            error.retry_after)
        await ctx.reply(err_desc)
    else:
        raise error
#------------------------------------------------
@bot.command()
async def bank(ctx):
    em = discord.Embed(title="Market")
    mainshop = [{
        "name": "VIP",
        "price": str(1500) + " <a:miocoin:852831494279397376>",
        "description": "Extra Points, Cheap Checkers. :anger:",
        "command":"+buy VIP "
    }
    
    ]
    for item in mainshop:
        name = item["name"]
        price = item["price"]
        desc = item["description"]
        command = item["command"]
        em.add_field(name=name, value=f" {price} \n  {desc}\n How Can I get it: {command}")

    await ctx.reply(embed=em)
digerkod = random.randint(0, 100)
#----------------------------------------
from flask import Flask
from threading import Thread
import random

app = Flask('')


@app.route('/')
def home():
  
  try:
    
    userid = str(request.args.get('id'))
    value = getvalue(userid)
    return str(value)
  except Exception as e:
    print(e)
    return "Aktif"


keep_alive()
bot.run(token)
# Starts the bot
