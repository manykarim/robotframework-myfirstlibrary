
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

