from pathlib import Path
from MyFirstLibrary import MyFirstLibrary
import pytest

testdata_directory = Path(__file__).parent.resolve() / "testdata"
face_detector = MyFirstLibrary()
image_with_face = str(testdata_directory /'faces.png')
image_without_face = str(testdata_directory /'no_faces.jpg')

def test_image_should_contain_a_face():
    assert face_detector.is_face_in_image(image_with_face) == True
    face_detector.should_contain_a_face(image_with_face)

def test_image_should_not_contain_a_face():
    assert face_detector.is_face_in_image(image_without_face) == False
    face_detector.should_not_contain_a_face(image_without_face)

def test_assertion_error_should_be_raised():
    with pytest.raises(AssertionError):
        face_detector.should_contain_a_face(image_without_face)
    with pytest.raises(AssertionError):
        face_detector.should_not_contain_a_face(image_with_face)