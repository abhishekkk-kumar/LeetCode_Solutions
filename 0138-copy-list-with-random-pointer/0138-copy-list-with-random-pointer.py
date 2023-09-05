"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:return None
        
        # Create a mapping of original nodes to their corresponding copied nodes
        node_map = {}
        
        # First pass: Create copies of nodes without setting next or random pointers
        current = head
        while current:
            node_map[current] = Node(current.val)
            current = current.next
        
        # Second pass: Set the next and random pointers of copied nodes
        current = head
        while current:
            copy_node = node_map[current]
            if current.next:copy_node.next = node_map[current.next]
            if current.random:copy_node.random = node_map[current.random]
            current = current.next
        
        return node_map[head]
        