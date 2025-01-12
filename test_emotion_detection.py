#Import the 'unittest' module to create unit tests for your code
import unittest

# Import 'emotion_detector' from emotion_detection
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):
        result_1 = emotion_detector("I am glad this happened") # test statement to give dominant emotion 'joy'
        self.assertEqual(result_1, "joy")

        result_2 = emotion_detector("I am really mad about this") # test statement to give dominant emotion 'anger'
        self.assertEqual(result_2, "anger")

        result_3 = emotion_detector("I feel disgusted just hearing about this") # test statement to give dominant emotion 'disgust'
        self.assertEqual(result_3, "disgust")
        
        result_4 = emotion_detector("I am so sad about this") # test statement to give dominant emotion 'sadness'
        self.assertEqual(result_4, "sadness")
      
        result_5 = emotion_detector("I am really afraid that this will happen") # test statement to give dominant emotion 'fear'
        self.assertEqual(result_5, "fear")

unittest.main()