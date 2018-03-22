import unittest
from merkle_tree import *


class SanityCheck(unittest.TestCase):

    def test_sanity_HashLeaf(self):
        """Ensure HashLeaf structures work as intended"""
        tx1 = 'a'
        tx2 = 'b'

        data = tx1 + tx2
        data = hash_data(data, 'sha256')

        hash_leaf = HashLeaf(tx1, tx2, 'sha256')

        self.assertEqual(hash_leaf.data, data)
        self.assertEqual(hash_leaf.height, 1)

    def test_sanity_HashNode(self):
        """Ensure HashNode structures work as intended"""
        tx1 = 'a'
        tx2 = 'b'
        tx3 = 'c'
        tx4 = 'd'

        data1 = tx1 + tx2
        data1 = hash_data(data1, 'sha256')
        data2 = tx3 + tx4
        data2 = hash_data(data2, 'sha256')
        data = data1 + data2
        data = hash_data(data, 'sha256')

        hash_leaf1 = HashLeaf(tx1, tx2, 'sha256')
        hash_leaf2 = HashLeaf(tx3, tx4, 'sha256')
        hash_node = HashNode(hash_leaf1, hash_leaf2, 'sha256')

        self.assertEqual(hash_node.data, data)
        self.assertEqual(hash_node.height, 2)

    def test_sanity_check_MerkleTree(self):
        """Ensure MerkleTree structures work as intended"""
        tx1 = 'a'
        tx2 = 'b'
        tx3 = 'c'
        tx4 = 'd'

        data1 = tx1 + tx2
        data1 = hash_data(data1, 'sha256')
        data2 = tx3 + tx4
        data2 = hash_data(data2, 'sha256')
        data = data1 + data2
        data = hash_data(data, 'sha256')

        merkle_tree = MerkleTree([tx1, tx2, tx3, tx4])

        self.assertEqual(merkle_tree.block_header, data)

if __name__ == '__main__':
    unittest.main()
