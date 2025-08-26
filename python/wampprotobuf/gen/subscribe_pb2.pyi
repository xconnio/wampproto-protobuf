from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Subscribe(_message.Message):
    __slots__ = ("request_id", "topic", "match")
    class Match(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EXACT: _ClassVar[Subscribe.Match]
        PREFIX: _ClassVar[Subscribe.Match]
        WILDCARD: _ClassVar[Subscribe.Match]
    EXACT: Subscribe.Match
    PREFIX: Subscribe.Match
    WILDCARD: Subscribe.Match
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    MATCH_FIELD_NUMBER: _ClassVar[int]
    request_id: int
    topic: str
    match: Subscribe.Match
    def __init__(self, request_id: _Optional[int] = ..., topic: _Optional[str] = ..., match: _Optional[_Union[Subscribe.Match, str]] = ...) -> None: ...
