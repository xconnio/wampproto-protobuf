package parsers

import (
	"google.golang.org/protobuf/proto"

	"github.com/xconnio/wampproto-go/messages"
	"github.com/xconnio/wampproto-protobuf/go/gen"
)

func UnregisteredToProtobuf(unregistered *messages.UnRegistered) ([]byte, error) {
	return nil, nil
}

func ProtobufToUnregistered(data []byte) (*messages.UnRegistered, error) {
	msg := &gen.UnRegistered{}
	err := proto.Unmarshal(data[1:], msg)
	if err != nil {
		return nil, err
	}

	return nil, nil
}
