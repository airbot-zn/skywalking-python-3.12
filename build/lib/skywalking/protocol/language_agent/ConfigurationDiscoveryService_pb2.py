# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: language-agent/ConfigurationDiscoveryService.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ..common import Command_pb2 as common_dot_Command__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2language-agent/ConfigurationDiscoveryService.proto\x12\rskywalking.v3\x1a\x14\x63ommon/Command.proto\"9\n\x18\x43onfigurationSyncRequest\x12\x0f\n\x07service\x18\x01 \x01(\t\x12\x0c\n\x04uuid\x18\x02 \x01(\t2z\n\x1d\x43onfigurationDiscoveryService\x12Y\n\x13\x66\x65tchConfigurations\x12\'.skywalking.v3.ConfigurationSyncRequest\x1a\x17.skywalking.v3.Commands\"\x00\x42\x98\x01\n3org.apache.skywalking.apm.network.language.agent.v3P\x01Z?skywalking.apache.org/repo/goapi/collect/agent/configuration/v3\xaa\x02\x1dSkyWalking.NetworkProtocol.V3b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'language_agent.ConfigurationDiscoveryService_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n3org.apache.skywalking.apm.network.language.agent.v3P\001Z?skywalking.apache.org/repo/goapi/collect/agent/configuration/v3\252\002\035SkyWalking.NetworkProtocol.V3'
  _globals['_CONFIGURATIONSYNCREQUEST']._serialized_start=91
  _globals['_CONFIGURATIONSYNCREQUEST']._serialized_end=148
  _globals['_CONFIGURATIONDISCOVERYSERVICE']._serialized_start=150
  _globals['_CONFIGURATIONDISCOVERYSERVICE']._serialized_end=272
# @@protoc_insertion_point(module_scope)
