import cv2
import poseModule_1 as pm
import numpy as np

cap=cv2.VideoCapture(r'C:\Users\delbi\Videos\Computer vision\opencv\Project 2\Fitnes Tracker\Vrikshasana - Tree Pose _ Benefits _ Steps _ Yogic Fitness _ Art Of Living Yoga.mp4')
# cap=cv2.VideoCapture(0)

detector = pm.poseDetector()
while True:
    success ,image=cap.read()
#     image=cv2.resize(image,(1280,720))

    image=detector.findPose(image)
    lmlist=detector.findPosition(image)

    cv2.rectangle(image,(0,0),(1280,90),(0,0,0),cv2.FILLED)

    if len(lmlist)!=0:
        
        angle1=detector.findAngle(image,24,26,28)
        angle2=detector.findAngle(image,23,25,27)
        angle3=detector.findAngle(image,23,11,13)
        angle4=detector.findAngle(image,24,12,14)
        angle5=detector.findAngle(image,12,14,16)
        angle6=detector.findAngle(image,11,13,15)


        if angle1>180 and angle2>170 and angle3>90 and angle4>265 and angle5>109 and angle6>215:
              cv2.putText(image,'Prasaritha padottasam or Wide-legged forward bend',(10,60),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

        if angle1>180 and angle2>335 and angle3>165 and angle4>185 and angle5>185 and angle6>170:
              cv2.putText(image,'Vrikshasana or Tree Pose',(10,60),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

        if angle1>178 and angle2>180 and angle3>155 and angle4>150 and angle5>175 and angle6>190:
              cv2.putText(image,'Eka Padasana or One-Foot Pose',(10,60),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

        if angle1>184 and angle2>178 and angle3>209 and angle4>108 and angle5>176 and angle6>171:
              cv2.putText(image,'Ananda Thandavam or Shiva Dance',(10,60),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
        
        if angle1>180 and angle2>278 and angle3>299 and angle4>198 and angle5>196 and angle6>173:
              cv2.putText(image,'Parsva Konasana or Extented side angle pose',(10,60),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

        if angle1>255 and angle2>178 and angle3>344 and angle4>14 and angle5>27 and angle6>324:
              cv2.putText(image,'Garudasanna or Eagle Pose',(10,60),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

        if 180>angle1>169 and 278>angle2>189 and angle3>190 and angle4>88 and angle5>190 and angle6>45:
              cv2.putText(image,'Anantasanna or Sleeping Vishnu pose',(10,60),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

        if angle1>169 and angle2>245 and angle3>117 and angle4>220 and angle5>173 and angle6>120:
              cv2.putText(image,'Natarajasanna or Dancer Pose',(10,60),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

        if angle1>185 and angle2>176 and angle3>322 and angle4>62 and angle5>190 and angle6>243:
              cv2.putText(image,'Uthita Hasta Pandag Usthasana or Extended hand to big toe pose',(10,60),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

        if angle1>262 and angle2>262 and angle3>55 and angle4>55 and angle5>188 and angle6>183:
              cv2.putText(image,'Ustrasana or Camel pose',(10,60),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

        
        if angle1>95 and angle2>175 and angle3>180 and angle4>175 and angle5>190 and angle6>190:
              cv2.putText(image,'Virabhadrasana or Warrior pose',(10,60),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)


    cv2.imshow('squat',image)
    if cv2.waitKey(1) & 0xFF==27:
             break
