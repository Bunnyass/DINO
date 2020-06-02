import pyautogui
from PIL import Image, ImageGrab
import time
#from numpy import asarray

def hit(key):
    pyautogui.keyDown(key)


def isCollide(data):

    #Bird
    for i in range(750,770):
        for j in range(205,283):
            if data[i,j] == "#9aa0a6"  :
                hit("down")
                return True
    
    #Cactus
    for i in range(750,770):
        for j in range(283,320):
            if data[i,j] > 150:
                hit("up")
                return True
    return False  

if __name__ == '__main__':
    print("Hey, Dino game is about to start in 3 seconds")
    time.sleep(3)
    hit('up')
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)
    #    print(asarray(image))
        """
        #Draw the rectangle for cactus
        #for i in range(700,730):
        #    for j in range(283,320):
        #        data[i,j] = 0

        #Draw the rectangle for bird
        for i in range(700,730):
            for j in range(205,283):
                data[i,j] = 166

        image.show()
        break
    """
    
    