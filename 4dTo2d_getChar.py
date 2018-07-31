#!/usr/bin/env python

'''
Mac OS X: ValueError: unknown locale: UTF-8 in Python, matplotlib 
add these lines to your ~/.bash_profile 
export LC_ALL=en_US.UTF-8 
export LANG=en_US.UTF-8 
'''

import sys
import matplotlib #as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

fallback=0
try: import getChar
except ImportError: 
	fallback = 1
	print ('error: in importing getChar.py \n falling back to mpl key capture')
#key input

dTheta = 5./180*np.pi
X,Y,Z,W = (0,1,2,3)

def loadObject():
	""" load 4D Object from file """
	if len(sys.argv)>1: 
		inputFile = sys.argv[1]
	else : print "usage: /4dTo2d.py filename.obj"; exit()

	inputLines = map(str.split, open(inputFile).readlines())

	vertises = []
	lines = []
	faces = []

	for iLine in inputLines:
		print '..', iLine, '..'
		if iLine==[] : continue

		if (iLine[0] == 'v'): vertises += [iLine[1:]]
		elif (iLine[0] == 'l'): lines += [iLine[1:]]
		elif (iLine[0] == 'f'): faces += [iLine[1:]]


	return (vertises, lines, faces)

def normalizeTo4Darray(vertises):
	""" returns a 4D numpy array for vertises """
	dimention = len(vertises[0])
	size = len(vertises)
	D4vertises = np.zeros((size,4), dtype=float)
	for i in range(size):
		#for j in range(len(vertises[i])):
		#	D4vertises[j][i] = vertises[i][j]
		D4vertises[i][:len(vertises[i])] = vertises[i]

	#normalize with range -1 to 1
	for i in range(4):
		iMax = D4vertises[:,i].max()
		iMin = D4vertises[:,i].min()
		iDiff = iMax-iMin
		if(iDiff!=0): 
			D4vertises[:,i] = (D4vertises[:,i]-(iMax+iMin)/2)*2/(iDiff)


	return D4vertises

def ontype(key):
	"""Deal with keyboard events"""
	event = key
	if fallback : event = key.key
	print("You pressed key {:s}".format(event))

	if (event == 'up'): rotate3D(Y,Z,dTheta)
	elif (event == 'down'): rotate3D(Y,Z,-dTheta)
	elif (event == 'left'): rotate3D(X,Y,dTheta)
	elif (event == 'right'): rotate3D(X,Y,-dTheta)
	elif (event == 'enter'): global D4vertises; D4vertises = np.copy(D4vertises_original)
	elif (event == 'w'): rotate3D(W,X,dTheta)
	elif (event == 'v'): rotate3D(W,X,-dTheta)
	elif (event == 't'): rotate3D(Y,W,dTheta)
	elif (event == 'n'): rotate3D(Y,W,-dTheta)
	elif (event == 'c'): rotate3D(Z,W,dTheta)
	elif (event == 'r'): rotate3D(Z,W,-dTheta)
	elif (event == 'q'): quit()

	display(D4vertises[:,:3])

def rotate3D(a,b,theta):
	""" rotate in 3D space along remaining axis """
	global D4vertises
	vertises = np.copy(D4vertises)
	D4vertises[:,a] = vertises[:,a]*np.cos(theta) + vertises[:,b]*np.sin(theta)
	D4vertises[:,b] = vertises[:,b]*np.cos(theta) - vertises[:,a]*np.sin(theta)


def display(vertises):
	""" plots the object on screen"""
	#ax.plot(vertises[:,0],vertises[:,1],vertises[:,2])
	#plt.cla()
	ax.cla() 

	#x,y,z = vertises[lines-1].T
	#print z.T
	#ax.plot(x.T, y.T, z.T[:,0])

	#for i in range(len(x)):
	#	ax.plot(x[i],y[i],z[i])
	
	#x,y,z = [],[],[]
	#plot lines
	for i,j in zip(vertises[lines[:,0]-1],vertises[lines[:,1]-1]):
		#x += [[i[0],j[0]],[None,None]]
		#y += [[i[1],j[1]],[None,None]]
		#z += [[i[2],j[2]],[None,None]]
		ax.plot([i[0],j[0]],[i[1],j[1]],[i[2],j[2]])

	color = []
	for i in range(size):
		if D4vertises[i,3]<0: color+='r'
		else : color+='b'
	#plot nodes/vertises with color code
	ax.scatter(D4vertises[:,0],D4vertises[:,1],D4vertises[:,2],'z',(D4vertises[:,3]+2)*100,color)

	ax.set_autoscale_on(0)
	ax.set_xlim3d(-2,2)
	ax.set_ylim3d(-2,2)
	ax.set_zlim3d(-2,2)

	plt.draw()
	plt.pause(0.05)


### main ###

vertises, lines, faces = loadObject()
lines = np.array(lines,dtype=int)
D4vertises = normalizeTo4Darray(vertises)
D4vertises_original = np.copy(D4vertises)
size = len(D4vertises)

fig = plt.figure()
#ax = fig.gca(projection='3d')
ax = fig.add_subplot(111, projection='3d')
#plt.show()

#ax.plot(D4vertises[:,0],D4vertises[:,1],D4vertises[:,2])
#plt.show()


display(D4vertises[:,:3])

if fallback: 
	fig.canvas.mpl_connect('key_press_event',ontype)
	plt.show()
else : 
	plt.ion()
	while True : 
		ch = getChar.getKey()
		ontype(ch)