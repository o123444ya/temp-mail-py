import requests, json, os, time, cloudscraper
#Made By HuanXiang
#Https://fb.com/o123444ya
class mail:
	def __init__(self):
		self.Request=cloudscraper.create_scraper()
	def CheckExpired(self):
		req_=self.Request.get('https://10minutemail.com/session/secondsLeft')
		if json.loads(req_.text)['secondsLeft']==0:
			return True
		else:
			return False
	def GetMail(self):
		req_=self.Request.get('https://10minutemail.com/session/address')
		self.Request.cookies=req_.cookies
		return json.loads(req_.text)['address']
	def GetMessage(self):
		if not self.CheckExpired():
			req_=self.Request.get('https://10minutemail.com/messages/messagesAfter/0')
			if req_.status_code!=200:return"Error"
			elif req_.text=='[]':return"N"
			else:
				reqjs=json.loads(req_.text[1:][:-1])
				txt='收信結果'
				txt+=f"\n發送者:{reqjs['sender']}"
				txt+=f"\n時間:{reqjs['sentDate']}"
				txt+=f"\n主旨:{reqjs['subject']}"
				txt+=f"\n內容:{reqjs['bodyPreview']}"
				return txt
print('歡迎使用幻想信箱py\n請勿作為商業用途')
mail=mail()
print('取得信箱中...')
print(mail.GetMail())
print('取得成功\n正在檢測收信...')
while True:
	try:
		get=mail.GetMessage()
		if get =='expired':print('過時\n請重新取得');break
		if get =='error':print('非200狀態錯誤\n請查看是否被封鎖IP\n如無法請聯繫幻想\nhttps://fb.com/o123444ya');break
		if get =='N':pass
		else:print(get);break
		time.sleep(5)#anti ban
	except KeyboardInterrupt:print('Ctrl-C');os._exit(1)
	except Exception as e:print(str(e))
