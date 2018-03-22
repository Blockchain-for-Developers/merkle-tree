from hash_data_structures import *


class MerkleTree(object):
    """Merkle Tree implementation, default hash function is 'sha256'.
    Nodes are reconstructed upon every tx addition but the list of tx
    persistent
    """
    def __init__(self, tx_list, hash_function='sha256'):
        hash_function = hash_function.lower()
        assert tx_list, "No transactions to be hashed"
        assert hash_function in SECURE_HASH_FUNCTIONS, (
            "{} is not a valid hash function".format(hash_function))
        self._hash_function = hash_function
        self._leaves = tx_list
        self._nodes = []
        self._root = self._evaluate()
        self._height = self._root.height
        self._block_header = self._root.data

    def add_tx(self, *tx):
        """Add an arbitrary amount of tx's to the tree. It needs to be
        reconstructed every time this happens and the block header
        changes as well
        """
        tx_in = list(tx)
        if type(tx_in[0]) == list:
            tx_in = tx_in[0]
        self._leaves += tx_in
        self._reevaluate()

    def reset_tree(self, hash_function='sha256'):
        """Clear the tree data"""
        self._hash_function = hash_function
        self._nodes = []
        self._height = 0
        self._block_header = None

    def _evaluate(self):
        """Used to construct the tree and arrive at the block header"""
        leaves = list(self._leaves)
        if not is_power_of_two(len(leaves)) or len(leaves) < 2:
            last_tx = leaves[-1]
            while not is_power_of_two(len(leaves)) or len(leaves) < 2:
                leaves.append(last_tx)
        for tx in range(0, len(leaves), 2):
            self._nodes.append(HashLeaf(leaves[tx], leaves[tx+1],
                self._hash_function))
        nodes = list(self._nodes)
        while len(nodes) > 2:
            left = nodes.pop(0)
            right = nodes.pop(0)
            node = HashNode(left, right, self._hash_function)
            nodes.append(node)
        if len(nodes) == 1:
            return nodes[0]
        return HashNode(nodes[0], nodes[1], self._hash_function)

    def _reevaluate(self):
        """Resets the tree and makes a call to `_evaluate(...)` to reconstruct
        the tree given its persistent list of tx's
        """
        self.reset_tree(self._hash_function)
        self._root = self._evaluate()
        self._height = self._root.height
        self._block_header = self._root.data

    @property
    def hash_function(self):
        """func: Allow the user to query the tree's hash function"""
        return self._hash_function

    # @hash_function.setter
    def hash_function(self, value):
        """Allows the user to change the tree's hash function. Requires that
        the tree be rebuilt to accomodate this change
        """
        value = value.lower()
        assert value in SECURE_HASH_FUNCTIONS, (
            "{} is not a valid hash function".format(value))
        self._hash_function = value

    @property
    def block_header(self):
        """str: Allow the user to query the tree's block header"""
        return self._block_header

    @property
    def height(self):
        """int: Allow the user to query the tree's height"""
        return self._height

    @property
    def leaves(self):
        """list: Allow the user to query the tree's list of tx's"""
        return self._leaves
