#!/usr/bin/env python

import sys
import random
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

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
		D4vertises[:,i] = (D4vertises[:,i]-(iMax+iMin)/2)*2/(iMax-iMin)


	return D4vertises

def ontype(event):
	"""Deal with keyboard events"""
	print("You pressed key {:s}".format(event.key))

	if (event.key == 'up'): rotate3D(Y,Z,dTheta)
	elif (event.key == 'down'): rotate3D(Y,Z,-dTheta)
	elif (event.key == 'left'): rotate3D(X,Y,dTheta)
	elif (event.key == 'right'): rotate3D(X,Y,-dTheta)
	elif (event.key == 'enter'): global D4vertises; D4vertises = np.copy(D4vertises_original)
	elif (event.key == 'w'): rotate3D(W,X,dTheta)
	elif (event.key == 'v'): rotate3D(W,X,-dTheta)
	elif (event.key == 't'): rotate3D(Y,W,dTheta)
	elif (event.key == 'n'): rotate3D(Y,W,-dTheta)
	elif (event.key == 'c'): rotate3D(Z,W,dTheta)
	elif (event.key == 'r'): rotate3D(Z,W,-dTheta)

	display(D4vertises[:,:3])

def rotate3D(a,b,theta):
	""" rotate in 3D space along remaining axis """
	global D4vertises
	vertises = np.copy(D4vertises)
	D4vertises[:,a] = vertises[:,a]*np.cos(theta) + vertises[:,b]*np.sin(theta)
	D4vertises[:,b] = vertises[:,b]*np.cos(theta) - vertises[:,a]*np.sin(theta)


def display(vertises):
	""" plots the object on screen"""
	#ax(ranDom).plot(vertises[:,0],vertises[:,1],vertises[:,2])
	plt.cla()

	#x,y,z = vertises[lines-1].T
	#print z.T
	#ax(ranDom).plot(x.T, y.T, z.T[:,0])

	#for i in range(len(x)):
	#	ax(ranDom).plot(x[i],y[i],z[i])
	
	#x,y,z = [],[],[]
	for i,j in zip(vertises[lines[:,0]-1],vertises[lines[:,1]-1]):
		#x += [[i[0],j[0]],[None,None]]
		#y += [[i[1],j[1]],[None,None]]
		#z += [[i[2],j[2]],[None,None]]
		ax{ranDom}.plot([i[0],j[0]],[i[1],j[1]],[i[2],j[2]])

	ax(ranDom).scatter(D4vertises[:,0],D4vertises[:,1],D4vertises[:,2],'z',(D4vertises[:,3]+2)*100)

	ax(ranDom).set_autoscale_on(0)
	ax(ranDom).set_xlim3d(-2,2)
	ax(ranDom).set_ylim3d(-2,2)
	ax(ranDom).set_zlim3d(-2,2)
	plt.draw()


### main ###

vertises, lines, faces = loadObject()
lines = np.array(lines,dtype=int)
D4vertises = normalizeTo4Darray(vertises)
D4vertises_original = np.copy(D4vertises)
size = len(D4vertises)

fig = plt.figure()
ranDom = random.random()
#ax(ranDom) = fig.gca(projection='3d')
ax  = {ranDom:fig.add_subplot(111, projection='3d')}

#ax(ranDom).plot(D4vertises[:,0],D4vertises[:,1],D4vertises[:,2])
#plt.show()

display(D4vertises[:,:3])
fig.canvas.mpl_connect('key_press_event',ontype)

plt.show()