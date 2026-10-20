import tempfile
import unittest
from pathlib import Path
from log_analyzer import analyze


class AnalyzerTests(unittest.TestCase):
    def test_counts_known_events(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "events.csv"
            path.write_text("EventID\n4624\n4625\n4625\n9999\n", encoding="utf-8")
            counts = analyze(path)
            self.assertEqual(counts["4624"], 1)
            self.assertEqual(counts["4625"], 2)

    def test_missing_header(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "events.csv"
            path.write_text("WrongColumn\n4624\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                analyze(path)


if __name__ == "__main__":
    unittest.main()
