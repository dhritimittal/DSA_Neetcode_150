class Solution:
    def buildTree(self, inorder, postorder):
        self.postIdx = len(postorder)-1
        def build(inStart, inEnd):
            if inStart > inEnd: return None
            root = TreeNode(postorder[self.postIdx])
            self.postIdx -= 1
            root.right = build(inorder.index(root.val)+1, inEnd)
            root.left  = build(inStart, inorder.index(root.val)-1)
            return root        
        return build(0, len(inorder)-1)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna