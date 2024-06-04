package parsers

import (
	"google.golang.org/protobuf/proto"

	"github.com/xconnio/wampproto-go/messages"
	"github.com/xconnio/wampproto-protobuf/go/gen"
)

func InterruptToProtobuf(interrupt *messages.Interrupt) ([]byte, error) {
	return nil, nil
}

func ProtobufToInterrupt(data []byte) (*messages.Interrupt, error) {
	msg := &gen.Interrupt{}
	err := proto.Unmarshal(data[1:], msg)
	if err != nil {
		return nil, err
	}

	return nil, nil
}
