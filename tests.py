from mds import MixedDataStructure as MDS
from data import simple_dict, simple_list, simple_string, simple_int, list_in_dict, dict_in_list

# creation


def test_creation():
    MDS(simple_dict)
    MDS(simple_list)
    MDS(simple_string)
    MDS(simple_int)
    MDS(list_in_dict)
    MDS(dict_in_list)

# access


def test_access_success():
    s = MDS(simple_dict)
    assert s.get_value(['a']) == 1
    s = MDS(simple_list)
    assert s.get_value([2]) == 3
    s = MDS(simple_string)
    assert s.get_value() == 'mille'
    s = MDS(simple_int)
    assert s.get_value() == 1000
    s = MDS(list_in_dict)
    assert s.get_value(['b', 2]) == 3
    s = MDS(dict_in_list)
    assert s.get_value([2, 'b']) == 2


def test_access_key_error():
    # default default
    s = MDS(simple_dict)
    assert s.get_value(['blah']) == None
    # chosen default
    s = MDS(dict_in_list)
    assert s.get_value([2, 'huuu'], 30) == 30


def test_access_index_error():
    # default default
    s = MDS(simple_list)
    assert s.get_value([30]) == None
    # chosen default
    s = MDS(list_in_dict)
    assert s.get_value(['b', 30], 'x') == 'x'


def test_get_substructure():
    s = MDS(list_in_dict)
    assert isinstance(s.get(['b']), MDS)


def test_is_leaf():
    s = MDS(simple_dict)
    assert not s.is_leaf()
    s = MDS(simple_int)
    assert s.is_leaf()
    s = MDS(list_in_dict)
    assert not s.get(['b']).is_leaf()
    assert s.get(['a']).is_leaf()


def test_children():
    s = MDS(simple_dict)
    ch = s.children()
    assert len(ch) == 3
    assert ch[0] == 1
    for c in ch:
        assert isinstance(c, MDS)

    s = MDS(list_in_dict)
    ch = s.children()
    assert len(ch) == 3
    assert ch[1] == 3
    for c in ch:
        assert isinstance(c, MDS)


def test_traverse():
    s = MDS(simple_dict)
    elements = [e for e in s.traverse()]
    assert len(elements) == 3
    for e in elements:
        assert isinstance(e, MDS)

    s = MDS(simple_string)
    elements = [e for e in s.traverse()]
    assert len(elements) == 1
    for e in elements:
        assert isinstance(e, MDS)

if __name__ == '__main__':
    s = MDS(simple_dict)
    print s
    print type(s)
    for e in s.traverse():
        print e
        print type(e)
    elements = [e for e in s.traverse()]
    print elements
    assert len(elements) == 3
    # for e in elements:
    #     assert isinstance(e, MDS)
