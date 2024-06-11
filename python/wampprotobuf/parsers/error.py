from wampproto.messages import Message
from wampproto.messages.error import IErrorFields, Error

from wampprotobuf.gen import error_pb2
from wampprotobuf.parsers import helpers


class ErrorFields(IErrorFields):
    def __init__(self, msg: error_pb2.Error):
        super().__init__()
        self._msg = msg
        self._args = None
        self._kwargs = None

    @property
    def message_type(self) -> int:
        return self._msg.message_type

    @property
    def request_id(self) -> int:
        return self._msg.request_id

    @property
    def uri(self) -> str:
        return self._msg.uri

    @property
    def details(self):
        return {}

    def unpack(self):
        try:
            args, kwargs = helpers.from_cbor_payload(self._msg.payload)
            self._args = args
            self._kwargs = kwargs
        except Exception as e:
            print(f"error parsing CBOR payload: {e}")

    @property
    def args(self):
        return self._args

    @property
    def kwargs(self):
        return self._kwargs

    @property
    def payload(self):
        return self._msg.payload

    @property
    def payload_serializer(self):
        return self._msg.payload_serializer

    def payload_is_binary(self):
        return True


def from_protobuf(payload: bytes) -> Message:
    result = error_pb2.Error()
    result.ParseFromString(payload)

    return Error(ErrorFields(result))


def to_protobuf(error: Error) -> bytes:
    result = error_pb2.Error()
    result.message_type = error.message_type
    result.request_id = error.request_id
    result.uri = error.uri

    if error.payload_is_binary():
        result.payload = error.payload
        result.payload_serializer = error.payload_serializer
    else:
        try:
            payload = helpers.to_cbor_payload(error.args, error.kwargs)
        except Exception as e:
            raise Exception(f"error in serialization to cbor: {e}")

        serializer = 1

        result.payload = payload
        result.payload_serializer = serializer

    return result.SerializeToString()
