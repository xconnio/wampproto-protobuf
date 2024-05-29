package parsers

import (
	"google.golang.org/protobuf/proto"

	"github.com/xconnio/wampproto-go/messages"
	"github.com/xconnio/wampproto-protobuf/go/gen"
)

func PublishToProtobuf(publish *messages.Publish) ([]byte, error) {
	return nil, nil
}

func ProtobufToPublish(data []byte) (*messages.Publish, error) {
	msg := &gen.Publish{}
	err := proto.Unmarshal(data[1:], msg)
	if err != nil {
		return nil, err
	}

	return nil, nil
}
