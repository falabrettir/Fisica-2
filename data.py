import cv2 as cv 
import pandas as pd 



data = [] # hashmap de posições e tempos

frame_rate = round(1/30, 2) #30 fps

def capture(sec):
    cap = cv.VideoCapture('falabro.mp4')
    cap.set(cv.CAP_PROP_POS_MSEC, sec*1000)
    ok, frame = cap.read()
    if ok:
        frame = bin(frame)
        pos = cm(frame)
        data.append({"pos":pos, "t":sec})
    return ok

def bin(frame):

    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) #grey scaling
    frame = cv.medianBlur(frame, 5) #aplica blur
    frame = cv.threshold(frame, 100, 255, cv.THRESH_BINARY_INV)[1] #binariza invertido

    return frame

def cm(frame):
    momentos = cv.moments(frame)
    return int(momentos["m10"]/momentos["m00"]) #momentos de imagem para calcular o centro de massa
  
sec = 0
ok = capture(sec)
while ok:
    sec += frame_rate
    sec = round(sec, 2) #loop principal
    ok = capture(sec)
    
csv = pd.DataFrame(data) #escreve os dados do hash em um .csv 
csv.to_csv("data.csv", index = False)
