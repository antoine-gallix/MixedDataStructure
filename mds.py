from pprint import pformat


def StructureError(Exception):
    pass


class MixedDataStructure(object):

    def __init__(self, s):
        self.s = s

    def get_value(self, keys=None, default=None):
        """get a value in the structure following a series of keys and indexes.
        Return a default value in case of wrong key or index
        """

        keys = keys or []
        try:
            return reduce(lambda s, k: s[k], keys, self.s)
        except (KeyError, IndexError):
            return default

    def get(self, keys=None, default=None):
        """Same as get_value, but returns another MixedDataStructure
        """
        return MixedDataStructure(self.get_value(keys, default))

    def is_leaf(self):
        return not(isinstance(self.s, dict) or isinstance(self.s, list))

    def children(self):
        """return a list of the children of the structure.
        Each children is another structure
        If the structure is a list
        """

        if isinstance(self.s, list):
            return MixedDataStructure(self.s)
        elif isinstance(self.s, dict):
            return [MixedDataStructure(self.s[k]) for k in self.s]
        else:
            return StructureError('this node has no children')

    def traverse(self):
        if self.is_leaf():
            yield self
        else:
            for c in self.children():
                yield c.traverse()

    def __eq__(self, o):
        return o == self.s

    def __str__(self):
        if self.is_leaf():
            return str(self.s)
        else:
            return pformat(self.s)

    def __repr__(self):
        return repr(self.s)
