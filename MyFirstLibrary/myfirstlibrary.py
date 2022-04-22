"""
# MyFirstLibrary for Robot Framework®
This Docstring is for the `README.md` file.

MyFirstLibrary is an example library for Robot Framework.  
It shall demonstrate the steps to publish a library to PyPi.  

Those steps include:

* Setting up the GitHub Repository
* Creating a new Python package and implementing the library
* Managing your dependencies
* Creating and running Unit Tests and Acceptance Tests
* Documenting your library
* Publishing your library to PyPi
* Using Tasks and GitHub Actions to automate your work

---
## Installation
If you already have Python >= 3.8 with pip installed, you can simply run:  
`pip install --upgrade robotframework-myfirstlibrary`

---
## Getting started
Some examples how to import and use the library.

``` robotframework
*** Settings ***
Library            MyFirstLibrary

*** Variables ***
${TESTDATA}    ${CURDIR}/testdata

*** Test Cases ***
Image Should Contain Face
    Should Contain A Face    ${TESTDATA}/faces.png

Image Should Not Contain A Face
    Should Not Contain A Face    ${TESTDATA}/no_faces.jpg
```

"""

import cv2
import os

class MyFirstLibrary:
    """
    This is a DocString for the Keyword Documentation.  
    It can explain some general things, like what the Library does and how it works.  

    Also the options to import the Library can be explained here with examples.

    """
    def __init__(self) -> None:
        cascade_path = os.path.join(os.path.dirname(__file__), 'haarcascade_frontalface_default.xml')
        self.face_cascade = cv2.CascadeClassifier(cascade_path)

    def is_face_in_image(self, img: str):
        """Returns ``True`` if a face is detected in the image ``img``, ``False`` otherwise.  

        ``img``: The path to the image

        Example:

        | Should Contain A Face | faces.png |
        | Should Contain A Face | ${CURDIR}/another_face.jpg |
        """
        
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
            
    def should_contain_a_face(self,img: str):
        """Fails if a face is not detected in the image ``img``. 

        ``img``: The path to the image

        Example:

        | Should Contain A Face | faces.png |
        | Should Contain A Face | ${CURDIR}/another_face.jpg |
        """
        if self.is_face_in_image(img) != True:
            raise AssertionError('Image should contain a face. But no face was detected')

    def should_not_contain_a_face(self,img: str):
        """Fails if a face is detected in the image ``img``.

        ``img``: The path to the image
            
        Example:

        | Should Not Contain A Face | no_faces.png |
        | Should Not Contain A Face | ${CURDIR}/also_no_face.jpg |
        """
        if self.is_face_in_image(img) == True:
            raise AssertionError('Image should NOT contain a face. But it contains a face')



    