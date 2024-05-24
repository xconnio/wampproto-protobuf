from wampproto import serializers, messages

from wampprotobuf.parsers import hello


class ProtobufSerializer(serializers.Serializer):
    def serialize(self, message: messages.Message) -> bytes:
        if isinstance(message, messages.Hello):
            message_id = messages.Hello.TYPE.to_bytes(1, byteorder='little')
            return message_id + hello.to_protobuf(message)
        else:
            raise TypeError("unknown message type")

    def deserialize(self, data: bytes) -> messages.Message:
        msg_type = data[0]
        match msg_type:
            case messages.Hello.TYPE:
                return hello.from_protobuf(data[1:])
            case _:
                raise ValueError("not supported.")
