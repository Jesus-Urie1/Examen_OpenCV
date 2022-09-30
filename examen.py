from logging import captureWarnings
import nntplib
from tkinter import N
from tkinter.tix import Tree
import cv2
import os.path as path
import numpy as np
#Alumno: Abdiel Jefte Santillan Luna
CapPantalla = cv2.VideoCapture(0)
n='0'
nn =1
if not CapPantalla.isOpened():
    raise IOError("No se puede abrir la camara")
while True:
    ret, frame = CapPantalla.read()
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    cv2.imshow('Camara',frame)
    c = cv2.waitKey(1)
    

    if c == 27:
        break
    elif c == 32:
        CapPantalla.set(cv2.CAP_PROP_FRAME_WIDTH,720) # ancho
        CapPantalla.set(cv2.CAP_PROP_FRAME_HEIGHT,640) # alto
        NombreImagen = "rostro"
        ExtencionDeImagen = ".jpg"
        image = '/home/jesuslap/Documents/Workspace/OpenCV/Examen/rostro'+n+ExtencionDeImagen
        if path.exists(image):
            while path.exists(image):
                nn = nn + 1
                n=str(nn)
                print(n)
                image = '/home/jesuslap/Documents/Workspace/OpenCV/Examen/rostro'+n+ExtencionDeImagen
                if path.exists(image) != True:
                    cv2.imwrite('/home/jesuslap/Documents/Workspace/OpenCV/Examen/'+NombreImagen+n+ExtencionDeImagen,frame)
                    img = cv2.imread('/home/jesuslap/Documents/Workspace/OpenCV/Examen/'+NombreImagen+n+ExtencionDeImagen)
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    gray = cv2.medianBlur(gray, 5)
                    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
                    color = cv2.bilateralFilter(img, 9, 300, 300)

                    # 3) Cartoon
                    cartoon = cv2.bitwise_and(color, color, mask=edges)
                    
                    cv2.imwrite('/home/jesuslap/Documents/Workspace/OpenCV/Examen/rostroCartun'+n+ExtencionDeImagen,cartoon)
                    cv2.imshow("Cartoon", cartoon)
                    break
        else:
            cv2.imwrite('/home/jesuslap/Documents/Workspace/OpenCV/Examen/'+NombreImagen+n+ExtencionDeImagen,frame)
            img = cv2.imread('/home/jesuslap/Documents/Workspace/OpenCV/Examen/'+NombreImagen+n+ExtencionDeImagen)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            gray = cv2.medianBlur(gray, 5)
            edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
            color = cv2.bilateralFilter(img, 9, 300, 300)

            # 3) Cartoon
            cartoon = cv2.bitwise_and(color, color, mask=edges)
            
            cv2.imwrite('/home/jesuslap/Documents/Workspace/OpenCV/Examen/rostroCartun'+n+ExtencionDeImagen,cartoon)
            cv2.imshow("Cartoon", cartoon)
      

CapPantalla.release()
cv2.destroyAllWindows()