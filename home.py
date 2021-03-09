#-*- coding: utf-8 -*-
from flask import Flask ,render_template,request
import datetime, json, codecs, time, os, threading, playsound
chk = 0
app = Flask(__name__)
logfile = "C:\\Users\\jswcy\\Desktop\\iot\\templates\\log.txt"
@app.route('/led')
def ledpage():
    return render_template('led.html')
@app.route('/login', methods=['POST'])
def register():
	with open('C:\\Users\\jswcy\\Desktop\\iot\\templates\\register.json',encoding='UTF-8') as data:
		registerData = json.load(data,encoding='UTF-8')
	registerData['user'][0]={"1":"mom"},{"2":"dad"}
	print(registerData)
	return render_template('family.html')
@app.route('/')
def main():
	return render_template('main.html')
@app.route('/ring', methods=['POST'])
def testform():
	f=open(logfile,'w')
	f.write("")
	return render_template('home.html',recent = "None")
@app.route('/family')
def fam():
	return render_template('family.html')
@app.route('/ring')
def home():
	recentDate = None
	f = open(logfile,'r')
	data = f.read()
	data_split = data.split(',')
	f.close()
	for i in data_split:
		if i != '':
			recentDate = i
	return render_template('home.html',recent = recentDate,date = data_split)
@app.route('/ring/requestVisit')
def response():
	test1 = threading.Thread(target=playmusic)
	test1.start()
	f = open(logfile,'a')
	date = datetime.datetime.now()
	dateStr = date.strftime("[%Y-%m-%d  %H:%M]")
	f.write(dateStr+",")
	f.close()
	return render_template('main.html')
def playmusic():
	playsound.playsound('C:\\Users\\jswcy\\Desktop\\iot\\static\\bam.mp3', True) 
if __name__ == '__main__':
	app.run(host='0.0.0.0', port =5000, debug=True)