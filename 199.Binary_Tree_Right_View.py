#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 'distance' parameter represents distance from right

        # Store buckets for each level of the tree, and keep track of the rightmost node for each level (i.e. the one with the least 'score' distance)
        min_node = {}

        def dfs(node, depth=0, distance=0):
            if not node:
                return
            if depth not in result or result[depth][1] > distance:
                min_node[depth] = (node, distance)

            dfs(node.right, depth+1, 2*distance)
            dfs(node.left, depth+1, 2*distance + 1)

        dfs(root)

        result = []

        i = 0
        while i in min_node:
            result.append(min_node[i][0].val)
            i += 1

        return result