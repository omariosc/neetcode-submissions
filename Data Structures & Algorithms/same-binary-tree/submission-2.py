import hashlib

class Solution:
    def isSameTree(self, p, q):

        def merkle(node):
            if node is None:
                yield "null"
                return

            # compute child hashes lazily
            left_hash = next(merkle(node.left))
            right_hash = next(merkle(node.right))

            data = f"{node.val}-{left_hash}-{right_hash}".encode()
            node_hash = hashlib.sha256(data).hexdigest()

            yield node_hash

        return next(merkle(p)) == next(merkle(q))