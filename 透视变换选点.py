# -*- coding: utf-8 -*-
"""
Created on Tue Mar 25 17:28:40 2025

@author: 寻木
"""

import cv2
import msvcrt
import os

img=cv2.imread("1.png")
img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
imgori=img.copy()
all_point=[[0,0],[0,0],[0,0],[0,0]]
img=cv2.resize(img,(int(img.shape[1]*0.5),int(img.shape[0]*0.5)))
img1=img.copy()
step=10
print("使用方法：\n\n1.输入点的坐标，然后按任意方向键查看图中的位置\n\n2.位置不满意即可使用方向键移动\n(若发现按下方向键没反应可以鼠标点一下图片的窗口再试试)\n\n3.若满意，按回车即可保存\n\n4.若想换一个位置和移动的步长，按esc即可\n\n\n")
for k in range (0,4):
    
    while True:
        print("请输入第"+str(k+1)+"个点的像素点的位置：")
        x0 = (input("请输入x坐标\n\n"))
        y0= (input ("请输入y坐标\n\n"))
        
        if len(x0)!=0 and len(y0)!=0 and str(int(x0))==x0 and str(int(y0))==y0:
            x0 = int(x0)
            y0= int(y0)
            
            break
    
    while True:
       key1=msvcrt.getch() 
       
       if key1==b'\r': #回车键
           all_point[k]=[x0,y0]
           print("cv2坐标(左上角为原点)为\n")
           print (x0,y0)
           break
       elif key1==b'\x1b': #输入键，esc
           
           img1=img.copy()

           while True:
               print("请输入第"+str(k+1)+"个点的像素点的位置：")
               x0 = (input("请输入x坐标\n\n"))
               y0= (input ("请输入y坐标\n\n"))
               step=int(input("请输入方向键步长\n\n"))
               if 0 < step <200 and len(x0)!=0 and len(y0)!=0 and str(int(x0))==x0 and str(int(y0))==y0:
                   x0 = int(x0)
                   y0= int(y0)
                   break
           x=int(x0/2)
           y=int(y0/2)
           if 0 <= x < img1.shape[1] and 0 <= y < img1.shape[0]:
               for i in range (0,10):
                   for j in range (0,10):
                       img1[y+i,x+j]=(0,0,255)
                       img1[y-i,x-j]=(0,0,255)
                       
               cv2.imshow("1",img1)
               cv2.waitKey(0)
               cv2.destroyAllWindows()
           else:
               continue
           print (x0,y0)
           
       elif key1==b'H' or key1==b"P" or key1==b"K" or key1==b"M":
           
           img1=img.copy()
           
           if key1==b'H' : #方向键上
               y0-=step
           elif key1==b"P" : #方向键下
               y0+=step
           elif key1==b"K" : #方向键左
               x0-=step
           elif key1==b"M" : #方向键右
               x0+=step
           x=int(x0/2)
           y=int(y0/2)
           if 0 <= x < img1.shape[1] and 0 <= y < img1.shape[0]:
               for i in range (0,10):
                   for j in range (0,10):
                       img1[y+i,x+j]=(0,0,255)
                       img1[y-i,x-j]=(0,0,255)
                       
               cv2.imshow("1",img1)
               cv2.waitKey(0)
               cv2.destroyAllWindows()
           else:
               continue
           print (x0,y0)
           
       
       
       
       
for k in range (0,4):
    #print("自然坐标系下：")
    print(all_point[k][0],all_point[k][1])
    print("\n\n\n")
    x=all_point[k][0]
    y=all_point[k][1]
    for i in range (0,10):
        for j in range (0,10):
            imgori[y+i,x+j]=(0,0,255)
            imgori[y-i,x-j]=(0,0,255)
    

    
cv2.imshow("1",imgori)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("2.png",imgori)
os.system("pause")
