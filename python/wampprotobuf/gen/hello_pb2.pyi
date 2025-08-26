from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Hello(_message.Message):
    __slots__ = ("realm", "authid", "authmethods", "roles", "public_key")
    class Roles(_message.Message):
        __slots__ = ("caller", "callee", "publisher", "subscriber")
        class Caller(_message.Message):
            __slots__ = ("caller_identification", "call_timeout", "call_canceling", "progressive_call_results")
            CALLER_IDENTIFICATION_FIELD_NUMBER: _ClassVar[int]
            CALL_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
            CALL_CANCELING_FIELD_NUMBER: _ClassVar[int]
            PROGRESSIVE_CALL_RESULTS_FIELD_NUMBER: _ClassVar[int]
            caller_identification: bool
            call_timeout: bool
            call_canceling: bool
            progressive_call_results: bool
            def __init__(self, caller_identification: bool = ..., call_timeout: bool = ..., call_canceling: bool = ..., progressive_call_results: bool = ...) -> None: ...
        class Callee(_message.Message):
            __slots__ = ("caller_identification", "call_timeout", "call_canceling", "progressive_call_results", "pattern_based_registration", "shared_registration")
            CALLER_IDENTIFICATION_FIELD_NUMBER: _ClassVar[int]
            CALL_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
            CALL_CANCELING_FIELD_NUMBER: _ClassVar[int]
            PROGRESSIVE_CALL_RESULTS_FIELD_NUMBER: _ClassVar[int]
            PATTERN_BASED_REGISTRATION_FIELD_NUMBER: _ClassVar[int]
            SHARED_REGISTRATION_FIELD_NUMBER: _ClassVar[int]
            caller_identification: bool
            call_timeout: bool
            call_canceling: bool
            progressive_call_results: bool
            pattern_based_registration: bool
            shared_registration: bool
            def __init__(self, caller_identification: bool = ..., call_timeout: bool = ..., call_canceling: bool = ..., progressive_call_results: bool = ..., pattern_based_registration: bool = ..., shared_registration: bool = ...) -> None: ...
        class Publisher(_message.Message):
            __slots__ = ("publisher_identification", "publisher_exclusion", "acknowledge_event_received")
            PUBLISHER_IDENTIFICATION_FIELD_NUMBER: _ClassVar[int]
            PUBLISHER_EXCLUSION_FIELD_NUMBER: _ClassVar[int]
            ACKNOWLEDGE_EVENT_RECEIVED_FIELD_NUMBER: _ClassVar[int]
            publisher_identification: bool
            publisher_exclusion: bool
            acknowledge_event_received: bool
            def __init__(self, publisher_identification: bool = ..., publisher_exclusion: bool = ..., acknowledge_event_received: bool = ...) -> None: ...
        class Subscriber(_message.Message):
            __slots__ = ("publisher_identification", "pattern_based_subscription")
            PUBLISHER_IDENTIFICATION_FIELD_NUMBER: _ClassVar[int]
            PATTERN_BASED_SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
            publisher_identification: bool
            pattern_based_subscription: bool
            def __init__(self, publisher_identification: bool = ..., pattern_based_subscription: bool = ...) -> None: ...
        CALLER_FIELD_NUMBER: _ClassVar[int]
        CALLEE_FIELD_NUMBER: _ClassVar[int]
        PUBLISHER_FIELD_NUMBER: _ClassVar[int]
        SUBSCRIBER_FIELD_NUMBER: _ClassVar[int]
        caller: Hello.Roles.Caller
        callee: Hello.Roles.Callee
        publisher: Hello.Roles.Publisher
        subscriber: Hello.Roles.Subscriber
        def __init__(self, caller: _Optional[_Union[Hello.Roles.Caller, _Mapping]] = ..., callee: _Optional[_Union[Hello.Roles.Callee, _Mapping]] = ..., publisher: _Optional[_Union[Hello.Roles.Publisher, _Mapping]] = ..., subscriber: _Optional[_Union[Hello.Roles.Subscriber, _Mapping]] = ...) -> None: ...
    REALM_FIELD_NUMBER: _ClassVar[int]
    AUTHID_FIELD_NUMBER: _ClassVar[int]
    AUTHMETHODS_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    realm: str
    authid: str
    authmethods: _containers.RepeatedScalarFieldContainer[str]
    roles: Hello.Roles
    public_key: str
    def __init__(self, realm: _Optional[str] = ..., authid: _Optional[str] = ..., authmethods: _Optional[_Iterable[str]] = ..., roles: _Optional[_Union[Hello.Roles, _Mapping]] = ..., public_key: _Optional[str] = ...) -> None: ...
