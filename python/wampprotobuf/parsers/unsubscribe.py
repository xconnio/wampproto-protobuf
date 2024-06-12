from wampproto.messages import Message
from wampproto.messages.unsubscribe import IUnSubscribeFields, UnSubscribe

from wampprotobuf.gen import unsubscribe_pb2


class UnSubscribeFields(IUnSubscribeFields):
    def __init__(self, msg: unsubscribe_pb2.UnSubscribe):
        self._msg = msg

    @property
    def request_id(self) -> int:
        return self._msg.request_id

    @property
    def subscription_id(self) -> int:
        return self._msg.subscription_id


def from_protobuf(payload: bytes) -> Message:
    result = unsubscribe_pb2.UnSubscribe()
    result.ParseFromString(payload)

    return UnSubscribe(UnSubscribeFields(result))


def to_protobuf(unsubscribe: UnSubscribe) -> bytes:
    result = unsubscribe_pb2.UnSubscribe()
    result.request_id = unsubscribe.request_id
    result.subscription_id = unsubscribe.subscription_id

    return result.SerializeToString()
