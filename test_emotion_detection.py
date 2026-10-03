from EmotionDetection import emotion_detector
import unittest


class TestEmotionDetector(unittest.TestCase):
    def test_sentiment_analyzer(self):
        tests = [
            ("I am glad this happended", "joy"),
            ("I am really mad about this", "anger"),
            ("I feel disgusted just hearing about this", "disgust"),
            ("I am so sad about this", "sadness"),
            ("I am really afraid that this will happen", "fear"),
        ]
        for test in tests:
            result = emotion_detector(test[0])
            self.assertEqual(result["dominant_emotion"], test[1])

unittest.main()