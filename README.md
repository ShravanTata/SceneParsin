# SceneParsin
Neural Networks : Deep CNN for semantic scene parsing

This repository is for us to work and share our code for the Neural Networks project. 

#IMPORTANT
While making commits please give a good description of what changes you are making.

#Steps to Install CAFFE: (Ubuntu)
Verified for ubuntu 14.04

## Installing Dependencies 
1. apt-get remove ipython (should be installed by pip)

2. apt-get install libprotobuf-dev libleveldb-dev libsnappy-dev libopencv-dev libboost-all-dev libhdf5-serial-dev

3. apt-get install gfortran qt4-default python-dev

4. apt-get install libgflags-dev libgoogle-glog-dev liblmdb-dev protobuf-compiler

5. apt-get install libatlas-base-dev  (or compile by yourself for better performance)

6. In [INSTDIRofCAFFE]/python:

for req in $(cat requirements.txt); do pip install $req --proxy $https_proxy; done

7. pip install pyzmq 

8. pip install pyside 

9. pip install pydot 

10. pip install flask 

11. pip install jinja2 

12. pip install tornado 

13. pip install jsonschema 

14. In [INSTDIRofCAFFE]:

cp Makefile.config.example Makefile.config

# Adjust Makefile.config for using CPU – not CUDA

# INCLUDE_DIRS := $(PYTHON_INCLUDE) /usr/local/include

# LIBRARY_DIRS := $(PYTHON_LIB) /usr/local/lib /usr/lib

15. make

16. make pycaffe

17. make test

18. make runtest
