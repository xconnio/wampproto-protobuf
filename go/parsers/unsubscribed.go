package parsers

import (
	"google.golang.org/protobuf/proto"

	"github.com/xconnio/wampproto-go/messages"
	"github.com/xconnio/wampproto-protobuf/go/gen"
)

func UnsubscribedToProtobuf(unsubscribed *messages.UnSubscribed) ([]byte, error) {
	return nil, nil
}

func ProtobufToUnsubscribed(data []byte) (*messages.UnSubscribed, error) {
	msg := &gen.UnSubscribed{}
	err := proto.Unmarshal(data[1:], msg)
	if err != nil {
		return nil, err
	}

	return nil, nil
}
