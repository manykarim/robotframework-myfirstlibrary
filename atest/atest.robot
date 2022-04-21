*** Settings ***
Library    ${CURDIR}/../MyFirstLibrary

*** Variables ***
${TESTDATA}    ${CURDIR}/testdata

*** Test Cases ***
Image Should Contain Face
    Should Contain A Face    ${TESTDATA}/faces.png

Image Should Not Contain A Face
    Should Not Contain A Face    ${TESTDATA}/no_faces.jpg





