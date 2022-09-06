import unittest
from unittest.mock import patch
import io
from main import *

class Test(unittest.TestCase):
    def test_add(self):
        with patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            process('add 4 8')
            self.assertEqual(mock_stdout.getvalue(), '12\n')

    def test_sample1(self):
        with patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            run('samples/sample1.txt')
            self.assertEqual(
                    mock_stdout.getvalue(), 
                    "\n".join(['24', '30', '1','0', '']))

    def test_sample2(self):
        with patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            run('samples/sample2.txt')
            self.assertEqual(
                    mock_stdout.getvalue(), 
                    "\n".join(['0', '', '0', '55', '1', '1', '0', '1', '0', '0',
                        '3582', '1', '-90', '26', '176160768', '0', '1', '69',
                        '0', '10240', '', '1', '']))

    def test_sample3(self):
        with patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            run('samples/sample3.txt')
            self.assertEqual(
                    mock_stdout.getvalue(), 
                    "\n".join(['0', '24', '36', '222', '1', '32', '1', '0', '1',
                        '1', '215', '-70', '0', '53', '1', '1', '0', '1288',
                        '1', '19516331393024', '0', '292057776128', '1', '0',
                        '109', '17', '0', '']))



if __name__ == '__main__':
    unittest.main()
