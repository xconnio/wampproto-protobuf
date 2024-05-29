package parsers

import (
	"google.golang.org/protobuf/proto"

	"github.com/xconnio/wampproto-go/messages"
	"github.com/xconnio/wampproto-protobuf/go/gen"
)

func AbortToProtobuf(abort *messages.Abort) ([]byte, error) {
	return nil, nil
}

func ProtobufToAbort(data []byte) (*messages.Abort, error) {
	msg := &gen.Abort{}
	err := proto.Unmarshal(data, msg)
	if err != nil {
		return nil, err
	}

	return nil, nil
}
