# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: protobuf/register.proto
# Protobuf Python Version: 5.27.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    1,
    '',
    'protobuf/register.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from protobuf import options_pb2 as protobuf_dot_options__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17protobuf/register.proto\x1a\x16protobuf/options.proto\"z\n\x08Register\x12\x12\n\nrequest_id\x18\x01 \x01(\x03\x12\x11\n\tprocedure\x18\x02 \x01(\t\x12\x17\n\x0f\x64isclose_caller\x18\x03 \x01(\x08\x12\x17\n\x06invoke\x18\x04 \x01(\x0e\x32\x07.Invoke\x12\x15\n\x05match\x18\x05 \x01(\x0e\x32\x06.Matchb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protobuf.register_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_REGISTER']._serialized_start=51
  _globals['_REGISTER']._serialized_end=173
# @@protoc_insertion_point(module_scope)