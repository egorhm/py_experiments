class Node(object):
    parent = None

    def __init__(self, *children):
        self.children = list(children)
        print(self.children)
        for node in self.children:
            node.parent = self
            print(self)


    @classmethod
    def tree(cls, depth=1, numchildren=1):
        if depth == 0:
            return []
        return [cls(*cls.tree(depth-1, numchildren))
                for _ in range(numchildren)]


if __name__ == '__main__':
    Node.tree(depth=2, numchildren=3)

    print("end")
