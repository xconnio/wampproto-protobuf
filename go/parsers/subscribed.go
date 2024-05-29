package parsers

import (
	"google.golang.org/protobuf/proto"

	"github.com/xconnio/wampproto-go/messages"
	"github.com/xconnio/wampproto-protobuf/go/gen"
)

func SubscribedToProtobuf(subscribed *messages.Subscribed) ([]byte, error) {
	return nil, nil
}

func ProtobufToSubscribed(data []byte) (*messages.Subscribed, error) {
	msg := &gen.Subscribed{}
	err := proto.Unmarshal(data[1:], msg)
	if err != nil {
		return nil, err
	}

	return nil, nil
}
