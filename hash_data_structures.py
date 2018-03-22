from utils import *


SECURE_HASH_FUNCTIONS = ['sha1', 'sha224', 'sha256', 'sha384', 'sha512']

class HashLeaf(object):
    """Attach two pieces of string data and store the hash of the concatenated
    strings
    """
    def __init__(self, left, right, hash_function):
        assert isinstance(hash_function, str), (
            "Hash function is not of type `String`")
        self._hash_function = hash_function
        self._left = left
        self._right = right
        self._data = self._evaluate()
        self._height = 1
        
    def _evaluate(self):
        """Ensure data is in the form of a string"""
        assert isinstance(self._left, str), "Data is not of type `String`"
        assert isinstance(self._right, str), "Data is not of type `String`"
        return hash_data(self._left + self._right, self._hash_function)

    @property
    def data(self):
        """str: Allow the user to query the hashed data stored in the
        HashLeaf
        """
        return self._data

    @property
    def height(self):
        """int: Allow the user to query the height stored in the HashLeaf"""
        return self._height

class HashNode(HashLeaf):
    """Attach two HashLeaf structures and store the hash of their concatenated
    data
    """
    def __init__(self, left, right, hash_function):
        super().__init__(left, right, hash_function)
        assert left._hash_function == hash_function, (
            "Hash functions incompatible")
        assert right._hash_function == hash_function, (
            "Hash functions incompatible")
        self._height = self._left.height + 1

    def _evaluate(self):
        """Ensure data is in the form of a HashLeaf data structures and has
        the correct height. Separate method from `HashLeaf` as there are
        different requirements
        """
        assert isinstance(self._left, HashLeaf), (
            "Data is not of type `HashLeaf`")
        assert isinstance(self._right, HashLeaf), (
            "Data is not of type `HashLeaf`")
        assert self._left.height == self._right.height, (
            "Left and right branch not balanced")
        return hash_data(self._left.data + self._right.data,
            self._hash_function)
