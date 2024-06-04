package parsers

import (
	"google.golang.org/protobuf/proto"

	"github.com/xconnio/wampproto-go/messages"
	"github.com/xconnio/wampproto-protobuf/go/gen"
)

func UnregisterToProtobuf(unregister *messages.UnRegister) ([]byte, error) {
	return nil, nil
}

func ProtobufToUnregister(data []byte) (*messages.UnRegister, error) {
	msg := &gen.UnRegister{}
	err := proto.Unmarshal(data[1:], msg)
	if err != nil {
		return nil, err
	}

	return nil, nil
}
