# -*- coding: utf-8 -*-
from Linephu.linepy import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse,timeit,atexit
from gtts import gTTS
from time import strftime
from googletrans import Translator
botStart = time.time()
cl = LINE("EwhyLGDEbKBAdHhytDn8.6XdruQn4v6LzyyLRNbWDwa.EVpJuF8hdZxqCBSyfDq7icoKw6yZijCLb8yB3ZhdtIA=")
cl.log("Auth Token : " + str(cl.authToken))
oepoll = OEPoll(cl)
readOpen = codecs.open("read.json","r","utf-8")
read = json.load(readOpen)
settingsOpen = codecs.open("temp.json","r","utf-8")
settings = json.load(settingsOpen)
myProfile = {
    "displayName": "",
    "statusMessage": "",
    "pictureStatus": ""
}
lineSettings = cl.getSettings()
clProfile = cl.getProfile()
clMID = cl.profile.mid
myProfile["displayName"] = clProfile.displayName
myProfile["statusMessage"] = clProfile.statusMessage
myProfile["pictureStatus"] = clProfile.pictureStatus
Bots=[clMID]
Owner=["ufe1707ae9b2ff7ab61505795b7995440",clMID]
admin=["ufe1707ae9b2ff7ab61505795b7995440",clMID]
mulai = time.time()

msg_dict = {}
bl = [""]

