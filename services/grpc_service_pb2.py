# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpc_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12grpc_service.proto\x12\x0cgrpc_service\"\x12\n\x10ListFilesRequest\"\"\n\x11ListFilesResponse\x12\r\n\x05\x66iles\x18\x01 \x03(\t2[\n\x0bPeerService\x12L\n\tListFiles\x12\x1e.grpc_service.ListFilesRequest\x1a\x1f.grpc_service.ListFilesResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'grpc_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_LISTFILESREQUEST']._serialized_start=36
  _globals['_LISTFILESREQUEST']._serialized_end=54
  _globals['_LISTFILESRESPONSE']._serialized_start=56
  _globals['_LISTFILESRESPONSE']._serialized_end=90
  _globals['_PEERSERVICE']._serialized_start=92
  _globals['_PEERSERVICE']._serialized_end=183
# @@protoc_insertion_point(module_scope)
