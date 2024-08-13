# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: language-agent/CLRMetric.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ..common import Common_pb2 as common_dot_Common__pb2
from ..common import Command_pb2 as common_dot_Command__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1elanguage-agent/CLRMetric.proto\x12\rskywalking.v3\x1a\x13\x63ommon/Common.proto\x1a\x14\x63ommon/Command.proto\"j\n\x13\x43LRMetricCollection\x12)\n\x07metrics\x18\x01 \x03(\x0b\x32\x18.skywalking.v3.CLRMetric\x12\x0f\n\x07service\x18\x02 \x01(\t\x12\x17\n\x0fserviceInstance\x18\x03 \x01(\t\"\x86\x01\n\tCLRMetric\x12\x0c\n\x04time\x18\x01 \x01(\x03\x12\x1f\n\x03\x63pu\x18\x02 \x01(\x0b\x32\x12.skywalking.v3.CPU\x12 \n\x02gc\x18\x03 \x01(\x0b\x32\x14.skywalking.v3.ClrGC\x12(\n\x06thread\x18\x04 \x01(\x0b\x32\x18.skywalking.v3.ClrThread\"i\n\x05\x43lrGC\x12\x18\n\x10Gen0CollectCount\x18\x01 \x01(\x03\x12\x18\n\x10Gen1CollectCount\x18\x02 \x01(\x03\x12\x18\n\x10Gen2CollectCount\x18\x03 \x01(\x03\x12\x12\n\nHeapMemory\x18\x04 \x01(\x03\"\x8f\x01\n\tClrThread\x12&\n\x1e\x41vailableCompletionPortThreads\x18\x01 \x01(\x05\x12\x1e\n\x16\x41vailableWorkerThreads\x18\x02 \x01(\x05\x12 \n\x18MaxCompletionPortThreads\x18\x03 \x01(\x05\x12\x18\n\x10MaxWorkerThreads\x18\x04 \x01(\x05\x32\x62\n\x16\x43LRMetricReportService\x12H\n\x07\x63ollect\x12\".skywalking.v3.CLRMetricCollection\x1a\x17.skywalking.v3.Commands\"\x00\x42\x93\x01\n3org.apache.skywalking.apm.network.language.agent.v3P\x01Z:skywalking.apache.org/repo/goapi/collect/language/agent/v3\xaa\x02\x1dSkyWalking.NetworkProtocol.V3b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'language_agent.CLRMetric_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n3org.apache.skywalking.apm.network.language.agent.v3P\001Z:skywalking.apache.org/repo/goapi/collect/language/agent/v3\252\002\035SkyWalking.NetworkProtocol.V3'
  _globals['_CLRMETRICCOLLECTION']._serialized_start=92
  _globals['_CLRMETRICCOLLECTION']._serialized_end=198
  _globals['_CLRMETRIC']._serialized_start=201
  _globals['_CLRMETRIC']._serialized_end=335
  _globals['_CLRGC']._serialized_start=337
  _globals['_CLRGC']._serialized_end=442
  _globals['_CLRTHREAD']._serialized_start=445
  _globals['_CLRTHREAD']._serialized_end=588
  _globals['_CLRMETRICREPORTSERVICE']._serialized_start=590
  _globals['_CLRMETRICREPORTSERVICE']._serialized_end=688
# @@protoc_insertion_point(module_scope)
