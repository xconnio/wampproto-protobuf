from wampproto.messages import Message
from wampproto.messages.published import IPublishedFields, Published

from wampprotobuf.gen import published_pb2


class PublishedFields(IPublishedFields):
    def __init__(self, msg: published_pb2.Published):
        self._msg = msg

    @property
    def request_id(self) -> int:
        return self._msg.request_id

    @property
    def publication_id(self) -> int:
        return self._msg.publication_id


def from_protobuf(payload: bytes) -> Message:
    result = published_pb2.Published()
    result.ParseFromString(payload)

    return Published(PublishedFields(result))


def to_protobuf(published: Published) -> bytes:
    result = published_pb2.Published()
    result.request_id = published.request_id
    result.publication_id = published.publication_id

    return result.SerializeToString()