def cTime_to_datetime(unixtime):
    return datetime.datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def restartBot():
    print ("[ 訊息 ] 機器重啟")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True     
    except Exception as error:
        logError(error)
        return False    
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
def logError(text):
    cl.log("[ 錯誤 ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def sendMention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@zeroxyuuki "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mid")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        cl.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
def helpmessage():
    helpmessage: """指令表
查看指令表
↪ 「Help」查看全部指令
↪ 「self」查看設定"""
    return helpmessage
def lineBot(op):
    try:
        if op.type == 26 or op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 13:
                if settings["contact"] == True:
                    msg.contentType = 0
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.getProfileCoverURL(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                            cl.sendMessage(msg.to,"[顯示名稱]:\n" + msg.contentMetadata["顯示名稱"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[狀態消息]:\n" + contact.statusMessage + "\n[圖片網址]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[封面網址]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.getProfileCoverURL(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendMessage(msg.to,"[顯示名稱]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[狀態消息]:\n" + contact.statusMessage + "\n[圖片網址]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[封面網址]:\n" + str(cu))
            if msg.contentType == 0:
                if text is None:
                    return
            if sender in admin:
                if text.lower() == "logout":
                  cl.sendMessage(to, "已登出")
                  sys.exit("[ INFO ] BOT SHUTDOWN")
                  return
                if "miya" in msg.text.lower():
                    while 1:
                        cl.sendMessage(to, text=None, contentMetadata={'mid': "ufe1707ae9b2ff7ab61505795b7995440',"}, contentType=13)
                elif text.lower() == 'reread on':
                    settings["reread"] = True
                    cl.sendMessage(to, "收回開啟")
        if op.type == 65:
            if settings["reread"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                            if msg_dict[msg_id]["text"] == 'Gambarnya dibawah':
                                ginfo = cl.getGroup(at)
                                contact = cl.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 Gambar Dihapus 」\n• Pengirim : "
                                ret_ = "• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ry = str(contact.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':contact.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                cl.sendMessage(at, "收回訊息者 @wanping ", contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                cl.sendImage(at, msg_dict[msg_id]["data"])
                            else:
                                ginfo = cl.getGroup(at)
                                contact = cl.getContact(msg_dict[msg_id]["from"])
                                ret_ =  "「 收回訊息 」\n"
                                ret_ += "• 收回訊息者 : {}".format(str(contact.displayName))
                                ret_ += "\n• 群組名稱 : {}".format(str(ginfo.name))
                                ret_ += "\n• 收回時間 : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n• 訊息內容 : {}".format(str(msg_dict[msg_id]["text"]))
                                cl.sendMessage(at, str(ret_))
                                image = "https://stickershop.line-scdn.net/stickershop/v1/sticker/" + contact.pictureStatus								
                                cl.sendImageWithURL(op.param1,image)	
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
                if settings["autoRead"] == True:
                    cl.sendChatChecked(to, msg_id)
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                if msg.contentType == 0 and sender not in clMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if clMID in mention["M"]:
                                if settings["detectMention"] == False:
                                    contact = cl.getContact(sender)
                                    cl.sendMessage(to, "標我有事？(此為系統自動回覆)")
                                    sendMessageWithMention(to, contact.mid)
                                break
            try:
                msg = op.message
                if settings["reread"] == True:
                    if msg.contentType == 0:
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                lists.append(mention["M"])
                            list=""
                            x = msg.text
                            for mid in lists:
                                x=x.replace("@"+str(cl.getContact(mid).displayName),"@!")
                                list+=mid+","
                            listt=list[:-1]
                            msg_dict[msg.id] = {"mtext":"[收回訊息者]\n @! \n[訊息內容]\n"+x,"from":msg._from,"createdTime":time.time(),"mentionee":listt}
                        else:
                            msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":time.time()}
            except Exception as e:
                print(e)
            if msg.contentType == 1:
                if settings["reread"] == True:
                    if 'gif' in msg.contentMetadata.keys()!= None:
                        gif = cl.downloadObjectMsg(msg_id, saveAs="reread/{}-image.gif".format(time.time()))
                        msg_dict[msg.id] = {"from":msg._from,"gif":gif,"createdTime":time.time()}
                    else:
                        image = cl.downloadObjectMsg(msg_id, saveAs="reread/{}-image.bin".format(time.time()))
                        msg_dict[msg.id] = {"from":msg._from,"image":image,"createdTime":time.time()}
            if msg.contentType == 3:
                if settings["reread"] == True:
                    sound = cl.downloadObjectMsg(msg_id, saveAs="reread/{}-sound.mp3".format(time.time()))
                    msg_dict[msg.id] = {"from":msg._from,"sound":sound,"createdTime":time.time()}
            if msg.contentType == 7:
                if settings["reread"] == True:
                    stk_id = msg.contentMetadata['STKID']
                    msg_dict[msg.id] = {"from":msg._from,"stkid": stk_id ,"createdTime":time.time()}
            if msg.contentType == 13:
                if settings["reread"] == True:
                    mid = msg.contentMetadata["mid"]
                    msg_dict[msg.id] = {"from":msg._from,"mid": mid ,"createdTime":time.time()}
            if msg.contentType == 14:
                if settings["reread"] == True:
                    file = cl.downloadObjectMsg(msg_id, saveAs="reread/{}-".format(time.time())+msg.contentMetadata['FILE_NAME'])
                    msg_dict[msg.id] = {"from":msg._from,"file":file,"createdTime":time.time()}
        if op.type == 65:
            try:
                msg = op.message
                at = op.param1
                msg_id = op.param2
                if settings["reread"] == True:
                    if msg_id in msg_dict:
                        timeNow = time.time()
                        opi=[]
                        opi.append(msg_dict[msg_id]["from"])
                        if "mtext" in msg_dict[msg_id]:
                            x =msg_dict[msg_id]["mentionee"].split(',')
                            for ic in x:
                                opi.append(ic)
#                            cl.sendMessage(at,msg_dict[msg_id]["mentionee"]+"||"+str(msg_dict[msg_id]["mtext"]))
                            sendMention(at,msg_dict[msg_id]["mtext"],opi)
                            cl.sendMessage(at,"收回時間"+str(timeNow - msg_dict[msg_id]["createdTime"])+"秒之前")
                            del msg_dict[msg_id]
                        if "text" in msg_dict[msg_id]:
                            sendMention(at,"[收回訊息者]\n @! \n[訊息內容]\n"+str(msg_dict[msg_id]["text"]),opi)
                            cl.sendMessage(at,"收回時間"+str(timeNow - msg_dict[msg_id]["createdTime"])+"秒之前")
                            del msg_dict[msg_id]
                        if "image" in msg_dict[msg_id]:
                            sendMention(at,"[收回訊息者]\n @! \n[訊息內容]\n一張圖片",opi)
                            cl.sendImage(at, msg_dict[msg_id]["image"])
                            cl.deleteFile(msg_dict[msg_id]["image"])
                            cl.sendMessage(at,"收回時間"+str(timeNow - msg_dict[msg_id]["createdTime"])+"秒之前")
                        if "gif" in msg_dict[msg_id]:
                            sendMention(at,"[收回訊息者]\n @! \n[訊息內容]\n一張圖片",opi)
                            cl.sendGIF(at, msg_dict[msg_id]["gif"])
                            cl.deleteFile(msg_dict[msg_id]["gif"])
                            cl.sendMessage(at,"收回時間"+str(timeNow - msg_dict[msg_id]["createdTime"])+"秒之前")
                        if "sound" in msg_dict[msg_id]:
                            sendMention(at,"[收回訊息者]\n @! \n[訊息內容]\n一份音檔",opi)
                            cl.sendAudio(at, msg_dict[msg_id]["sound"])
                            cl.deleteFile(msg_dict[msg_id]["sound"])
                            cl.sendMessage(at,"收回時間"+str(timeNow - msg_dict[msg_id]["createdTime"])+"秒之前")
                            del msg_dict[msg_id]
                        if "file" in msg_dict[msg_id]:
                            sendMention(at,"[收回訊息者]\n @! \n[訊息內容]\n一個檔案",opi)
                            cl.sendFile(at, msg_dict[msg_id]["file"])
                            cl.deleteFile(msg_dict[msg_id]["file"])
                            cl.sendMessage(at,"收回時間"+str(timeNow - msg_dict[msg_id]["createdTime"])+"秒之前")
                            del msg_dict[msg_id]
                        if "stkid" in msg_dict[msg_id]:
                            path = "https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/ANDROID/sticker.png;compress=true".format(msg_dict[msg_id]["stkid"])
                            sendMention(at,"[收回訊息者]\n @! \n[訊息內容]\n一張貼圖",opi)
                            cl.sendImageWithURL(at,path)
                            cl.sendMessage(at,"收回時間"+str(timeNow - msg_dict[msg_id]["createdTime"])+"秒之前")
                            del msg_dict[msg_id]
                        if "mid" in msg_dict[msg_id]:
                            sendMention(at,"[收回訊息者]\n @! \n[訊息內容]\n一則友資",opi)
                            cl.sendContact(at,msg_dict[msg_id]["mid"])
                            cl.sendMessage(at,"收回時間"+str(timeNow - msg_dict[msg_id]["createdTime"])+"秒之前")
                            del msg_dict[msg_id]
                else:
                    pass
            except Exception as e:
                print (e)
        if op.type == 55:
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass
    except Exception as error:
        logError(error)
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)
		







































































