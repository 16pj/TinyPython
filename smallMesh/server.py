from flask import Flask
import os
from multiprocessing.dummy import Pool as ThreadPool 

app = Flask(__name__)



def sampleFunction(myArray):
	'''returns array relative to the first value'''
	resultArray = []
	#print os.getpid()
	for i in myArray:
		if i == myArray[0]:
			resultArray.append(myArray[0])
		else:
			resultArray.append(i-myArray[0])
	return resultArray

def handleThread(myArrayofArrays):
	results = []
	pool = ThreadPool(len(myArrayofArrays)) 
	results = pool.map(sampleFunction, myArrayofArrays)
	return results


@app.route("/")
def root():
	msg = '''Welcome to my server.<br>
This is a P2P server that works using threads<br>
pass argument array or arrays separated by colon [:]<br>
This returns an array with elements relative to the first element<br>
eg: localhost:5000/calculate/1,2,3,4:2,3,4:6,7,8<br>
result: [[1, 1, 2, 3], [2, 1, 2], [6, 1, 2]]'''
	return msg
    
@app.route("/calculate/<string:strarray>")
def readArray(strarray):
	myArrayofArrays = []
	tmpArroArr = strarray.split(":")
	print tmpArroArr
	
	for tmpArr in tmpArroArr:
		myArrayofArrays.append([int(i) for i in tmpArr.split(",")])
	print myArrayofArrays
	
	# actual function
	results = handleThread(myArrayofArrays)
	
	return str(results)
	
if __name__ == '__main__':
	
	app.run('0.0.0.0',5000, debug=True)


