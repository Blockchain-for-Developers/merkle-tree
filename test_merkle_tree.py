import unittest
from merkle_tree import *


class TestMerkleTree(unittest.TestCase):

    def test_one_tx(self):
        """Test that the tree can construct the proper block header given
        only one transaction
        """
        tx1 = 'a'

        data = tx1 + tx1
        data = hash_data(data, 'sha256')

        merkle_tree = MerkleTree([tx1])

        self.assertEqual(merkle_tree.block_header, data)
        self.assertEqual(merkle_tree.height, 1)

    def test_two_tx(self):
        """Test that the tree can construct the proper block header given
        only two transactions
        """
        tx1 = 'a'
        tx2 = 'b'

        data = tx1 + tx2
        data = hash_data(data, 'sha256')

        merkle_tree = MerkleTree([tx1, tx2])

        self.assertEqual(merkle_tree.block_header, data)
        self.assertEqual(merkle_tree.height, 1)


    def test_less_tx(self):
        """Test that the tree can construct the proper block header given
        some non-exponent-of-two amount of transactions
        """
        tx1 = 'a'
        tx2 = 'b'
        tx3 = 'c'

        data1 = tx1 + tx2
        data1 = hash_data(data1, 'sha1')
        data2 = tx3 + tx3
        data2 = hash_data(data2, 'sha1')
        data = data1 + data2
        data = hash_data(data, 'sha1')

        merkle_tree = MerkleTree([tx1, tx2, tx3], 'sha1')

        self.assertEqual(merkle_tree.block_header, data)
        self.assertEqual(merkle_tree.height, 2)

    def test_less_tx_again(self):
        """Test that the tree can construct the proper block header given
        a greater non-exponent-of-two amount of transactions
        """
        tx1 = 'a'
        tx2 = 'b'
        tx3 = 'c'
        tx4 = 'd'
        tx5 = 'e'

        data1 = tx1 + tx2
        data1 = hash_data(data1, 'sha256')
        data2 = tx3 + tx4
        data2 = hash_data(data2, 'sha256')
        data3 = data1 + data2
        data3 = hash_data(data3, 'sha256')
        data4 = tx5 + tx5
        data4 = hash_data(data4, 'sha256')
        data5 = tx5 + tx5
        data5 = hash_data(data5, 'sha256')
        data6 = data4 + data5
        data6 = hash_data(data6, 'sha256')
        data = data3 + data6
        data = hash_data(data, 'sha256')

        merkle_tree = MerkleTree([tx1, tx2, tx3, tx4, tx5])

        self.assertEqual(merkle_tree.block_header, data)
        self.assertEqual(merkle_tree.height, 3)

    def test_reset_tree(self):
        """Test that users can wipe the tree successfully"""
        tx1 = 'a'
        tx2 = 'b'

        merkle_tree = MerkleTree([tx1, tx2])
        self.assertEqual(merkle_tree.height, 1)

        merkle_tree.hash_function('sha1')

        merkle_tree.reset_tree()
        self.assertEqual(merkle_tree.height, 0)

    def test_add_tx(self):
        """Test that users can add tx's to the tree successfully. It should
        be reset and reconstructed from the new list
        """
        tx1 = 'a'
        tx2 = 'b'
        tx3 = 'c'
        tx4 = 'd'

        data1 = tx1 + tx2
        data1 = hash_data(data1, 'sha256')
        data2 = tx3 + tx3
        data2 = hash_data(data2, 'sha256')
        data = data1 + data2
        data = hash_data(data, 'sha256')

        merkle_tree = MerkleTree([tx1, tx2])
        merkle_tree.add_tx(tx3)

        self.assertEqual(merkle_tree.block_header, data)

        data2 = tx3 + tx4
        data2 = hash_data(data2, 'sha256')
        data = data1 + data2
        data = hash_data(data, 'sha256')

        merkle_tree = MerkleTree([tx1, tx2])
        merkle_tree.add_tx(tx3, tx4)

        self.assertEqual(merkle_tree.block_header, data)

        merkle_tree = MerkleTree([tx1, tx2])
        merkle_tree.add_tx([tx3, tx4])

        self.assertEqual(merkle_tree.block_header, data)

if __name__ == '__main__':
    unittest.main()
