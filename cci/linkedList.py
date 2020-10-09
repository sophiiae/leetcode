class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class LinkedList:
	def __init__(self, head=None):
		self.head = head
		self.last = head

	def insert(self, data):
		if (not self.head):
			node = ListNode(data, self.head)
			self.head = node
			self.last = node
		else:
			node = ListNode(data)
			self.last.next = node
			self.last = node

	def insertByArray(self, arr: []):
		for val in arr:
			self.insert(val)

	def toString(self):
		s = ''
		node = self.head
		while (node and node.next):
			s = s + str(node.val) + ', '
			node = node.next
		s += str(node.val)
		return s