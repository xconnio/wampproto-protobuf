package parsers

import (
	"fmt"

	"google.golang.org/protobuf/proto"

	"github.com/xconnio/wampproto-go/messages"
	"github.com/xconnio/wampproto-protobuf/go/gen"
)

type Challenge struct {
	gen *gen.Challenge
}

func NewChallengeFields(gen *gen.Challenge) messages.ChallengeFields {
	return &Challenge{gen: gen}
}

func (c *Challenge) AuthMethod() string {
	return c.gen.AuthMethod
}

func (c *Challenge) Extra() map[string]any {
	return map[string]any{
		"challenge": c.gen.Challenge,
	}
}

func ChallengeToProtobuf(challenge *messages.Challenge) ([]byte, error) {
	challengeValue, ok := challenge.Extra()["challenge"].(string)
	if !ok {
		return nil, fmt.Errorf("challenge value is not a string")
	}

	msg := &gen.Challenge{
		AuthMethod: challenge.AuthMethod(),
		Challenge:  challengeValue,
	}

	data, err := proto.Marshal(msg)
	if err != nil {
		return nil, err
	}

	byteValue := byte(messages.MessageTypeChallenge & 0xFF)
	return append([]byte{byteValue}, data...), nil
}

func ProtobufToChallenge(data []byte) (*messages.Challenge, error) {
	msg := &gen.Challenge{}
	err := proto.Unmarshal(data, msg)
	if err != nil {
		return nil, err
	}

	return messages.NewChallengeWithFields(NewChallengeFields(msg)), nil
}
