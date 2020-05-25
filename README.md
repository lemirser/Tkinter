# Tkinter
Tkinter repo from the tutorial on codemy.com/ youtube.

You can follow the tutorial on [Youtube](https://www.youtube.com/playlist?list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV). Please note that I did not created this tutorial or videos, I'm just following it's tutorials.

Tkinter description directly from the youtube playlist:
> Tkinter is the fastest and easiest way to create the Graphic User Interfaces (GUI applications) with Python. Tkinter comes with Python already, so there's nothing to install!

## Creating Python Environment
1. Install `pipenv`.
```
$ cd \path\of\your\project\
$ pip3 install pipenv
$ pipenv install pillow
```
2. Activate the environment
```
$ cd \path\of\your\project\
$ pipenv shell
```

## Generate pipenv
Activate your venv, then run the commands below on your command line.
```
# For pipenv
$ pipenv shell
$ pipenv lock

# For pipenv (requirements.txt)
## This will generate a Pipfile.lock
$ pipenv lock -r

## This will generate a requirements.txt
$ pipenv run pip freeze > requirements.txt
```

## Install dependencies
```
# Install packages from the Pipfile.lock
$ pipenv sync

# Install packages from requirements.txt
$ pipenv install -r path/to/requirements.txt
```

## Update pipenv packages
* Check what changed upstream: `$ pipenv update --outdated`
* Two options to update packages:
  * Update all packages: `$ pipenv update`.
  * Specific package: `$ pipenv update <pkg>`.
