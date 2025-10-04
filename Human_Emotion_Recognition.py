import streamlit as st
import numpy as np
import cv2
from deepface import DeepFace 
from PIL import Image
import tempfile


st.title("Human Emotion Recognition")

options=st.selectbox("Choose an Option",("image","video"))

def Analyze_Emotion(image_or_video):
    try:
        analysis=DeepFace.analyze(image_or_video,actions=['emotion'],enforce_detection=True)
        return analysis[0]['emotion']
    except ValueError as e:
        return None

if options=='image':
    upload=st.file_uploader('please upload an image', type=['png','jpg','jpeg'])
    if upload is not None:
        image=Image.open(upload)
        image_array=np.array(image)
        st.image(image_array,use_container_width=True,channels='RGP')
        
        emotion_score=Analyze_Emotion(image_array)
        if emotion_score:
            detected_emotion=max(emotion_score,key=emotion_score.get)
            st.header(f"detected Emotion :{detected_emotion}") 

        else:
            st.write("no face detected")

if options=='video':
    upload=st.file_uploader('please upload a video...', type=['mp4','mov','avi'])
    if upload is not None:
        with tempfile.NamedTemporaryFile(delete=False) as temp_video:
            temp_video.write(upload.read())
            video_name=temp_video.name
        video=cv2.VideoCapture(video_name)

        frame_rate=90
        frame_count=0
        while video.isOpened():
            ret,frame=video.read()
            if not ret:
                break
            frame_count+=1
            if frame_count%frame_rate==0:
                frame_rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                emotion_score=Analyze_Emotion(frame_rgb)
                if emotion_score:
                    detected_emotion=max(emotion_score,key=emotion_score.get) 
                    cv2.putText(frame,detected_emotion,(100,60),cv2.FONT_HERSHEY_SIMPLEX,3,(200,20,150),2)
                else:
                    detected_emotion="no face detected"
                    cv2.putText(frame,detected_emotion,(60,60),cv2.FONT_HERSHEY_SIMPLEX,3,(230,20,160),2)
                st.image(frame,channels='BGR')
        video.release()
