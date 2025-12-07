# Dlib compiled wheels for Python 3.7, 3.8, 3.9, 3.10, 3.11 for Windows 10 X64
Dlib compiled binary (.whl) for python 3.7, 3.8, 3.9 for windows x64

After wasting a lot of time to get these files, I compiled them myself.

## Installation:

### solution 1:

PIP direct from Github :

```
pip install https://github.com/sachadee/Dlib/raw/main/wheel_for_your_python_version.whl
```
Example:

```
pip install https://github.com/sachadee/Dlib/raw/main/dlib-20.0.0-cp310-cp310-win_amd64.whl
```
### solution 2 (Downloading the wheel):

1- Download the file you need

2- copy it in the root folder of your python distribuition

3- open a cmd shell in the your root python folder 

example:
```
cd c:\python37
```

4- Install DLIB true PIP

### python 3.7
```
python -m pip install dlib-19.22.99-cp37-cp37-win_amd64.whl 
```
### python 3.8
```
python -m pip install dlib-19.22.99-cp38-cp38-win_amd64.whl
```
### python 3.9
```
python -m pip install dlib-19.22.99-cp39-cp39-win_amd64.whl
```
### python 3.10

#### Should work directly with: 

```
pip install dlib
```

#### If not:

DLIB Version 19.22.99

```
python -m pip install dlib-19.22.99-cp310-cp310-win_amd64.whl
```

DLIB Version 20.0.0
```
python -m pip install dlib-20.0.0-cp310-cp310-win_amd64.whl
```
### python 3.11
```
python -m pip install dlib-19.24.1-cp311-cp311-win_amd64.whl
```
That's it

