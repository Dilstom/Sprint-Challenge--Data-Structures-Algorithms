class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
      # Recursive implementation
      # call the cb on th current node
    cb(self.value)
      #check if this node has a left child
    if self.left:
      #call dfs on the left child
        self.left.depth_first_for_each(cb)
      #check if this node has a right child 
    if self.right:
      # call dfs on the right child
        self.right.depth_first_for_each(cb) 
      
    # *** V2 *** iterative implementation
    def depth_first_for_each(self, cb):
        # initialize a list to be our stack
        stack = []
        # add the root node to the dtack
        stack.append(self)
        # loop as long as we have elements in the stack
        while len(stack):
            # pop off the stack
            current_node = stack.pop()
            # check if the popped-off node has a right child
            if current_node.right:
            # add the right child to the stack
                stack.append(current_node.right)
            # check if the popped-off node has a left child
            if current_node.left:
            # add the left child to the stack
                stack.append(current_node.right)
            #invoke the cb on the popped-off node
            cb(current_node.value)

    # solution - the most expensive because of array (shift all values)
    def breadth_first_for_each(self, cb):
    # initialize a list to be our queue
    queue = []
    # add the root node to the queue
    queue.append(self)
    # loop as long as we have elements in the queue
    while len(queue):
        # pop off the queue
        current_node = queue.pop(0)
        # check if the popped-off node has a left child
        if current_node.left:
        # add the left child to the queue
            queue.append(current_node.left)
        # check if the popped-off node has a right child
        if current_node.right:
        # add the right child to the queue
            queue.append(current_node.right)
        #invoke the cb on the popped-off node
        cb(current_node.value)
     
  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value
