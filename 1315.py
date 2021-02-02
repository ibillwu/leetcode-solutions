# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def checkGrandpaEven(node,grandfather,father):
    total=0
    me=int(node.val%2!=1)
    if node.left!=None:
        total+=checkGrandpaEven(node.left,father,me)
        print(total)
    if node.right!=None:
        total+=checkGrandpaEven(node.right,father,me) 
        print(total)
    return(total+node.val*grandfather)
    
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        total=checkGrandpaEven(root,0,0)
        return total
