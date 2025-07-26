from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor
exact: Match
first: Invoke
last: Invoke
prefix: Match
random: Invoke
roundrobin: Invoke
single: Invoke
wildcard: Match

class Match(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class Invoke(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
