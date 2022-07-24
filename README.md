# 个人PC端微信自动回复demo

## 基本实现方式
总的来说就是通过图像对比识别到未读消息，然后模拟点击发送
1. 通过组件`pyautogui`获取未读消息图片(代码中的red1.png)在屏幕中的x,y坐标，并点击
2. 通过`pyperclip`复制粘贴回复内容
3. 再通过`pyautogui`根据发送按钮图片(send.png)找到在屏幕中的位置，并点击完成消息发送

## 运行方式
1. cd到当前工程目录
2. pip install -r requirements.txt # 安装依赖包
3. python wechatRPA.py
> 如果发现识别不到未读消息的图片，自己截图，因为pyautogui是通过opencv实现的图片对比

## 感谢
[B站UP主-晓舟报告](https://www.bilibili.com/video/BV12q4y1u7FN?spm_id_from=333.880.my_history.page.click&vd_source=30d8ecd340b205acfab288af87853b04)  
[B站UP主-不高兴就喝水](https://www.bilibili.com/video/BV1T34y1o73U?spm_id_from=333.880.my_history.page.click&vd_source=30d8ecd340b205acfab288af87853b04)
