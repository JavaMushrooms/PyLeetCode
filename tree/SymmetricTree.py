"""

给定一个二叉树，检查它是否是镜像对称的。
 *
 *  * Definition for a binary tree node.
 *  * public class TreeNode {
 *  *     int val;
 *  *     TreeNode left;
 *  *     TreeNode right;
 *  *     TreeNode(int x) { val = x; }
 *  * }

"""

from bean import TreeNode


class SymmetricTree:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.symmetric(root, root)

    def symmetric(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        return (root1.val == root2.val) and self.symmetric(root1.left, root2.right) and self.symmetric(root1.right, root2.left)
