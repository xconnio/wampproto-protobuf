import pytest

from wampprotobuf.gen import hello_pb2, call_pb2

import random
data = random.randbytes(1024*1024*1)


@pytest.mark.skip
def test_hello():
    for i in range(1000):
        hello = hello_pb2.Hello()
        hello.authid = "hello"
        hello.realm = "ok"
        hello.authprovider = "static"
        hello.authmethod.append("cryptosign")
        hello.authmethod.append("ticket")
        hello.authmethod.append("cra")
        hello.authmethod.append("anonymous")

        data = hello.SerializeToString()
        hello2 = hello_pb2.Hello()
        hello2.ParseFromString(data)
        assert hello.authid == hello2.authid
        assert hello.realm == hello2.realm
        assert hello.authprovider == hello2.authprovider


def test_call():
    for i in range(10000):
        call = call_pb2.Call()
        call.request_id = 1 << 53
        call.procedure = "foo.bar.account.get"
        call.payload = data
        serialized = call.SerializeToString()

        call2 = call_pb2.Call()
        call2.ParseFromString(serialized)
        assert call.payload == data
