from flask import Flask
import os
from multiprocessing.dummy import Pool as ThreadPool 
import subprocess

app = Flask(__name__)



def myDivideFunction(myArray):
	'''returns array relative to the first value'''
	resultArray = []
	#print os.getpid()
	for i in myArray:
		if i == myArray[0]:
			resultArray.append(myArray[0])
		else:
			resultArray.append(i/myArray[0])
	return resultArray

def mySubtractFunction(myArray):
	'''returns array relative to the first value'''
	resultArray = []
	#print os.getpid()
	for i in myArray:
		if i == myArray[0]:
			resultArray.append(myArray[0])
		else:
			resultArray.append(i - myArray[0])
	return resultArray

def handleThread(myArrayofArrays, myFunction):
	results = []
	pool = ThreadPool(len(myArrayofArrays)) 
	results = pool.map(myFunction, myArrayofArrays)
	return results

@app.route("/neighbors")
def neighbors():
	cmd = '''nmap -sn 192.168.1.0/24 --exclude 192.168.1.1 | grep -o 192.*'''
	sub = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
	out, err = sub.communicate()
	
	ips = out.split()
	clean_ips = [ip.strip() for ip in ips]
	ip_msg = ', '.join(clean_ips)
	return ip_msg


@app.route("/")
def root():
	msg = '''Welcome to my server.<br>
This is a P2P server that works using threads<br>
pass argument array or arrays separated by colon [:]<br>
This returns an array with elements relative to the first element<br>
eg: localhost:5000/calculate/1,2,3,4:2,3,4:6,7,8<br>
result: [[1, 1, 2, 3], [2, 1, 2], [6, 1, 2]]'''
	return msg
    
@app.route("/divide/<string:strarray>")
def divideFunc(strarray):
	myArrayofArrays = []
	tmpArroArr = strarray.split(":")
	print tmpArroArr
	
	for tmpArr in tmpArroArr:
		myArrayofArrays.append([int(i) for i in tmpArr.split(",")])
	print myArrayofArrays
	
	# actual function
	results = handleThread(myArrayofArrays, myDivideFunction)
	
	return str(results)

@app.route("/subtract/<string:strarray>")
def subFunc(strarray):
	myArrayofArrays = []
	tmpArroArr = strarray.split(":")
	print tmpArroArr
	
	for tmpArr in tmpArroArr:
		myArrayofArrays.append([int(i) for i in tmpArr.split(",")])
	print myArrayofArrays
	
	# actual function
	results = handleThread(myArrayofArrays, mySubtractFunction)
	
	return str(results)

if __name__ == '__main__':
	
	app.run('0.0.0.0',5000, debug=True)


