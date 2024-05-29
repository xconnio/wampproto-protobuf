package parsers

import (
	"google.golang.org/protobuf/proto"

	"github.com/xconnio/wampproto-go/messages"
	"github.com/xconnio/wampproto-protobuf/go/gen"
)

func GoodbyeToProtobuf(goodbye *messages.GoodBye) ([]byte, error) {
	return nil, nil
}

func ProtobufToGoodbye(data []byte) (*messages.GoodBye, error) {
	msg := &gen.Goodbye{}
	err := proto.Unmarshal(data[1:], msg)
	if err != nil {
		return nil, err
	}

	return nil, nil
}
