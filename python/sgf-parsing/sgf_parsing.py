
import re


class SgfTree:
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for k, v in self.properties.items():
            if k not in other.properties:
                return False
            if other.properties[k] != v:
                return False
        for k in other.properties.keys():
            if k not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for a, b in zip(self.children, other.children):
            if a != b:
                return False
        return True

    def __ne__(self, other):
        return not self == other


def parse(input_string):
    def parse_trees(input_string: str):
        if input_string == "":
            return None
        else:
            return SgfTree(None, parse_trees(input_string[0:input_string.find(")") + 1]))

    def parse_nodes(input_string):
        input = str(input_string)

        nodes = input.split(";")

        output = []

        for node in nodes[1:]:
            output.append(SgfTree(node))

        return nodes

    if not isinstance(input_string, str) or input_string == "":
        raise ValueError

    trees = parse_trees(input_string)

    output = []

    for tree in trees:
        output.append(SgfTree())

        for node in parse_nodes(tree):
            output[-1].children.append(node)

    return output

input_string = "(;A[B](;B[C])(;C[D]))"
expected = SgfTree(
    properties={"A": ["B"]},
    children=[SgfTree({"B": ["C"]}), SgfTree({"C": ["D"]})],
)
parse(input_string)