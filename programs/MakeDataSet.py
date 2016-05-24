# To reduce the input image size of the dataset:

import glob

import os

from PIL import Image

RWidth = 640

RHeight = 320



# Save the directories

DirRoot = "/home/silver005/NnFcn/"

DirList = glob.glob(DirRoot + "leftImg8bit/*") # Extract List of directories

# Run through the three direct directories 
for i in range(0,3):	
	
	SubDir = glob.glob(DirList[i] + "/*") # Extract list of sub-directories	

	for j in range(0,len(SubDir)):
		
		NewDir = DirRoot + "Compressed/" + SubDir[j].replace(DirRoot+"leftImg8bit/","")
		
		if not os.path.exists(NewDir):
			os.makedirs(NewDir)

		ImgList = glob.glob(SubDir[j] + "/*") # Extract list of Images

		for k in range(0,len(ImgList)):

			Img = Image.open(ImgList[k]) # Read the Image 
	
			Img = Img.resize((RWidth, RHeight), Image.ANTIALIAS)		
			
			Img.save(NewDir + ImgList[k].replace(SubDir[j],""))
	
	

		


	


