# write method to remove duplicates from unsorted linked list

class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class LinkedList:
	def __init__(self, head=None):
		self.head = head

	def insert(self, data):
		node = ListNode(data, self.head)
		self.head = node

	def insertByArray(self, arr: []):
		for val in arr:
			self.insert(val)

def removeDups(head: ListNode):
	table = {}
	pre, node = head, head
	while(node):
		if (node.val in table):
			pre.next = node.next
			node = node.next
		else:
			table[node.val] = 1
			pre = node
			node = node.next
	return head

def linkedListToArray(head: ListNode):
	arr = []
	while(head):
		arr.append(head.val)
		head = head.next
	return arr

list1 = LinkedList()
list1.insertByArray([3, 4, 5, 6, 1, 7, 3, 2, 6, 9, 1, 1])

print(linkedListToArray(removeDups(list1.head)))





