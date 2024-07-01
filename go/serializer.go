package wampprotobuf

import (
	"fmt"

	"github.com/xconnio/wampproto-go/messages"
	"github.com/xconnio/wampproto-go/serializers"
	"github.com/xconnio/wampproto-protobuf/go/parsers"
)

type ProtobufSerializer struct{}

var _ serializers.Serializer = &ProtobufSerializer{}

func (p *ProtobufSerializer) Serialize(message messages.Message) ([]byte, error) {
	switch message.Type() {
	case messages.MessageTypeHello:
		msg := message.(*messages.Hello)
		return parsers.HelloToProtobuf(msg)
	case messages.MessageTypeWelcome:
		msg := message.(*messages.Welcome)
		return parsers.WelcomeToProtobuf(msg)
	case messages.MessageTypeChallenge:
		msg := message.(*messages.Challenge)
		return parsers.ChallengeToProtobuf(msg)
	case messages.MessageTypeAuthenticate:
		msg := message.(*messages.Authenticate)
		return parsers.AuthenticateToProtobuf(msg)
	case messages.MessageTypeAbort:
		msg := message.(*messages.Abort)
		return parsers.AbortToProtobuf(msg)
	case messages.MessageTypeGoodbye:
		msg := message.(*messages.GoodBye)
		return parsers.GoodbyeToProtobuf(msg)
	case messages.MessageTypeRegister:
		msg := message.(*messages.Register)
		return parsers.RegisterToProtobuf(msg)
	case messages.MessageTypeRegistered:
		msg := message.(*messages.Registered)
		return parsers.RegisteredToProtobuf(msg)
	case messages.MessageTypeUnRegister:
		msg := message.(*messages.UnRegister)
		return parsers.UnregisterToProtobuf(msg)
	case messages.MessageTypeUnRegistered:
		msg := message.(*messages.UnRegistered)
		return parsers.UnregisteredToProtobuf(msg)
	case messages.MessageTypePublish:
		msg := message.(*messages.Publish)
		return parsers.PublishToProtobuf(msg)
	case messages.MessageTypePublished:
		msg := message.(*messages.Published)
		return parsers.PublishedToProtobuf(msg)
	case messages.MessageTypeEvent:
		msg := message.(*messages.Event)
		return parsers.EventToProtobuf(msg)
	case messages.MessageTypeCall:
		msg := message.(*messages.Call)
		return parsers.CallToProtobuf(msg)
	case messages.MessageTypeInvocation:
		msg := message.(*messages.Invocation)
		return parsers.InvocationToProtobuf(msg)
	case messages.MessageTypeYield:
		msg := message.(*messages.Yield)
		return parsers.YieldToProtobuf(msg)
	case messages.MessageTypeResult:
		msg := message.(*messages.Result)
		return parsers.ResultToProtobuf(msg)
	case messages.MessageTypeSubscribe:
		msg := message.(*messages.Subscribe)
		return parsers.SubscribeToProtobuf(msg)
	case messages.MessageTypeSubscribed:
		msg := message.(*messages.Subscribed)
		return parsers.SubscribedToProtobuf(msg)
	case messages.MessageTypeUnSubscribe:
		msg := message.(*messages.UnSubscribe)
		return parsers.UnsubscribeToProtobuf(msg)
	case messages.MessageTypeUnSubscribed:
		msg := message.(*messages.UnSubscribed)
		return parsers.UnsubscribedToProtobuf(msg)
	case messages.MessageTypeCancel:
		msg := message.(*messages.Cancel)
		return parsers.CancelToProtobuf(msg)
	case messages.MessageTypeInterrupt:
		msg := message.(*messages.Interrupt)
		return parsers.InterruptToProtobuf(msg)
	case messages.MessageTypeError:
		msg := message.(*messages.Error)
		return parsers.ErrorToProtobuf(msg)
	default:
		return nil, fmt.Errorf("unknown message type: %v", message.Type())
	}
}

func (p *ProtobufSerializer) Deserialize(bytes []byte) (messages.Message, error) {
	switch bytes[0] {
	case messages.MessageTypeHello:
		return parsers.ProtobufToHello(bytes[1:])
	case messages.MessageTypeWelcome:
		return parsers.ProtobufToWelcome(bytes[1:])
	case messages.MessageTypeChallenge:
		return parsers.ProtobufToChallenge(bytes[1:])
	case messages.MessageTypeAuthenticate:
		return parsers.ProtobufToAuthenticate(bytes[1:])
	case messages.MessageTypeGoodbye:
		return parsers.ProtobufToGoodbye(bytes[1:])
	case messages.MessageTypeCall:
		return parsers.ProtobufToCall(bytes[1:])
	case messages.MessageTypeInvocation:
		return parsers.ProtobufToInvocation(bytes[1:])
	case messages.MessageTypeYield:
		return parsers.ProtobufToYield(bytes[1:])
	case messages.MessageTypeResult:
		return parsers.ProtobufToResult(bytes[1:])
	case messages.MessageTypeRegister:
		return parsers.ProtobufToRegister(bytes[1:])
	case messages.MessageTypeRegistered:
		return parsers.ProtobufToRegistered(bytes[1:])
	case messages.MessageTypeUnRegister:
		return parsers.ProtobufToUnregister(bytes[1:])
	case messages.MessageTypeUnRegistered:
		return parsers.ProtobufToUnregistered(bytes[1:])
	case messages.MessageTypeAbort:
		return parsers.ProtobufToAbort(bytes[1:])
	case messages.MessageTypeCancel:
		return parsers.ProtobufToCancel(bytes[1:])
	case messages.MessageTypeInterrupt:
		return parsers.ProtobufToInterrupt(bytes[1:])
	case messages.MessageTypePublish:
		return parsers.ProtobufToPublish(bytes[1:])
	case messages.MessageTypePublished:
		return parsers.ProtobufToPublished(bytes[1:])
	case messages.MessageTypeEvent:
		return parsers.ProtobufToEvent(bytes[1:])
	case messages.MessageTypeSubscribe:
		return parsers.ProtobufToSubscribe(bytes[1:])
	case messages.MessageTypeSubscribed:
		return parsers.ProtobufToSubscribed(bytes[1:])
	case messages.MessageTypeUnSubscribe:
		return parsers.ProtobufToUnsubscribe(bytes[1:])
	case messages.MessageTypeUnSubscribed:
		return parsers.ProtobufToUnsubscribed(bytes[1:])
	case messages.MessageTypeError:
		return parsers.ProtobufToError(bytes[1:])
	default:
		return nil, fmt.Errorf("unknown message type: %v", bytes[0])
	}
}

func (p *ProtobufSerializer) Static() bool {
	return true
}
