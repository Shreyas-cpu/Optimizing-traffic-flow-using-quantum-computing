import cv2
import numpy as np
import PIL as Image
import os
from os import listdir

frameCarNr = frameVehNr = frameNr = (x for x in range(1000))

# Use relative paths and os.path.join for cross-platform compatibility
CASCADE_DIR = os.path.join(os.path.dirname(__file__))
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")

# Ensure output directories exist
os.makedirs(os.path.join(OUTPUT_DIR, "Pedestrians"), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_DIR, "Two_Wheeler"), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_DIR, "Cars"), exist_ok=True)

def Ped(video_source : "str"):
    full_body = cv2.CascadeClassifier(os.path.join(CASCADE_DIR, 'pedestrians.xml'))
    cap = cv2.VideoCapture(video_source)
    global gray, framePed
    while cap.isOpened():
        framePed = cap.read()
        gray = cv2.cvtColor(framePed, cv2.COLOR_BGR2GRAY)
        body = full_body.detectMultiScale(gray, 1.2, 3)
        font = cv2.FONT_HERSHEY_SIMPLEX
        
        for (x,y,w,h) in body: 
            cv2.putText(framePed, 'Person', (x, y-5), font, 1, (255,255,0), 1, cv2.LINE_AA)
            cv2.rectangle(framePed,(x,y),(x+w,y+h),(255,255,0),2)
            cv2.imshow('Body Detection',framePed)
        
            cv2.imwrite(os.path.join(OUTPUT_DIR, 'Pedestrians', f'frame_{frameNr}.jpg'), framePed)
        
        k = cv2.waitKey(1)
        if k == 40:
            break
        
    cap.release() 
    cv2.destroyAllWindows()

def PC():
    ped_dir = os.path.join(OUTPUT_DIR, "Pedestrians")
    for images in os.listdir(ped_dir):
        if (images.endswith(".png") or images.endswith(".jpg") or images.endswith(".jpeg")):
            image_arr2 = np.array(images)
            cnt = 0
            for (x,y,w,h) in images:
                cv2.rectangle(image_arr2,(x,y),(x+w,y+h),(255,0,0),2)
                cnt += 1
                Image.fromarray(image_arr2)
    return 1

def Twheeler(T_video_src: str):
    cap = cv2.VideoCapture(T_video_src)
    car_cascade = cv2.CascadeClassifier(os.path.join(CASCADE_DIR, 'two_wheeler.xml'))
    while True:
        ret, img = cap.read()
        if (type(img) == type(None)):
            break
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        veh = car_cascade.detectMultiScale(gray,1.01, 1)
        for (x,y,w,h) in veh:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,215),2)
            cv2.imshow('2 wheeler detection', img)
            cv2.imwrite(os.path.join(OUTPUT_DIR, 'Two_Wheeler', f'frame_{frameVehNr}.jpg'), img)
        if cv2.waitKey(33) == 27:
            break
    cv2.destroyAllWindows()

def TWC():
    two_wheeler_dir = os.path.join(OUTPUT_DIR, "Two_Wheeler")
    for vehicles in os.listdir(two_wheeler_dir):
        if (vehicles.endswith(".png") or vehicles.endswith(".jpg") or vehicles.endswith(".jpeg")):
            image_arrVeh = np.array(vehicles)
            cntVeh = 0
            for (x,y,w,h) in vehicles:
                cv2.rectangle(image_arrVeh,(x,y),(x+w,y+h),(255,0,0),2)
                cntVeh += 1
                Image.fromarray(image_arrVeh)
    return 1

def cars(C_video_src : "str"):
    cap = cv2.VideoCapture(C_video_src)
    car_cascade = cv2.CascadeClassifier(os.path.join(CASCADE_DIR, 'cars.xml'))
    while True:
        ret, imgCars = cap.read()
        if (type(imgCars) == type(None)):
            break
        gray = cv2.cvtColor(imgCars, cv2.COLOR_BGR2GRAY)
        cars = car_cascade.detectMultiScale(gray, 1.1, 2)
        for (x,y,w,h) in cars:
            cv2.rectangle(imgCars,(x,y),(x+w,y+h),(0,255,255),2)
            cv2.imshow('video', imgCars)
            cv2.imwrite(os.path.join(OUTPUT_DIR, 'Cars', f'frame_{frameCarNr}.jpg'), imgCars)
    
        if cv2.waitKey(33) == 27:
            break

    cv2.destroyAllWindows()

def CCo():
    cars_dir = os.path.join(OUTPUT_DIR, "Cars")
    for cars in os.listdir(cars_dir):
        if (cars.endswith(".png") or cars.endswith(".jpg") or cars.endswith(".jpeg")):
            image_arrCar = np.array(cars)
            global cntCar
            cntCar = 0
            for (x,y,w,h) in cars:
                cv2.rectangle(image_arrCar,(x,y),(x+w,y+h),(255,0,0),2)
                cntCar += 1
                Image.fromarray(image_arrCar)
    return 1

def FRML():
    Main = list()
    dm = list()
    ML = list()
    for i in range(4):
        a = input("Input the path to pedestrian video source file:- ")
        b = input("Input the path to Two wheeler video source file:- ")
        c = input("Input the path to Car video source file:- ")
        Ped(a)
        Twheeler(b)
        cars(c)
        O = [float(CCo()+ TWC()), PC()]
        ML.append(O)
    Main.append(ML)
    dm.append(ML)
    global x, y
    x = float(input("Enter the X-Coordinate of Node:- "))
    y = float(input("Enter the Y-Coordiante of Node:- "))
    M = [x,y]
    Main.append(M)
    dm.append(M)
    t = int(input("Numbers of Nodes connected:- "))
    OP = list()
    for j in range(int(t)):
        N = str(input("Enter the Node Name:- "))
        OP.append(N)
    for i in range(4):
        Main[0][i].append(OP[i])
    A = Main[0]
    dm.append(A)
    return dm
