import unittest

def multiply(x,y):
    return x * x

class TestMultiply(unittest.TestCase):

    def test_multiply(self):
        test_x = 5
        test_y = 4
        self.assertEqual(multiply(test_x, test_y), 20, "Should be 20")

# if __name__ == "__main__":
#     unittest.main()


