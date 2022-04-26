*** Settings ***
Library    MyFirstLibrary

*** Variables ***
${TESTDATA}    ${CURDIR}/testdata
${image_with_face}    ${TESTDATA}/faces.png
${image_without_face}    ${TESTDATA}/no_faces.jpg
${no_face_detected_error}    Image should contain a face. But no face was detected
${face_detected_error}    Image should NOT contain a face. But it contains a face

*** Test Cases ***
Image Should Contain Face
    Should Contain A Face    ${image_with_face}

Image Should Not Contain A Face
    Should Not Contain A Face    ${image_without_face}

Check Exceptions
    Run Keyword And Expect Error    
    ...    ${no_face_detected_error}    
    ...    Should Contain A Face    ${image_without_face}
    Run Keyword And Expect Error
    ...    ${face_detected_error}    
    ...    Should Not Contain A Face    ${image_with_face}
    





