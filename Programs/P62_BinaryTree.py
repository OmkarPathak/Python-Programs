# Author: OMKAR PATHAK
# A data structure in which a record is linked to two successor records, usually referred to as
# the left branch when greater and the right when less than the previous record.

class BinaryTree(object):

    def __init__(self,nodeData):
      self.left = None
      self.right = None
      self.nodeData = nodeData

    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right

    def setnodeDataValue(self,value):
        self.nodeData = value

    def getnodeDataValue(self):
        return self.nodeData

    def insertRight(self,newnodeData):
        if self.right == None:
            self.right = BinaryTree(newnodeData)
        else:
            tree = BinaryTree(newnodeData)
            tree.right = self.right
            self.right = tree

    def insertLeft(self,newnodeData):
        if self.left == None:
            self.left = BinaryTree(newnodeData)
        else:
            tree = BinaryTree(newnodeData)
            self.left = tree
            tree.left = self.left




def printTree(tree):
        if tree != None:
            printTree(tree.getLeftChild())
            print(tree.getnodeDataValue())
            printTree(tree.getRightChild())


def pprint(head_node, _pre="", _last=True, term=False):
    data = "*" if head_node is None else head_node.nodeData

    print(_pre, "`- " if _last else "|- ", data, sep="")
    _pre += "   " if _last else "|  "

    if term: return

    left = head_node.getLeftChild()
    right = head_node.getRightChild()

    for i, child in enumerate([left, right]):
        pprint(child,  _pre, bool(i) ,term=not(bool(child)))




def testTree():
    myTree = BinaryTree("1")
    myTree.insertLeft("2")
    myTree.insertRight("3")
    myTree.insertRight("4")
    printTree(myTree)
    pprint(myTree)

if __name__ == '__main__':
    testTree()

    # OUTPUT
    # 2
    # 1
    # 4
    # 3
