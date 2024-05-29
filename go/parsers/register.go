package parsers

import (
	"google.golang.org/protobuf/proto"

	"github.com/xconnio/wampproto-go/messages"
	"github.com/xconnio/wampproto-protobuf/go/gen"
)

func RegisterToProtobuf(register *messages.Register) ([]byte, error) {
	return nil, nil
}

func ProtobufToRegister(data []byte) (*messages.Register, error) {
	msg := &gen.Register{}
	err := proto.Unmarshal(data[1:], msg)
	if err != nil {
		return nil, err
	}

	return nil, nil
}
