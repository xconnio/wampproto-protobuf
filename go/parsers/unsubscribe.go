package parsers

import (
	"google.golang.org/protobuf/proto"

	"github.com/xconnio/wampproto-go/messages"
	"github.com/xconnio/wampproto-protobuf/go/gen"
)

func UnsubscribeToProtobuf(unsubscribe *messages.UnSubscribe) ([]byte, error) {
	return nil, nil
}

func ProtobufToUnsubscribe(data []byte) (*messages.UnSubscribe, error) {
	msg := &gen.UnSubscribe{}
	err := proto.Unmarshal(data[1:], msg)
	if err != nil {
		return nil, err
	}

	return nil, nil
}
