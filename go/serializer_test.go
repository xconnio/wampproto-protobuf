package wampprotobuf_test

import (
	"testing"

	"github.com/stretchr/testify/require"

	"github.com/xconnio/wampproto-go/messages"
	wampprotobuf "github.com/xconnio/wampproto-protobuf/go"
)

func TestSerializer(t *testing.T) {
	serializer := &wampprotobuf.ProtobufSerializer{}
	//serializer = &serializers.CBORSerializer{}
	args := []any{"hello", "test"}
	kwArgs := map[string]any{"first": "ok"}
	call := messages.NewCall(1, nil, "foo.bar", args, kwArgs)
	callData, err := serializer.Serialize(call)
	require.NoError(t, err)
	require.NotNil(t, callData)

	yield := messages.NewYield(1, nil, args, kwArgs)
	yieldData, err := serializer.Serialize(yield)
	require.NoError(t, err)
	require.NotNil(t, yieldData)

	for i := 0; i < 100000; i++ {
		c, err := serializer.Deserialize(callData)
		require.NoError(t, err)

		iCall := c.(*messages.Call)
		inv := messages.NewInvocation(iCall.RequestID(), 899, nil, call.Args(), call.KwArgs())
		_, _ = serializer.Serialize(inv)

		y, err := serializer.Deserialize(yieldData)
		require.NoError(t, err)
		require.NotNil(t, y)
		iYield := y.(*messages.Yield)

		result := messages.NewResult(iYield.RequestID(), nil, iYield.Args(), iYield.KwArgs())
		data, err := serializer.Serialize(result)
		require.NoError(t, err)
		require.NotNil(t, data)
	}
}
