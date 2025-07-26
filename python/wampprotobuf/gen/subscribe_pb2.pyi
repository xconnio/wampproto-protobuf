from protobuf import options_pb2 as _options_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Subscribe(_message.Message):
    __slots__ = ["get_retained", "match", "request_id", "topic"]
    GET_RETAINED_FIELD_NUMBER: _ClassVar[int]
    MATCH_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    get_retained: bool
    match: _options_pb2.Match
    request_id: int
    topic: str
    def __init__(self, request_id: _Optional[int] = ..., topic: _Optional[str] = ..., match: _Optional[_Union[_options_pb2.Match, str]] = ..., get_retained: bool = ...) -> None: ...
