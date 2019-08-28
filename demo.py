import pyautogui
import time
#http://www.4399.com/flash/154247_3.htm
pyautogui.FAILSAFE=True

time.sleep(3)

while True:
    region=(566,588,400,20)
    im=pyautogui.screenshot(region=region)
    im.save('test.png')

    for i in range(50,375,100):
        px = im.getpixel((i,10))
        print(px)
        if px[0] == 1:
            pyautogui.click(region[0]+i,region[1]+10)
