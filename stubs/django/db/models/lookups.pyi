# Stubs for django.db.models.lookups (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from django.db.models.expressions import Func
from django.db.models.query_utils import RegisterLookupMixin

class Lookup:
    lookup_name = ... # type: Any
    rhs = ... # type: Any
    bilateral_transforms = ... # type: Any
    def __init__(self, lhs, rhs): ...
    def apply_bilateral_transforms(self, value): ...
    def batch_process_rhs(self, compiler, connection, rhs=None): ...
    def get_prep_lookup(self): ...
    def get_db_prep_lookup(self, value, connection): ...
    def process_lhs(self, compiler, connection, lhs=None): ...
    def process_rhs(self, compiler, connection): ...
    def rhs_is_direct_value(self): ...
    def relabeled_clone(self, relabels): ...
    def get_group_by_cols(self): ...
    def as_sql(self, compiler, connection): ...
    def contains_aggregate(self): ...

class Transform(RegisterLookupMixin, Func):
    bilateral = ... # type: Any
    def __init__(self, expression, **extra): ...
    @property
    def lhs(self): ...
    def get_bilateral_transforms(self): ...

class BuiltinLookup(Lookup):
    def process_lhs(self, compiler, connection, lhs=None): ...
    def as_sql(self, compiler, connection): ...
    def get_rhs_op(self, connection, rhs): ...

class Exact(BuiltinLookup):
    lookup_name = ... # type: Any

class IExact(BuiltinLookup):
    lookup_name = ... # type: Any
    def process_rhs(self, qn, connection): ...

class GreaterThan(BuiltinLookup):
    lookup_name = ... # type: Any

class GreaterThanOrEqual(BuiltinLookup):
    lookup_name = ... # type: Any

class LessThan(BuiltinLookup):
    lookup_name = ... # type: Any

class LessThanOrEqual(BuiltinLookup):
    lookup_name = ... # type: Any

class In(BuiltinLookup):
    lookup_name = ... # type: Any
    def process_rhs(self, compiler, connection): ...
    def get_rhs_op(self, connection, rhs): ...
    def as_sql(self, compiler, connection): ...
    def split_parameter_list_as_sql(self, compiler, connection): ...

class PatternLookup(BuiltinLookup):
    def get_rhs_op(self, connection, rhs): ...

class Contains(PatternLookup):
    lookup_name = ... # type: Any
    def process_rhs(self, qn, connection): ...

class IContains(Contains):
    lookup_name = ... # type: Any

class StartsWith(PatternLookup):
    lookup_name = ... # type: Any
    def process_rhs(self, qn, connection): ...

class IStartsWith(PatternLookup):
    lookup_name = ... # type: Any
    def process_rhs(self, qn, connection): ...

class EndsWith(PatternLookup):
    lookup_name = ... # type: Any
    def process_rhs(self, qn, connection): ...

class IEndsWith(PatternLookup):
    lookup_name = ... # type: Any
    def process_rhs(self, qn, connection): ...

class Between(BuiltinLookup):
    def get_rhs_op(self, connection, rhs): ...

class Range(BuiltinLookup):
    lookup_name = ... # type: Any
    def get_rhs_op(self, connection, rhs): ...
    def process_rhs(self, compiler, connection): ...

class IsNull(BuiltinLookup):
    lookup_name = ... # type: Any
    def as_sql(self, compiler, connection): ...

class Search(BuiltinLookup):
    lookup_name = ... # type: Any
    def as_sql(self, compiler, connection): ...

class Regex(BuiltinLookup):
    lookup_name = ... # type: Any
    def as_sql(self, compiler, connection): ...

class IRegex(Regex):
    lookup_name = ... # type: Any

class DateTimeDateTransform(Transform):
    lookup_name = ... # type: Any
    def output_field(self): ...
    def as_sql(self, compiler, connection): ...

class DateTransform(Transform):
    def as_sql(self, compiler, connection): ...
    def output_field(self): ...

class YearTransform(DateTransform):
    lookup_name = ... # type: Any

class YearLookup(Lookup):
    def year_lookup_bounds(self, connection, year): ...

class YearExact(YearLookup):
    lookup_name = ... # type: Any
    def as_sql(self, compiler, connection): ...

class YearComparisonLookup(YearLookup):
    def as_sql(self, compiler, connection): ...
    def get_rhs_op(self, connection, rhs): ...
    def get_bound(self): ...

class YearGt(YearComparisonLookup):
    lookup_name = ... # type: Any
    def get_bound(self, start, finish): ...

class YearGte(YearComparisonLookup):
    lookup_name = ... # type: Any
    def get_bound(self, start, finish): ...

class YearLt(YearComparisonLookup):
    lookup_name = ... # type: Any
    def get_bound(self, start, finish): ...

class YearLte(YearComparisonLookup):
    lookup_name = ... # type: Any
    def get_bound(self, start, finish): ...

class MonthTransform(DateTransform):
    lookup_name = ... # type: Any

class DayTransform(DateTransform):
    lookup_name = ... # type: Any

class WeekDayTransform(DateTransform):
    lookup_name = ... # type: Any

class HourTransform(DateTransform):
    lookup_name = ... # type: Any

class MinuteTransform(DateTransform):
    lookup_name = ... # type: Any

class SecondTransform(DateTransform):
    lookup_name = ... # type: Any
