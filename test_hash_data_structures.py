import unittest
from hash_data_structures import *


class TestHashDataStructures(unittest.TestCase):

    def test_incompatible_hash_functions(self):
        """Ensure that the hash function used across the tree
        is the same
        """
        tx1 = 'a'
        tx2 = 'b'
        tx3 = 'c'
        tx4 = 'd'

        hash_leaf1 = HashLeaf(tx1, tx2, 'sha1')
        hash_leaf2 = HashLeaf(tx3, tx4, 'sha224')

        self.assertRaises(AssertionError, HashNode, hash_leaf1, hash_leaf2,
            'sha256')

if __name__ == '__main__':
    unittest.main()
