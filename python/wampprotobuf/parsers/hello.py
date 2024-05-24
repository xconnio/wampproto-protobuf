from wampprotobuf.gen.protobuf import hello_pb2


class HelloParser:
    def do(self):
        hello = hello_pb2.Hello()
        hello.authid = "hello"
        hello.realm = "ok"
        hello.authprovider = "static"
        hello.authmethod = "cryptosign"
        hello.authmethod = "ticket"
        hello.authmethod = "cra"
        hello.authmethod = "anonymous"

        data = hello.SerializeToString()
        hello2 = hello_pb2.Hello()
        hello2.ParseFromString(data)
