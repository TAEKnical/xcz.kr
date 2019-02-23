import requests
from PIL import Image
from pytesseract import *
import re
from fractions import gcd
session_id={'PHPSESSID':''}

def OCR(imgfile, lang='eng'):
	img=Image.open(imgfile)
	text = image_to_string(img, lang=lang)

	return text

def color_change():
	img=Image.open("test1.jpg").convert("L")
	img.save("test1_gray.png")


def download_img():
	img_url="http://xcz.kr/START/prob/prob_files/prob25_img.php"
	img=requests.get(url=img_url,cookies=session_id).content
	filename="test1.jpg"
	with open(filename,"wb") as f:
		f.write(img)

def lcm(a,b):
	return a*b//(gcd(a,b))		#lcm = a*b/gcd

def submit(result):
	pf=-1
	submit_url="http://xcz.kr/START/prob/prob_files/prob25_ok.php?lcm="+str(result)
	# params={'lcm':result}
	response=requests.get(url=submit_url,cookies=session_id)
	print("전송완료")
	if "Failed" in response.text:
		print("Failed")
		pf=0
		print(pf)
		print(response.text)
	else:
		print(response.text)
		print("Successed")
		pf=1
		print(pf)
	return pf
while True:
	try:
		download_img()
		color_change()
		text=OCR("test1_gray.png")
		# text=re.findall("\d+",text)
		# text[1]=int(text[1])
		# text[2]=int(text[2])
		text=text.split(",")
		text[0]=re.findall("\d+",text[0])
		text[1]=re.findall("\d+",text[1])
		text[0]=int(text[0][0])#findall이 리스트로 반환하기 때문
		text[1]=int(text[1][0])
		result=lcm(text[0],text[1])
		if len(str(text[0]))==30 and len(str(text[1]))==30:
			print('+++ OCR Result +++')
			print(text)
			print(text[0])
			print(text[1])
			print(result)
			if submit(result)==1:
				print("성공!")
				break
			else:
				print("실패")
	except IndexError as e:
		print(e)

