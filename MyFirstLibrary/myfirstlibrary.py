# region: docstring
"""
# MyFirstLibrary for Robot Framework®
"""
# endregion

import cv2
import os

class MyFirstLibrary:
    def __init__(self) -> None:
        # Load the cascade
        # Combine path of current folder and the cascade file
        cascade_path = os.path.join(os.path.dirname(__file__), 'haarcascade_frontalface_default.xml')
        self.face_cascade = cv2.CascadeClassifier(cascade_path)

    def is_face_in_image(self, img):
        '''
        This function should return True if the image contains a face, and False otherwise.
        '''
        
        # Read the input image
        img = cv2.imread(img)
        # Convert into grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Detect faces
        faces = self.face_cascade.detectMultiScale(gray, 1.1, 4)
        if len(faces)>0:
            return True
        else:
            return False
            
    def should_contain_a_face(self,img):
        if self.is_face_in_image(img) != True:
            raise AssertionError('Image should contain a face. But no face was detected')

    def should_not_contain_a_face(self,img):
        if self.is_face_in_image(img) == True:
            raise AssertionError('Image should NOT contain a face. But it contains a face')



    