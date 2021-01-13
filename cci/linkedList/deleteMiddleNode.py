from linkedList import ListNode, LinkedList

# write a method delete any node but first and last node. nothing returned. 
def deleteMiddleNode(node: ListNode):
	node.val = node.next.val
	node.next = node.next.next

list1 = LinkedList()
list1.insertByArray([3, 4, 5, 6, 1, 7])
node = list1.head
i = 3
while i > 0:
	node = node.next
	i -= 1

deleteMiddleNode(node)  # node.val = 6
print(list1.toString())
