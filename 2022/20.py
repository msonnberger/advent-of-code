from aocd import numbers


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


def solve(part2=False):
    nodes = []

    for num in numbers:
        val = num if not part2 else num * 811589153
        nodes.append(Node(val))

    for i in range(1, len(nodes) - 1):
        nodes[i].prev = nodes[i - 1]
        nodes[i].next = nodes[i + 1]

    nodes[0].prev = nodes[len(nodes) - 1]
    nodes[0].next = nodes[1]
    nodes[len(nodes) - 1].next = nodes[0]
    nodes[len(nodes) - 1].prev = nodes[len(nodes) - 2]

    for _ in range(1 if not part2 else 10):
        for node in nodes:
            node.prev.next = node.next
            node.next.prev = node.prev
            prev, nxt = node.prev, node.next

            for _ in range(node.value % (len(nodes) - 1)):
                prev = prev.next
                nxt = nxt.next

            prev.next = node
            node.prev = prev
            nxt.prev = node
            node.next = nxt

    for node in nodes:
        if node.value == 0:
            total = 0
            ptr = node

            for _ in range(3):
                for _ in range(1000):
                    ptr = ptr.next

                total += ptr.value

            return total


print(f"part 1: {solve()}")
print(f"part 2: {solve(True)}")
