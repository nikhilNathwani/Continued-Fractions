import time
import math
import sys
import matplotlib.pyplot as plt

def mySqrt(num,stop):
	return evalConvergents(num,stop)

def getError(num,stop):
	return math.sqrt(num)-mySqrt(num,stop)

def getStopForWindow(num,window):
	stop= 0
	sqrt= 0
	real= math.sqrt(num)
	while (sqrt < real - window/2) or (sqrt > real + window/2):
		stop= stop+1
		sqrt= evalConvergents(num,stop)
	return stop

def evalConvergents(num,stop):
	x=1
	y=1
	first= 1
	second= 1
	while stop>0:
		x= first
		y= second
		first= x+y
		second= (num*x)+y
		stop= stop-1 
	return float(second)/float(first)


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
	values= range(20,endVal)
	window= 0.002

	print map(lambda x: getStopForWindow(x,window),values)
	print [x for x in map(lambda x: getStopForWindow(x,window),values) if x%2==1]

	plt.plot(values, map(lambda x: getStopForWindow(x,window),values))
	plt.axis([20, endVal, 35, endVal])
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

	start= time.time()
	val= int(sys.argv[1])
	stopVal= int(sys.argv[2])
	start= time.time()
	print evalConvergents(val,stopVal)
	print time.time()-start
	start= time.time()
	print mySqrt(val,stopVal)
	print time.time()-start
	start= time.time()
	print math.sqrt(val)
	print time.time()-start

