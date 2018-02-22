import time
from finder import Finder
from unittest import TestCase
import string
import random

# Test class which create the test data before each test for testing the finder class and also print the time taken.
# @author Saurabh Singh
# @version 1.0
class FinderTests(TestCase):

    # Create the stringlist array with 10000 elements using random string where each string contains 10 characters.
    # The method also note the start time.
    # The method also hold the first element of the array for success case comparision.
    def setUp(self):
        per_str_chars = 10
        array_size = 10000
        string_list = [''.join(random.choice(string.ascii_lowercase) for _ in range(per_str_chars)) for _ in range(array_size)]
        self.first_array_str = string_list[0]
        self.finder = Finder(string_list)
        self.start_time = time.time()

    # The method test the success scenario by using reverse string in the
    # find method and then checking the first string of the array.
    def test_success(self):
        time.sleep(1)
        first_array_reverse_str = self.first_array_str[::-1]
        self.assertEqual([self.first_array_str], self.finder.find(first_array_reverse_str))

    # Checking the invalid string scenario, in this case method should return None.
    def test_failure(self):
        time.sleep(2)
        self.assertEqual(None, self.finder.find('Invalid'))

    # Log the time taken by each tests.
    def tearDown(self):
        t = time.time() - self.start_time
        print("%s: %.3f" % (self.id(), t))