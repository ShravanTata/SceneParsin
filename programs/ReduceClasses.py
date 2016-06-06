# To reduce the input image size of labels in the dataset:

import glob

import os

from PIL import Image

import cv2 

import numpy as np

RWidth = 640

RHeight = 320



# Save the directories

DirRoot = "/home/silver005/NnFcn/"

DirList = glob.glob(DirRoot + "labels/gtCoarse/*") # Extract List of directories

# Run through the three direct directories
for i in range(0,2):	
	
	SubDir = glob.glob(DirList[i] + "/*") # Extract list of sub-directories	

	for j in range(0,len(SubDir)):
		
		NewDir = DirRoot + "CompressedLabels/" + SubDir[j].replace(DirRoot+"labels/gtCoarse/","")
		
		if not os.path.exists(NewDir):
			os.makedirs(NewDir)

		ImgList = glob.glob(SubDir[j] + "/*_labelIds.png") # Extract list of Images

		for k in range(0,len(ImgList)):

			Img = cv2.imread(ImgList[k]) # Read the Image 
	
			# Class void - 0
			for m in range(0,7):
				Img[Img == m] = 0

			#class flat - 1
                        for m in range(7,11):
                                Img[Img == m] = 1

			 # Class Construction - 2
                        for m in range(11,21):
                                Img[Img == m] = 2

			 # Class Nature - 4
                        for m in range(21,24):
                                Img[Img == m] = 3

			 # Class Do Not Hit - 5
                        for m in range(24,34):
                                Img[Img == m] = 4


			Img[Img == -1] = 4

			Img = Img[:,:,1]

			Img = cv2.resize(Img, (RWidth, RHeight),interpolation =  cv2.INTER_NEAREST)
			
			cv2.imwrite(NewDir + ImgList[k].replace(SubDir[j],""), Img)
	
	

		


	


