import unittest

from app.model import generate_response


class TestModel(unittest.TestCase):
    def test_returns_string(self):
        response = generate_response("Hello, how are you?")
        self.assertIsInstance(response, str)
        self.assertTrue(len(response) > 0)

    def test_prompt_in_response(self):
        prompt = "The sky is blue"
        response = generate_response(prompt)
        self.assertIsInstance(response, str)
        self.assertIn("The", response[:100])
