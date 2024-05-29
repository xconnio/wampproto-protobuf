package parsers

import (
	"google.golang.org/protobuf/proto"

	"github.com/xconnio/wampproto-go/messages"
	"github.com/xconnio/wampproto-protobuf/go/gen"
)

func CancelToProtobuf(cancel *messages.Cancel) ([]byte, error) {
	return nil, nil
}

func ProtobufToCancel(data []byte) (*messages.Cancel, error) {
	msg := &gen.Cancel{}
	err := proto.Unmarshal(data[1:], msg)
	if err != nil {
		return nil, err
	}

	return nil, nil
}
