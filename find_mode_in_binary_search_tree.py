
class Solution(object):
    def findMode(self, root):
        result = []
        max_freq = [0]
        current_freq = [0]
        previous = [None]

        def inorder(node):
            if not node:
                return

            inorder(node.left)

            if previous[0] == node.val:
                current_freq[0] += 1
            else:
                current_freq[0] = 1

            if current_freq[0] > max_freq[0]:
                max_freq[0] = current_freq[0]
                result[:] = [node.val]
            elif current_freq[0] == max_freq[0]:
                result.append(node.val)

            previous[0] = node.val

            inorder(node.right)

        inorder(root)
        return result
