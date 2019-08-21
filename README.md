# Kuku-Kube-Bot
[Kuku Kube](https://www.kuku-kube.com/) is a webgame about clicking the one square out of many that is colored differently. Each round, there are more and more squares, so it gets progressively more difficult. Try playing it and see what you score!

#### Notice :
I use the term "bot" really loosely here. In reality this code is super, SUPER hardcoded, to the point that in it's current form, it really only works on my machine. 

The script takes into account what I'll call "pixel coordinates" for each of the squares on the screen, which will change for each person depending on their screen size and resolution.

This was my first, real simple script project in Python. In the future I might try to make the script universal, in that, it works on any machine when run. Eventually I'll also make a video of the script in action.

## Getting Started
This script uses a few 3rd party libraries and modules, each of which need to be installed in order for the script to work. As the case with most Python projects, I recommend using a virtual environment too.

### Prerequisites
You're going to need some sort of package manager to install the required modules. I personally prefer pip, or pip3 for Python 3. 

* Pillow - Python Imaging Library : [Website](https://python-pillow.org), [PyPi page](https://pypi.org/project/Pillow/)
* PyAutoGui - Used for moving mouse around and clicking the screen : [Website](https://pyautogui.readthedocs.io/en/latest/), [PyPi page](https://pypi.org/project/PyAutoGUI/)
* PyScreeze - Used to take temporary screenshots : [Github Repo](https://github.com/asweigart/pyscreeze), [PyPi page](https://pypi.org/project/PyScreeze/)

