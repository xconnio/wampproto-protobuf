from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Event(_message.Message):
    __slots__ = ("subscription_id", "publication_id", "payload_serializer_id", "publisher", "publisher_authid", "publisher_authrole", "topic")
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    PUBLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_SERIALIZER_ID_FIELD_NUMBER: _ClassVar[int]
    PUBLISHER_FIELD_NUMBER: _ClassVar[int]
    PUBLISHER_AUTHID_FIELD_NUMBER: _ClassVar[int]
    PUBLISHER_AUTHROLE_FIELD_NUMBER: _ClassVar[int]
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    subscription_id: int
    publication_id: int
    payload_serializer_id: int
    publisher: int
    publisher_authid: str
    publisher_authrole: str
    topic: str
    def __init__(self, subscription_id: _Optional[int] = ..., publication_id: _Optional[int] = ..., payload_serializer_id: _Optional[int] = ..., publisher: _Optional[int] = ..., publisher_authid: _Optional[str] = ..., publisher_authrole: _Optional[str] = ..., topic: _Optional[str] = ...) -> None: ...
