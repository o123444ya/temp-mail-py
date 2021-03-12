import requests, json, os, time
#Made By HuanXiang
#Https://fb.com/o123444ya
class mail:
	def __init__(self):
		self.cookies=None
		self.address=None
	def getmail(self):
		req=requests.get('https://10minutemail.com/session/address')
		if req.status_code != 200:return 'error'
		else:
			try:
				address=json.loads(req.text)['address']
				self.cookies=req.cookies
				self.address=address
				return f'此次mail為{address}'
			except Exception as e:return str(e)
	def checkexpired(self):
		req=requests.get('https://10minutemail.com/session/expired',cookies=self.cookies)
		if json.loads(req.text)['expired']==True:
			return True
		else:return False
	def getmessage(self):
		if self.cookies != None:
			if self.address != None:
				try:
					if self.checkexpired() == False:
						req=requests.get('https://10minutemail.com/messages/messagesAfter/0',cookies=self.cookies)
						if req.status_code!=200:return 'error'
						if req.text == '[]':return 'N'
						else:
							reqjs=json.loads(req.text[1:][:-1])
							txt='收信結果'
							txt+=f"\n發送者:{reqjs['sender']}"
							txt+=f"\n時間:{reqjs['sentDate']}"
							txt+=f"\n主旨:{reqjs['subject']}"
							txt+=f"\n內容:{reqjs['bodyPreview']}"
							return txt
					else:return 'expired'
				except Exception as e:return str(e)
print('歡迎使用幻想信箱py\n請勿作為商業用途')
mail=mail()
print(mail.getmail())
while True:
	try:
		get=mail.getmessage()
		if get =='expired':print('過時');break
		if get =='error':print('非200狀態錯誤');break
		if get =='N':pass
		else:print(get);break
		time.sleep(5)#anti ban
	except KeyboardInterrupt:print('Ctrl-C');os._exit(1)
	except Exception as e:print(str(e))