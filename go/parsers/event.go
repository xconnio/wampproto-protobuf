package parsers

import (
	"google.golang.org/protobuf/proto"

	"github.com/xconnio/wampproto-go/messages"
	"github.com/xconnio/wampproto-protobuf/go/gen"
)

func EventToProtobuf(event *messages.Event) ([]byte, error) {
	return nil, nil
}

func ProtobufToEvent(data []byte) (*messages.Event, error) {
	msg := &gen.Event{}
	err := proto.Unmarshal(data[1:], msg)
	if err != nil {
		return nil, err
	}

	return nil, nil
}
