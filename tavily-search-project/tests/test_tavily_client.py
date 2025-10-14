import unittest
from src.tavily_client import TavilyClient

class TestTavilyClient(unittest.TestCase):
    def setUp(self):
        self.client = TavilyClient(api_key='test_api_key')

    def test_search(self):
        term = "example search term"
        self.client.search(term)
        results = self.client.get_results()
        self.assertIsInstance(results, list)

    def test_get_results_empty(self):
        self.client.search("nonexistent term")
        results = self.client.get_results()
        self.assertEqual(results, [])

if __name__ == '__main__':
    unittest.main()