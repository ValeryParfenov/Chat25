import unittest
from time import time

from app.model import generate_response
from time import time


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


class Benchmark(unittest.TestCase):
    def test_time(self):
        prompt = "Hello, how are you?"
        n = 10
        avg_duration = 0.0
        for _ in range(n):
            start = time()
            generate_response(prompt)
            end = time()
            avg_duration += end - start
        avg_duration /= n
        self.assertTrue(avg_duration < 10.0)

    def test_time_per_token(self):
        prompt = "Hello, how are you?"
        n = 10
        avg_duration_per_word = 0.0
        for _ in range(n):
            start = time()
            response = generate_response(prompt)
            end = time()
            avg_duration_per_word += (end - start) / len(response.split(' '))
        avg_duration_per_word /= n
        print(avg_duration_per_word)
        self.assertTrue(avg_duration_per_word < 0.5)
