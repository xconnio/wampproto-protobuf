from protobuf import options_pb2 as _options_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Subscribe(_message.Message):
    __slots__ = ("request_id", "topic", "match", "get_retained")
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    MATCH_FIELD_NUMBER: _ClassVar[int]
    GET_RETAINED_FIELD_NUMBER: _ClassVar[int]
    request_id: int
    topic: str
    match: _options_pb2.Match
    get_retained: bool
    def __init__(self, request_id: _Optional[int] = ..., topic: _Optional[str] = ..., match: _Optional[_Union[_options_pb2.Match, str]] = ..., get_retained: bool = ...) -> None: ...
