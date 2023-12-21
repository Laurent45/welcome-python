import unittest
import subprocess
from textwrap import dedent

class Test00(unittest.TestCase):

    def test(self):
        """
        In the file ../ex00/Hello.py, you need to add some code below
        #your code here in order to pass the test. The purpose here is to
        discover some data type in python and see an insight of mutable object
        and immutable object
        """

        outputExpected = dedent("""
        ['Hello', 'World!']$
        ('Hello', 'France!')$
        {'Hello', 'Paris!'}$
        {'Hello': '42Paris!'}$
        """).lstrip()
        
        process = subprocess.run("python3 ../ex00/Hello.py | cat -e", shell=True, capture_output=True, encoding="UTF-8")

        self.assertEqual(outputExpected, process.stdout, "It must looks like outputExpected")

if __name__ == "__main__":
    unittest.main()
