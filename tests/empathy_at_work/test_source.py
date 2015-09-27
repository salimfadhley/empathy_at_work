import unittest
from empathy_at_work.source.fetcher import fetcher


class TestFetcher(unittest.TestCase):

    def test_fetcher(self):
        fet = fetcher()
        for row in fet:
            print(row)

if __name__ == '__main__':
    unittest.main()