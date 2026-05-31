import subprocess
import unittest

class TestMain(unittest.TestCase):
    def test_output(self):
        result = subprocess.run(['python3', 'main.py'], capture_output=True, text=True)
        self.assertEqual(result.stdout.strip(), "Criello")

if __name__ == '__main__':
    unittest.main()
