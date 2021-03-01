from linkedList import ListNode, LinkedList

# implement a function to check if a linked list is a palindrome

def palindrome1(head: ListNode):
	vals = []
	node = head
	while node is not None:
		vals.append(node.val)
		node = node.next
	return vals == vals[::-1]

def palindrome2(head: ListNode):
	slow = head
	fast = head
	while (slow is not None and fast is not None):
		slow = slow.next
		fast = fast.next.next
	
	first_half_end = slow
	second_half_start = reverse(first_half_end.next)

	result = True
	first = head
	second = second_half_start
	while result and second is not None:
		if first.val != second.val:
			result = False
		first = first.next
		second = second.next

	return result

def reverse(head: ListNode):
	pre = None
	cur = head
	while cur is not None:
		next_node = cur.next
		cur.next = pre
		pre = cur
		cur = next_node
	return pre

