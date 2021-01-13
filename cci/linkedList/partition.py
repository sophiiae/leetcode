from linkedList import ListNode, LinkedList

# partition a linked list around a value x, such that all nodes less than x com before all nodes greater than or equal to x. if x is contained within the list, tha values of x only need to be after the lements less than x. 

# note: the partiton element x can appear anywhere in the "right partition"

# input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5]
# output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

def partition(head: ListNode, x: int):
	left = head if head.val < x else None
	right = head if head.val >= x else None
	pre = head
	node = head.next

	while (node):
		if node.val >= x:
			if not right:
				right = node
			node = node.next
			pre = pre.next
		else:
			left.next = node
			pre.next = node.next
			node.next = right
			node = pre.next
			left = left.next
	return head

list1 = LinkedList()
list1.insertByArray([3, 5, 8, 5, 10, 2, 1, 6, 4])

print(partition(list1.head, 5).printAll())
