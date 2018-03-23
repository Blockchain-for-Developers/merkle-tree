
class Node:
	"""Node wrapper class implementation. 
	Useful for tracking depth of a node when
	constructing the merkle proof"""
	def __init__(self, direction, tx):
		self._direction = direction
		self._tx = tx

	def __eq__(self, other):
		"""Overrides the default implementation"""
		if isinstance(self, other.__class__):
			return self.__dict__ == other.__dict__
		return False

	def __cmp__(self, other):
		"""Overrides the default implementation"""
		if isinstance(self, other.__class__):
			return self.__dict__ == other.__dict__
		return False
	

	@property
	def direction(self):
		"""int: Allow user to query node for its depth"""
		return self._direction

	@property
	def tx(self):
		"""string: Allow user to query node for its tx string"""
		return self._tx
