from typing import List, Any


class Node:
    def __init__(self, data: Any) -> None:
        self.data: Any = data
        self.children: List[Node] = []


class Tree:
    def __init__(self) -> None:
        self.root: Node = None
