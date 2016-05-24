# Script to convert images to lmdb file format
# Input arguements:
	# 1. Root location of the dataset:
	# 2. Save location for the created lmdb file:
	# 3. [Optional] Name of the lmdb file to be created:

# Packages
import lmdb
from PIL import Image
import numpy as np
import glob
from random import shuffle
import sys
import os
sys.path.append("/home/silver005/NnFcn/SceneParsin/caffe/python")
import caffe

# Read the input arguements:
Inputs = sys.argv

if (len(Inputs) <= 2):
	print("Not enough input arguements. \n Atleast two arguements needed \n 1. Root location of the dataset \n 2. Save location for the created lmdb file")
	sys.exit()

else:
	RootDir = Inputs[1]
	DestDir = Inputs[2]
	if(len(Inputs) == 4):
		FileName = Inputs[3]
	else:
		FileName = 'data_lmdb'

	if (not (os.path.exists(RootDir))):
		print("Root Directory does not exist")
	elif (not (os.path.exists(DestDir))):
		print("Destination Directory does not exist")
	else:
		print("Setting up files for conversion.....")

# Read the Files from the Database:
SubDir = glob.glob(RootDir + "*")

ImgList = []

for j in range(0,len(SubDir)):
	# Save all the Image details
	ImgList = ImgList + sorted(glob.glob(SubDir[j] + "/*.png"))

print(RootDir, DestDir, FileName)

#Creating the LMDB file
print('Converting {0!s} images to LMDB'.format(len(ImgList)))
in_db = lmdb.open(DestDir + FileName,map_size=int(1e12)) # Open lmdb file

with in_db.begin(write=True) as in_txn:

	for in_idx, in_ in enumerate(ImgList):
	
		image = np.array(Image.open(in_))
		image = image[:,:,::-1]
		image = image.transpose((2,0,1))
		image_dat = caffe.io.array_to_datum(image)
		in_txn.put('{:0>10d}'.format(in_idx),image_dat.SerializeToString())
in_db.close()
print("Successfully created the LMDB file")

