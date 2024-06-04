package parsers

import (
	"google.golang.org/protobuf/proto"

	"github.com/xconnio/wampproto-go/messages"
	"github.com/xconnio/wampproto-protobuf/go/gen"
)

func SubscribeToProtobuf(subscribe *messages.Subscribe) ([]byte, error) {
	return nil, nil
}

func ProtobufToSubscribe(data []byte) (*messages.Subscribe, error) {
	msg := &gen.Subscribe{}
	err := proto.Unmarshal(data[1:], msg)
	if err != nil {
		return nil, err
	}

	return nil, nil
}
