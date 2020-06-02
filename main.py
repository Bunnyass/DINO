import pyautogui # pip install pyautogui
from PIL import Image, ImageGrab # pip install pillow
# from numpy import asarray
import time

def hit(key):
    pyautogui.keyDown(key)
    return

def isCollide(data):

    for i in range(760, 780):
        for j in range(283, 325):
            if data[i, j] > 150:
                hit("up")
                return True
    return False

if __name__ == "__main__":
    print("Hey.. Dino game about to start in 3 seconds")
    time.sleep(3)
    pyautogui.PAUSE = 0.01 

    while True:
        image = ImageGrab.grab().convert('L') 
        data = image.load()
        isCollide(data)
        
        """
        # Draw the rectangle for cactus
        for i in range(760, 780):
            for j in range(283, 325):
                data[i, j] = 0
        
        image.show()
        break
    """
    

