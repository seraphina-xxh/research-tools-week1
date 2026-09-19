"""text_stats 的简单回归测试。"""

from pathlib import Path
import unittest

from text_stats import count_words


class CountWordsTest(unittest.TestCase):
    def test_hello_appears_five_times_in_sample(self) -> None:
        sample_file = Path(__file__).resolve().parent.parent / "sample.txt"
        counts = dict(count_words(str(sample_file)))
        self.assertEqual(counts["hello"], 5)


if __name__ == "__main__":
    unittest.main()
