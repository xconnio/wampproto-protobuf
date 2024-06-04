package parsers

import (
	"google.golang.org/protobuf/proto"

	"github.com/xconnio/wampproto-go/messages"
	"github.com/xconnio/wampproto-protobuf/go/gen"
)

type hello struct {
	gen *gen.Hello
}

func NewHelloFields(call *gen.Hello) messages.HelloFields {
	return &hello{
		gen: call,
	}
}

func (h *hello) Realm() string {
	return h.gen.Realm
}

func (h *hello) AuthID() string {
	return h.gen.Authid
}

func (h *hello) AuthMethods() []string {
	return nil
}

func (h *hello) AuthExtra() map[string]any {
	return map[string]any{}
}

func (h *hello) Roles() map[string]any {
	return map[string]any{}
}

func HelloToProtobuf(hello *messages.Hello) ([]byte, error) {
	msg := &gen.Hello{
		Realm:        hello.Realm(),
		Authid:       hello.AuthID(),
		Authprovider: "static",
	}

	data, err := proto.Marshal(msg)
	if err != nil {
		return nil, err
	}

	byteValue := byte(messages.MessageTypeHello & 0xFF)
	return append([]byte{byteValue}, data...), nil
}

func ProtobufToHello(data []byte) (*messages.Hello, error) {
	msg := &gen.Hello{}
	err := proto.Unmarshal(data, msg)
	if err != nil {
		return nil, err
	}

	return messages.NewHelloWithFields(NewHelloFields(msg)), nil
}
