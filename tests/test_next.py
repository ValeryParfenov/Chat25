import unittest
from app.model import generate_response

class TestNext(unittest.TestCase):
    def test_next_number(self):
        """Тест предсказания следующего числа в последовательности"""
        prompt = "12345678"
        response = generate_response(prompt, max_new_tokens=20)
        self.assertIsInstance(response, str)
        self.assertTrue(len(response) > 0)
        # Проверяем, что в ответе есть число 9
        self.assertIn("9", response)
    
    def test_next_letter(self):
        """Тест предсказания следующей буквы в алфавите"""
        prompt = "1 2 3 4 5 6 7"
        response = generate_response(prompt, max_new_tokens=20)
        self.assertIsInstance(response, str)
        self.assertTrue(len(response) > 0)
        # Проверяем, что в ответе есть буква H
        self.assertIn("8", response)
    
    def test_next_word(self):
        """Тест предсказания следующего слова в последовательности"""
        prompt = "A B C D E"
        response = generate_response(prompt, max_new_tokens=20)
        self.assertIsInstance(response, str)
        self.assertTrue(len(response) > 0)
        # Проверяем, что в ответе есть Thursday
        self.assertIn("F", response)