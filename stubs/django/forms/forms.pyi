# Stubs for django.forms.forms (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from django.forms.widgets import MediaDefiningClass
from django.utils.translation import ugettext as _

class DeclarativeFieldsMetaclass(MediaDefiningClass):
    def __new__(mcs, name, bases, attrs): ...

class BaseForm:
    field_order = ... # type: Any
    prefix = ... # type: Any
    is_bound = ... # type: Any
    data = ... # type: Any
    files = ... # type: Any
    auto_id = ... # type: Any
    initial = ... # type: Any
    error_class = ... # type: Any
    label_suffix = ... # type: Any
    empty_permitted = ... # type: Any
    fields = ... # type: Any
    def __init__(self, data=None, files=None, auto_id='', prefix=None, initial=None, error_class=..., label_suffix=None, empty_permitted=False, field_order=None): ...
    def order_fields(self, field_order): ...
    def __iter__(self): ...
    def __getitem__(self, name): ...
    @property
    def errors(self): ...
    def is_valid(self): ...
    def add_prefix(self, field_name): ...
    def add_initial_prefix(self, field_name): ...
    def as_table(self): ...
    def as_ul(self): ...
    def as_p(self): ...
    def non_field_errors(self): ...
    def add_error(self, field, error): ...
    def has_error(self, field, code=None): ...
    cleaned_data = ... # type: Any
    def full_clean(self): ...
    def clean(self): ...
    def has_changed(self): ...
    def changed_data(self): ...
    @property
    def media(self): ...
    def is_multipart(self): ...
    def hidden_fields(self): ...
    def visible_fields(self): ...

class Form: ...
