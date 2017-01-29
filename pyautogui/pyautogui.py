import pyautogui as pag

0. 常用函数
pyautogui.position()
pyautogui.size()

# (x,y)是否在屏幕上
pyautogui.onScreen(x, y)

# PyAutoGUI函数增加延迟为2.5秒
pyautogui.PAUSE = 2.5
# 当pyautogui.FAILSAFE = True时，如果把鼠标光标在屏幕左上角，PyAutoGUI函数就会产生pyautogui.FailSafeException异常。
pyautogui.FAILSAFE = True

1. 鼠标动作
1.1. 移动
pyautogui.moveTo(x=moveToX, y=moveToY, duration=num_seconds)

1.2. 点击
pyautogui.click(x=moveToX, y=moveToY, 
	clicks=num_of_clicks, 
	interval=secs_between_clicks, 
	button='left') # left/middle/right
# 下面的函数可读性更好
pyautogui.rightClick(x=moveToX, y=moveToY)
pyautogui.middleClick(x=moveToX, y=moveToY)
pyautogui.doubleClick(x=moveToX, y=moveToY)
pyautogui.tripleClick(x=moveToX, y=moveToY)
1.3. 滚轮滚动
pyautogui.scroll(clicks=amount_to_scroll, x=moveToX, y=moveToY)

1.4. 拖拽
pyautogui.dragTo(x=dragToX, y=dragToY, duration=num_seconds, button='left')

1.5. mouseDown/mouseUp
pyautogui.mouseDown(x=moveToX, y=moveToY, button='left')
pyautogui.mouseUp(x=moveToX, y=moveToY, button='left')

1.6. 缓动Tween/渐变Easing
#  开始很慢，不断加速
pyautogui.moveTo(x, y, duration, pyautogui.easeInQuad)
#  开始很快，不断减速
pyautogui.moveTo(x, y, duration, pyautogui.easeOutQuad)
#  开始和结束都快，中间比较慢
pyautogui.moveTo(x, y, duration, pyautogui.easeInOutQuad)
#  一步一徘徊前进
pyautogui.moveTo(x, y, duration, pyautogui.easeInBounce)
#  徘徊幅度更大，甚至超过起点和终点
pyautogui.moveTo(x, y, duration, pyautogui.easeInElastic)


2. 键盘动作
2.1. 按键 press
pyautogui.press(key_name)

2.1. 键盘热键 hotkey
pyautogui.hotkey(key_name1, key_name2, key_name3)

2.2. 键盘输入 typewrite
pyautogui.typewrite(string_to_input, interval=num_seconds)

2.3. keyDown/keyUp
pyautogui.keyDown(key_name)
pyautogui.keyUp(key_name)


3. 截屏函数
#  返回一个Pillow/PIL的Image对象
pyautogui.screenshot()
pyautogui.screenshot('foo.png')

#  返回(最左x坐标，最顶y坐标，宽度，高度)
pyautogui.locateOnScreen('looks.png')
pyautogui.locateAllOnScreen('looks.png') # 寻找所有相似图片，返回一个生成器
pyautogui.locateCenterOnScreen('looks.png') # 返回图片在屏幕上的中心XY轴坐标值


4. 消息弹窗函数

pyautogui.alert('这个消息弹窗是文字+OK按钮')
pyautogui.confirm('这个消息弹窗是文字+OK+Cancel按钮，返回值是OK/Cancel')
pyautogui.confirm(text, title, buttons = buttonList)

pyautogui.prompt('这个消息弹窗是让用户输入字符串，单击OK')