package parsers

import (
	"google.golang.org/protobuf/proto"

	"github.com/xconnio/wampproto-go/messages"
	"github.com/xconnio/wampproto-protobuf/go/gen"
)

func AuthenticateToProtobuf(authenticate *messages.Authenticate) ([]byte, error) {
	return nil, nil
}

func ProtobufToAuthenticate(data []byte) (*messages.Authenticate, error) {
	msg := &gen.Authenticate{}
	err := proto.Unmarshal(data[1:], msg)
	if err != nil {
		return nil, err
	}

	return nil, nil
}
