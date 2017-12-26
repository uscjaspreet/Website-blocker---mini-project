import time
from datetime import datetime as dt
host_temp='D:\Python-work\Hardway\website blocker\hosts'
host_path = 'C:\Windows\System32\drivers\etc\hosts'
redirect = '127.0.0.1'
website_list = ['https://www.facebook.com/','www.facebook.com','facebook.com']

while True:
	if dt(dt.now().year, dt.now().month, dt.now().day,4) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,22):
		print("Working hours...")
		with open(host_path,'r+') as file:
			content = file.read()
			for website in website_list:
				if website in content:
					pass
				else:
					file.write('\n'+redirect+' '+website)
	else:
		print("Fun hours...")
		with open(host_path,'r+') as file:
			content= file.readlines()	
			file.seek(0)
			for line in content:
				if not any(website in line for website in website_list):
					file.write(line)
			file.truncate()
	time.sleep(10)