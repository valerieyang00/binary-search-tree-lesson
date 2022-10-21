class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        
    def __str__(self):
        return f"{self.data}"

# root = Node(15)
# root.left = Node(10)
# root.right = Node(16)
# print(f"root: {root}, right: {root.right}, left: {root.left}")

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        '''
            Insert(data: any) -> None:\n 
            creates a new Node from the data passed in and adds it to the tree
            If the data is already in the tree, does not insert it again
        '''
        new_node = Node(data)
        # if this is the first node, create a root node
        if not self.root:
            self.root = new_node
            return
        
        # loop over the tree starting at the root
        # keep track of the current node
        current_node = self.root
        while current_node:
            # if the new data is smaller than the current node
            if new_node.data < current_node.data:
                # if there is no left: that is the place it goes
                if not current_node.left:
                    current_node.left = new_node
                    return
                # if there IS a left: keep iterating
                else:
                    current_node = current_node.left
            # if the new data is greater than the current node
            elif new_node.data > current_node.data:
                # if there is no right:
                if not current_node.right:
                    current_node.right = new_node
                    return
                else:
                    current_node = current_node.right
            # if the new data is duplicate of the current node
            else:
                # stop iterating
                return
    
    def dfs(self, val):
        '''
            dfs(val: any) -> value or bool:\n 
            Performs depth first search
            Search the Tree for a node with the given value
            If the node exists, return it
            If the node doesn't exist, return false
        '''
        # if there is no root return early
        if not self.root:
            return False
        
        #  loop through the tree iteratively
        current_node = self.root
        while current_node:
            # if the value we are searching for is smaller than current node
            if val < current_node.data:
                current_node = current_node.left
            # if the value we are searching for is Greater than current node
            elif val > current_node.data:
                current_node = current_node.right
            # if the value is neither = it's a match to return!
            else:
                return current_node
        
        # made through the whole loop but didn't find anything = return false
        return False


    def bfs(self, val):
        '''
            bfs(val: any) -> value or bool:\n
            Performs breadth first search
            Search the Tree for a node with the given value
            If the node exists, return it
            If the node doesn't exist, return false
        '''
        # if no root
        if not self.root:
            return False
        
        # need a queue to keep track of each level
        queue = [self.root]

        while len(queue) > 0:
            # examine node at start of queue (and remove if not it)
            current_node = queue.pop(0) #remove index 0 (python specific)
            # if it contains the data we want -- we will return that node
            if current_node.data == val:
                return current_node
            # take the children of node we dequeued and enqueue them to test next lvl
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        
        # went through all queue and Not found, return false
        return False
    # print out all the nodes
    def print(self, node=None):
        '''
            print() -> None:\n
            prints out all values recursively (in a depth first search fashion)
            default start is at root node
        '''
        # if this is the first invocation
        if not node:
            node = self.root        
        print(node)

        # if this node has left/right, we will recursively print
        if node.left:
            self.print(node.left)
        if node.right:
            self.print(node.right)

my_tree = BinaryTree()

my_tree.insert(15)
my_tree.insert(10)
my_tree.insert(16)
my_tree.insert(19)
my_tree.insert(22)
my_tree.insert(17)
my_tree.insert(6)
my_tree.insert(9)
my_tree.insert(2)

my_tree.print()

print(f"should be 9: {my_tree.dfs(9)}, should be 17: {my_tree.bfs(17)}")