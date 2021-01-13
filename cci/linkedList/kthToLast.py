from linkedList import ListNode, LinkedList

# find kth to last element of a singly linked list 

def kthToLast(head: ListNode, k: int):
	p1 = head
	p2 = head

	# p1 move forward by k steps, then p1 has n-k steps left to the end of linked list
	while (k > 0):
		if (p1 == None):
			return None
		p1 = p1.next
		k -= 1

	# p2 move n-k step with p1, so p2 stops at kth to last element
	while (p1):
		p1 = p1.next
		p2 = p2.next
	return p2

list1 = LinkedList()
list1.insertByArray([3, 4, 5, 6, 1, 7, 3, 2, 6, 9, 1, 1])

print(kthToLast(list1.head, 3).val) #9
print(kthToLast(list1.head, 5).val) #2
