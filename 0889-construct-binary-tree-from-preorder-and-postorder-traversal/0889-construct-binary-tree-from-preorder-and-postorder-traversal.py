# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> Optional[TreeNode]:
        def build_tree(pre_start, pre_end, post_start, post_end):
            if pre_start > pre_end or post_start > post_end:
                return None

            root = TreeNode(pre[pre_start])

            if pre_start == pre_end or post_start == post_end:
                return root

            post_root_index = post.index(pre[pre_start + 1])
            left_subtree_size = post_root_index - post_start + 1

            root.left = build_tree(pre_start + 1, pre_start + left_subtree_size, post_start, post_root_index)
            root.right = build_tree(pre_start + left_subtree_size + 1, pre_end, post_root_index + 1, post_end - 1)

            return root

        return build_tree(0, len(pre) - 1, 0, len(post) - 1)

        