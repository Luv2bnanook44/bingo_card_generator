import unittest

class TestFlaskApp(unittest.TestCase):

    def test_index(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_generate_cards(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_confirmation(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()