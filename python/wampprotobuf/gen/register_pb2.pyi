from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Register(_message.Message):
    __slots__ = ("request_id", "procedure", "invoke", "match")
    class Invoke(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SINGLE: _ClassVar[Register.Invoke]
        ROUNDROBIN: _ClassVar[Register.Invoke]
        RANDOM: _ClassVar[Register.Invoke]
        FIRST: _ClassVar[Register.Invoke]
        LAST: _ClassVar[Register.Invoke]
    SINGLE: Register.Invoke
    ROUNDROBIN: Register.Invoke
    RANDOM: Register.Invoke
    FIRST: Register.Invoke
    LAST: Register.Invoke
    class Match(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EXACT: _ClassVar[Register.Match]
        PREFIX: _ClassVar[Register.Match]
        WILDCARD: _ClassVar[Register.Match]
    EXACT: Register.Match
    PREFIX: Register.Match
    WILDCARD: Register.Match
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    PROCEDURE_FIELD_NUMBER: _ClassVar[int]
    INVOKE_FIELD_NUMBER: _ClassVar[int]
    MATCH_FIELD_NUMBER: _ClassVar[int]
    request_id: int
    procedure: str
    invoke: Register.Invoke
    match: Register.Match
    def __init__(self, request_id: _Optional[int] = ..., procedure: _Optional[str] = ..., invoke: _Optional[_Union[Register.Invoke, str]] = ..., match: _Optional[_Union[Register.Match, str]] = ...) -> None: ...
