# from collections import deque
#
# axw = deque()
#
# axw.append('dcbjd')
# axw.append('qedgyashb')
# print(axw)
#
# axb = list()
#
# axb.append('cbdj')
# axb.append('wdsxvc')
# print(axb)
#
# print(axb.pop())
# print(axb)

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)


def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptops")
    root.add_child(laptop)

    return root


if __name__ == '__main__':
    build_product_tree()
