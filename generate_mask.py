# -*- coding: utf-8 -*-
import cv2
import numpy as np
lsPointsChoose = []
tpPointsChoose = []
pointsCount = 0
count = 0
pointsMax = 10
def on_mouse(event, x, y, flags, param):
    global img, point1, point2, count, pointsMax
    global lsPointsChoose, tpPointsChoose  # 存入选择的点
    global pointsCount  # 对鼠标按下的点计数
    global img2, ROI_bymouse_flag
    img2 = img.copy()  # 此行代码保证每次都重新再原图画  避免画多了
    if event == cv2.EVENT_LBUTTONDOWN:  # 左键点击
        pointsCount = pointsCount + 1
        print('pointsCount:', pointsCount)
        point1 = (x, y)
        print(x, y)
        cv2.circle(img2, point1, 10, (0, 255, 0), 2)
        lsPointsChoose.append([x, y])  # 用于转化为darry 提取多边形ROI
        tpPointsChoose.append((x, y))  # 用于画点
        print(len(tpPointsChoose))
        for i in range(len(tpPointsChoose) - 1):
            print('i', i)
            cv2.line(img2, tpPointsChoose[i], tpPointsChoose[i + 1], (0, 0, 255), 2)
        # 绘制区域
        if (pointsCount == pointsMax):
            ROI_byMouse()
            ROI_bymouse_flag = 1
            lsPointsChoose = []

        cv2.imshow('src', img2)
    if event == cv2.EVENT_RBUTTONDOWN:
        print("right-mouse")
        pointsCount = 0
        tpPointsChoose = []
        lsPointsChoose = []
        print(len(tpPointsChoose))
        for i in range(len(tpPointsChoose) - 1):
            print('i', i)
            cv2.line(img2, tpPointsChoose[i], tpPointsChoose[i + 1], (0, 0, 255), 2)
        cv2.imshow('src', img2)


def ROI_byMouse():
    global src, ROI, ROI_flag, mask2
    mask = np.zeros(img.shape, np.uint8)
    pts = np.array([lsPointsChoose], np.int32)
    pts = pts.reshape((-1, 1, 2))
    mask = cv2.polylines(mask, [pts], True, (255, 255, 255))
    # 绘制多边形
    mask2 = cv2.fillPoly(mask, [pts], (255, 255, 255))
    cv2.imshow('mask', mask2)
    cv2.imwrite('test_data_mask/8.png', mask2)
    ROI = cv2.bitwise_and(mask2, img)
# 输入测试图像
img = cv2.imread('images/r12946364t.png')
ROI = img.copy()
cv2.namedWindow('src')
cv2.setMouseCallback('src', on_mouse)
cv2.imshow('src', img)
cv2.waitKey(0)
