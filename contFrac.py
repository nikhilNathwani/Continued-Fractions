import time
import math
import sys
import matplotlib.pyplot as plt

def mySqrt(num,stop):
	return 1+evalContFrac([num-1,2],0,True,stop)

def getError(num,stop):
	return math.sqrt(num)-(1+evalContFrac([num-1,2],0,True,stop))

def getStopForWindow(num,window,func):
	stop= 0
	sqrt= 0
	real= math.sqrt(num)
	while (sqrt < real - window/2) or (sqrt > real + window/2):
		stop= stop+1
		sqrt= func(num,stop)
	return stop

#addDiv is 0 if adding, 1 if dividing
def evalContFrac(seq,seqCount,addDiv,stop):
	if stop==0:
		if not addDiv:
			return 1
		else:
			return 0
	else:
		if not addDiv:
			return seq[seqCount] + float(evalContFrac(seq,(seqCount+1)%len(seq),not(addDiv),stop-1))
		else:
			return seq[seqCount] / float(evalContFrac(seq,(seqCount+1)%len(seq),not(addDiv),stop-1))


def evalContFracFast(num,stop):
	num= num-1
	curr= 2
	seqNum= 0
	while stop >= float(stop)/2:
		if seqNum%2==0:
			curr= float(num)/curr
			stop= stop-1
		else:
			curr= float(2)+curr
		seqNum= seqNum+1

	return 1+curr	


if __name__=="__main__":

	#Comparing speed of mySqrt to built-in sqrt
	'''start= time.time()
	print mySqrt(int(sys.argv[1]),int(sys.argv[2]))
	print time.time()-start

	start= time.time()
	print math.sqrt(int(sys.argv[1]))
	print time.time()-start'''

	#Comparing speed to compute many square roots
	'''stopVal= 50
	start= time.time()
	for num in range(2,100,1):
		s= mySqrt(num,stopVal)
	print time.time()-start

	start= time.time()
	for num in range(2,100,1):
		s= math.sqrt(num)
	print time.time()-start'''


	#Finding stopping points for different square roots
	start= time.time()
	endVal= int(sys.argv[1])
	values= range(2,endVal)
	window= 0.002

	plt.plot(values, map(lambda x: getStopForWindow(x,window,evalContFracFast),values))
	plt.plot(values, map(lambda x: getStopForWindow(x,window,mySqrt),values))
	plt.axis([0, endVal, 0, endVal])
	plt.xlabel('Calculating sqrt of...')
	plt.ylabel('# Computations')	
	plt.title('# Computation Needed to have Absolute Error < 0.001')
	print time.time()-start
	plt.show()


	#Evaluating intermediate values along the calculation
	'''prev= -1000
	val= int(sys.argv[1])
	stops= range(80,150)
	for stop in stops:
		e= 1+evalContFrac([val-1,2],0,True,stop)
		direc= "UP" if prev < e else "DOWN"
		opp= "ADD" if stop%2 else "DIV"
		window= (math.sqrt(val)-e > -0.001 and math.sqrt(val)-e < 0) or (math.sqrt(val)-e < 0.001 and math.sqrt(val)-e > 0)
		print opp, direc, math.sqrt(val)-e, window, stop

	#Error line
	#plt.plot(stops,map(lambda x: getError(val,x),stops))
	#Actual value line
	plt.plot(stops,map(lambda x: abs(getError(val,x)),stops),'b')
	plt.axhline(y=0,xmin=0,xmax=max(stops),c="red")
	plt.xlabel('# Computations')
	plt.ylabel('Absolute Error')	
	plt.title('Absolute Error of sqrt('+str(val)+') Approximation vs. # Computations')
	plt.show()'''

	'''start= time.time()
	val= int(sys.argv[1])
	stopVal= int(sys.argv[2])
	start= time.time()
	print evalContFracFast(val-1,stopVal)
	print time.time()-start
	start= time.time()
	print mySqrt(val,stopVal)
	print time.time()-start
	start= time.time()
	print math.sqrt(val)
	print time.time()-start'''

