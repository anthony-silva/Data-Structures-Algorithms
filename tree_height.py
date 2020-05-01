'''
 python3
 Author: Anthony Silva

 Description: You are given a description of a rooted tree. The task is to
    compute and output its height. Recall that the height of a (rooted) tree
    is the maximum depth of a node, or the maximum distance from a leaf to the
    root. You are given an arbitrary tree, not necessarily a binary tree.

 Input: The first line contains the number of nodes 𝑛. The second line contains 𝑛
    integer numbers from −1 to 𝑛 − 1 — parents of nodes. If the 𝑖-th one of them
    (0 ≤ 𝑖 ≤ 𝑛 − 1) is −1, node 𝑖 is the root, otherwise it’s 0-based index of the
    parent of 𝑖-th node. It is guaranteed that there is exactly one root. It is
    guaranteed that the input represents a tree.

 Output: Output the height of the tree.
'''

class TreeHeight:
    def __init__(self, parent, n):
        self.n = n
        self.parent = parent
        self.nodes = {}
        for i in range(self.n):
            self.nodes[i] = []
        for i in range(self.n):
            if self.parent[i] == -1:
                pass
            else:
                self.nodes[parent[i]] += [i]

    def ComputeHeight(self):
        root = None
        try:
            root = self.parent.index(-1)
        except ValueError:
            return 0

        queue = []
        queue.append(root)
        height = 0

        while True:
            node_count = len(queue)
            if node_count == 0:
                return height
            height += 1
            while node_count > 0:
                node = queue.pop(0)
                if self.nodes[node]:
                    for v in self.nodes[node]:
                        queue.append(v)
                node_count -= 1


if __name__ == "__main__":
    n = int(input()) # number of nodes in tree
    parent = [int(x) for x in input().split()]
    tree = TreeHeight(parent, n)
    print(tree.ComputeHeight())