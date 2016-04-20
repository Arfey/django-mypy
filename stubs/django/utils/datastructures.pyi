# Stubs for django.utils.datastructures (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class OrderedSet:
    dict = ... # type: Any
    def __init__(self, iterable=None): ...
    def add(self, item): ...
    def remove(self, item): ...
    def discard(self, item): ...
    def __iter__(self): ...
    def __contains__(self, item): ...
    def __bool__(self): ...
    def __nonzero__(self): ...
    def __len__(self): ...

class MultiValueDictKeyError(KeyError): ...

class MultiValueDict(dict):
    def __init__(self, key_to_list_mapping=...): ...
    def __getitem__(self, key): ...
    def __setitem__(self, key, value): ...
    def __copy__(self): ...
    def __deepcopy__(self, memo=None): ...
    def get(self, key, default=None): ...
    def getlist(self, key, default=None): ...
    def setlist(self, key, list_): ...
    def setdefault(self, key, default=None): ...
    def setlistdefault(self, key, default_list=None): ...
    def appendlist(self, key, value): ...
    items = ... # type: Any
    lists = ... # type: Any
    values = ... # type: Any
    iteritems = ... # type: Any
    iterlists = ... # type: Any
    itervalues = ... # type: Any
    def copy(self): ...
    def update(self, *args, **kwargs): ...
    def dict(self): ...

class ImmutableList(tuple):
    warning = ... # type: Any
    def __new__(cls, *args, **kwargs): ...
    def complain(self, *wargs, **kwargs): ...
    __delitem__ = ... # type: Any
    __delslice__ = ... # type: Any
    __iadd__ = ... # type: Any
    __imul__ = ... # type: Any
    __setitem__ = ... # type: Any
    __setslice__ = ... # type: Any
    append = ... # type: Any
    extend = ... # type: Any
    insert = ... # type: Any
    pop = ... # type: Any
    remove = ... # type: Any
    sort = ... # type: Any
    reverse = ... # type: Any

class DictWrapper(dict):
    func = ... # type: Any
    prefix = ... # type: Any
    def __init__(self, data, func, prefix): ...
    def __getitem__(self, key): ...
