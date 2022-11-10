# A Linked List Node
class Node:
	def __init__(self, data, next=None):
		self.data = data
		self.next = next


# Utility function to print contents of a linked list
def printList(node):

	while node:
		print(node.data, end=' —> ')
		node = node.next
	print('None')


# Takes two lists sorted in increasing order and merges their nodes
# to make one big sorted list returned
def sortedMerge(a, b):

	# base cases
	if a is None:
		return b
	elif b is None:
		return a

	# pick either `a` or `b`, and recur
	if a.data <= b.data:
		result = a
		result.next = sortedMerge(a.next, b)
	else:
		result = b
		result.next = sortedMerge(a, b.next)

	return result


# The main function to merge given `k` sorted linked lists.
# It takes a list of lists `lists[0…k)` and generates the sorted output
def mergeKLists(lists):

	# base case
	if not lists:
		return None

	last = len(lists) - 1

	# repeat until only one list is left
	while last:
		(i, j) = (0, last)

		# `(i, j)` forms a pair
		while i < j:
			# merge list `j` with `i`
			lists[i] = sortedMerge(lists[i], lists[j])

			# consider the next pair
			i = i + 1
			j = j - 1

			# if all pairs are merged, update last
			if i >= j:
				last = j

	return lists[0]


if __name__ == '__main__':

	k = 3	# total number of linked lists

	# a list to store the head nodes of the linked lists
	lists = [Node] * k

	lists[0] = Node(1)
	lists[0].next = Node(4)
	lists[0].next.next = Node(5)

	lists[1] = Node(1)
	lists[1].next = Node(3)
	lists[1].next.next = Node(4)
	# lists[1].next.next.next = Node(9)

	lists[2] = Node(2)
	lists[2].next = Node(6)
	# lists[2].next.next = Node(10)

	# Merge all lists into one
	head = mergeKLists(lists)
	printList(head)
