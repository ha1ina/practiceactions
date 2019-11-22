import unittest
import app

class TestAction(unittest.TestCase):
    def test_assert(self):
        assert app.return3() == 3
if __name__=='__main__':
    unittest.main()
