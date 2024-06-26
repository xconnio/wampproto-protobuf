// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.34.1
// 	protoc        v4.25.1
// source: protobuf/register.proto

package gen

import (
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	reflect "reflect"
	sync "sync"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

type Register struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	RequestId int64  `protobuf:"varint,1,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
	Procedure string `protobuf:"bytes,2,opt,name=procedure,proto3" json:"procedure,omitempty"`
	// options
	DiscloseCaller bool   `protobuf:"varint,3,opt,name=disclose_caller,json=discloseCaller,proto3" json:"disclose_caller,omitempty"`
	Invoke         Invoke `protobuf:"varint,4,opt,name=invoke,proto3,enum=Invoke" json:"invoke,omitempty"`
	Match          Match  `protobuf:"varint,5,opt,name=match,proto3,enum=Match" json:"match,omitempty"`
}

func (x *Register) Reset() {
	*x = Register{}
	if protoimpl.UnsafeEnabled {
		mi := &file_protobuf_register_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *Register) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Register) ProtoMessage() {}

func (x *Register) ProtoReflect() protoreflect.Message {
	mi := &file_protobuf_register_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Register.ProtoReflect.Descriptor instead.
func (*Register) Descriptor() ([]byte, []int) {
	return file_protobuf_register_proto_rawDescGZIP(), []int{0}
}

func (x *Register) GetRequestId() int64 {
	if x != nil {
		return x.RequestId
	}
	return 0
}

func (x *Register) GetProcedure() string {
	if x != nil {
		return x.Procedure
	}
	return ""
}

func (x *Register) GetDiscloseCaller() bool {
	if x != nil {
		return x.DiscloseCaller
	}
	return false
}

func (x *Register) GetInvoke() Invoke {
	if x != nil {
		return x.Invoke
	}
	return Invoke_single
}

func (x *Register) GetMatch() Match {
	if x != nil {
		return x.Match
	}
	return Match_exact
}

var File_protobuf_register_proto protoreflect.FileDescriptor

var file_protobuf_register_proto_rawDesc = []byte{
	0x0a, 0x17, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2f, 0x72, 0x65, 0x67, 0x69, 0x73,
	0x74, 0x65, 0x72, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x16, 0x70, 0x72, 0x6f, 0x74, 0x6f,
	0x62, 0x75, 0x66, 0x2f, 0x6f, 0x70, 0x74, 0x69, 0x6f, 0x6e, 0x73, 0x2e, 0x70, 0x72, 0x6f, 0x74,
	0x6f, 0x22, 0xaf, 0x01, 0x0a, 0x08, 0x52, 0x65, 0x67, 0x69, 0x73, 0x74, 0x65, 0x72, 0x12, 0x1d,
	0x0a, 0x0a, 0x72, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x5f, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01,
	0x28, 0x03, 0x52, 0x09, 0x72, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x49, 0x64, 0x12, 0x1c, 0x0a,
	0x09, 0x70, 0x72, 0x6f, 0x63, 0x65, 0x64, 0x75, 0x72, 0x65, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09,
	0x52, 0x09, 0x70, 0x72, 0x6f, 0x63, 0x65, 0x64, 0x75, 0x72, 0x65, 0x12, 0x27, 0x0a, 0x0f, 0x64,
	0x69, 0x73, 0x63, 0x6c, 0x6f, 0x73, 0x65, 0x5f, 0x63, 0x61, 0x6c, 0x6c, 0x65, 0x72, 0x18, 0x03,
	0x20, 0x01, 0x28, 0x08, 0x52, 0x0e, 0x64, 0x69, 0x73, 0x63, 0x6c, 0x6f, 0x73, 0x65, 0x43, 0x61,
	0x6c, 0x6c, 0x65, 0x72, 0x12, 0x1f, 0x0a, 0x06, 0x69, 0x6e, 0x76, 0x6f, 0x6b, 0x65, 0x18, 0x04,
	0x20, 0x01, 0x28, 0x0e, 0x32, 0x07, 0x2e, 0x49, 0x6e, 0x76, 0x6f, 0x6b, 0x65, 0x52, 0x06, 0x69,
	0x6e, 0x76, 0x6f, 0x6b, 0x65, 0x12, 0x1c, 0x0a, 0x05, 0x6d, 0x61, 0x74, 0x63, 0x68, 0x18, 0x05,
	0x20, 0x01, 0x28, 0x0e, 0x32, 0x06, 0x2e, 0x4d, 0x61, 0x74, 0x63, 0x68, 0x52, 0x05, 0x6d, 0x61,
	0x74, 0x63, 0x68, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_protobuf_register_proto_rawDescOnce sync.Once
	file_protobuf_register_proto_rawDescData = file_protobuf_register_proto_rawDesc
)

func file_protobuf_register_proto_rawDescGZIP() []byte {
	file_protobuf_register_proto_rawDescOnce.Do(func() {
		file_protobuf_register_proto_rawDescData = protoimpl.X.CompressGZIP(file_protobuf_register_proto_rawDescData)
	})
	return file_protobuf_register_proto_rawDescData
}

var file_protobuf_register_proto_msgTypes = make([]protoimpl.MessageInfo, 1)
var file_protobuf_register_proto_goTypes = []interface{}{
	(*Register)(nil), // 0: Register
	(Invoke)(0),      // 1: Invoke
	(Match)(0),       // 2: Match
}
var file_protobuf_register_proto_depIdxs = []int32{
	1, // 0: Register.invoke:type_name -> Invoke
	2, // 1: Register.match:type_name -> Match
	2, // [2:2] is the sub-list for method output_type
	2, // [2:2] is the sub-list for method input_type
	2, // [2:2] is the sub-list for extension type_name
	2, // [2:2] is the sub-list for extension extendee
	0, // [0:2] is the sub-list for field type_name
}

func init() { file_protobuf_register_proto_init() }
func file_protobuf_register_proto_init() {
	if File_protobuf_register_proto != nil {
		return
	}
	file_protobuf_options_proto_init()
	if !protoimpl.UnsafeEnabled {
		file_protobuf_register_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*Register); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_protobuf_register_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   1,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_protobuf_register_proto_goTypes,
		DependencyIndexes: file_protobuf_register_proto_depIdxs,
		MessageInfos:      file_protobuf_register_proto_msgTypes,
	}.Build()
	File_protobuf_register_proto = out.File
	file_protobuf_register_proto_rawDesc = nil
	file_protobuf_register_proto_goTypes = nil
	file_protobuf_register_proto_depIdxs = nil
}
