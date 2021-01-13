# write method to remove duplicates from unsorted linked list
from linkedList import ListNode, LinkedList
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

list1 = LinkedList()
list1.insertByArray([3, 4, 5, 6, 1, 7, 3, 2, 6, 9, 1, 1])

print(removeDups(list1.head).printAll())
