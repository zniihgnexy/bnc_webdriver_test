import pyautogui

x,y = pyautogui.position() #获取鼠标当前位置
print ("x_location：{}，y_location：{}".format(x,y)) #控制台打印出来

screenWidth, screenHeight = pyautogui.size()
print(screenWidth, screenHeight)

