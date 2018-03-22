from utils import *
import math
from node import Node


def merkle_proof(tx, merkle_tree):
    """Given a tx and a Merkle tree object, retrieve its list of tx's and
    parse through it to arrive at the minimum amount of information required
    to arrive at the correct block header. This does not include the tx
    itself.

    Return this data as a list; remember that order matters!
    """
    #### YOUR CODE HERE


def get_max_depth_node(nodes):
    """Helper function to retrieve the node with the maximum depth.
    Helpful for pairing nodes for hashing in verify_proof"""
    curr = nodes[0]
    for i in range(0, len(nodes)):
        if nodes[i].depth > curr.depth:
            curr = nodes[i]
    return curr


def verify_proof(tx, merkle_proof):
    """Given a Merkle proof - constructed via `merkle_proof(...)` - verify
    that the correct block header can be retrieved by properly hashing the tx
    along with every other piece of data in the proof in the correct order
    """
    #### YOUR CODE HERE


    
