class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # def depth_first_for_each(self, cb):
    #     if(self is None):
    #         return
    #     cb(self.value)
    #     if(self.left):
    #         self.left.depth_first_for_each(cb)
    #     if(self.right):
    #         self.right.depth_first_for_each(cb)

    def depth_first_for_each(self, cb):
        stack = []
        stack.insert(0, self)
        while len(stack):
            el = stack.pop(0)
            if(el.right):
                stack.insert(0, el.right)
            if(el.left):
                stack.insert(0, el.left)
            cb(el.value)



    def breadth_first_for_each(self, cb):
        queue = []
        queue.append(self)
        while len(queue):
            el = queue.pop(0)
            if el.left:
                queue.append(el.left)
            if el.right:
                queue.append(el.right)
            cb(el.value)


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