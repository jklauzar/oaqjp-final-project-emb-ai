# Task 5a
import pytest
from EmotionDetection import emotion_detector
def test_joy():
    assert emotion_detector("I am glad this happened")["dominant_emotion"] == "joy"
def test_anger():
    assert emotion_detector("I am really mad about this")["dominant_emotion"] == "anger"
def test_disgust():
    assert emotion_detector("I feel disgusted just hearing about this")["dominant_emotion"] == "disgust"
def test_sadness():
    assert emotion_detector("I am so sad about this")["dominant_emotion"] == "sadness"
def test_fear():
    assert emotion_detector("I am really afraid that this will happen")["dominant_emotion"] == "fear"
