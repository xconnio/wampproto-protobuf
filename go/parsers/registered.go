package parsers

import (
	"google.golang.org/protobuf/proto"

	"github.com/xconnio/wampproto-go/messages"
	"github.com/xconnio/wampproto-protobuf/go/gen"
)

func RegisteredToProtobuf(registered *messages.Registered) ([]byte, error) {
	return nil, nil
}

func ProtobufToRegistered(data []byte) (*messages.Registered, error) {
	msg := &gen.Registered{}
	err := proto.Unmarshal(data[1:], msg)
	if err != nil {
		return nil, err
	}

	return nil, nil
}
