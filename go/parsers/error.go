package parsers

import (
	"google.golang.org/protobuf/proto"

	"github.com/xconnio/wampproto-go/messages"
	"github.com/xconnio/wampproto-protobuf/go/gen"
)

func ErrorToProtobuf(error *messages.Error) ([]byte, error) {
	return nil, nil
}

func ProtobufToError(data []byte) (*messages.Error, error) {
	msg := &gen.Error{}
	err := proto.Unmarshal(data[1:], msg)
	if err != nil {
		return nil, err
	}

	return nil, nil
}
