import cv2,os,urllib.request
import numpy as np
from django.conf import settings
from avatar.mod import model
from keras.preprocessing import image
from . import views

label_dict = {0 : 'Angry', 1 : 'Disgust', 2 : 'Fear', 3 : 'Happy', 4 : 'Sad', 5 : 'Surprise', 6 : 'Neutral'}

model.load_weights(os.path.join(settings.BASE_DIR, 'cnn_model_files/emotion_weights_3.hdf5'))

face_haar_cascade = cv2.CascadeClassifier(os.path.join(settings.BASE_DIR,'cnn_model_files/haarcascade_frontalface_default.xml'))


class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, img = self.video.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = face_haar_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:

            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_gray = cv2.resize(roi_gray, (48, 48))
            img_pixels = image.img_to_array(roi_gray)
            img_pixels = np.expand_dims(img_pixels, axis=0)

            predictions = model.predict(img_pixels)
            emotion_label = np.argmax(predictions)
            emotion_prediction = label_dict[emotion_label]
            views.epred(emotion_prediction)
            cv2.putText(img, emotion_prediction, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 1)
        ret, jpeg = cv2.imencode('.jpg', img)
        return jpeg.tobytes()