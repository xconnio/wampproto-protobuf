package parsers

import (
	"google.golang.org/protobuf/proto"

	"github.com/xconnio/wampproto-go/messages"
	"github.com/xconnio/wampproto-protobuf/go/gen"
)

func WelcomeToProtobuf(welcome *messages.Welcome) ([]byte, error) {
	return nil, nil
}

func ProtobufToWelcome(data []byte) (*messages.Welcome, error) {
	msg := &gen.Welcome{}
	err := proto.Unmarshal(data[1:], msg)
	if err != nil {
		return nil, err
	}

	return nil, nil
}
