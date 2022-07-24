import pyautogui
import pyperclip

# 任务列表
taskList = [
    {"type": "单击图片", "content": "red1.png"},
    {"type": "输入文字", "content": "爱你呦"},
    {"type": "单击图片", "content": "send.png"}
]


# 左键点击指定图片，点击成功返回true,找不到图片返回false;
def mouse_click(img):
    location = pyautogui.locateCenterOnScreen(img, confidence=0.9)
    print("location:", location)
    if location is not None:
        pyautogui.click(location.x, location.y, clicks=1, interval=0.2, duration=0.2, button="left")
        return True
    else:
        return False


# 执行任务
def do_task(task):
    print("task:", task)
    # 判断任务类型
    if task["type"] == "单击图片":
        img = task['content']  # 获取图片名称
        return mouse_click(img)  # 返回操作结果
    elif task["type"] == '输入文字':
        text = task['content']  # 获取文本
        pyperclip.copy(text)  # 拷贝文本
        pyautogui.hotkey('ctrl', 'v')  # 粘贴文本
        print("粘贴文本成功")
    return True


# 主函数
while True:
    i = 0
    while i < len(taskList):
        if do_task(taskList[i]):
            i += 1
        else:
            print("监听中...")
