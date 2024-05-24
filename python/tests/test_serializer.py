from wampproto.messages.hello import Hello, HelloFields

from wampprotobuf import ProtobufSerializer


def test_serialize_deserialize():
    serializer = ProtobufSerializer()

    for i in range(100000):
        hello = Hello(HelloFields("realm1", {"caller": {}}, "", authmethods=[]))
        data = serializer.serialize(hello)
        message = serializer.deserialize(data)
        assert message.TYPE == hello.TYPE
