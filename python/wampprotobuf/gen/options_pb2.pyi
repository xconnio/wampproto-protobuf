from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class Match(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    exact: _ClassVar[Match]
    prefix: _ClassVar[Match]
    wildcard: _ClassVar[Match]

class Invoke(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    single: _ClassVar[Invoke]
    roundrobin: _ClassVar[Invoke]
    random: _ClassVar[Invoke]
    first: _ClassVar[Invoke]
    last: _ClassVar[Invoke]
exact: Match
prefix: Match
wildcard: Match
single: Invoke
roundrobin: Invoke
random: Invoke
first: Invoke
last: Invoke
