# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: logging/Logging.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ..common import Common_pb2 as common_dot_Common__pb2
from ..common import Command_pb2 as common_dot_Command__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15logging/Logging.proto\x12\rskywalking.v3\x1a\x13\x63ommon/Common.proto\x1a\x14\x63ommon/Command.proto\"\xea\x01\n\x07LogData\x12\x11\n\ttimestamp\x18\x01 \x01(\x03\x12\x0f\n\x07service\x18\x02 \x01(\t\x12\x17\n\x0fserviceInstance\x18\x03 \x01(\t\x12\x10\n\x08\x65ndpoint\x18\x04 \x01(\t\x12(\n\x04\x62ody\x18\x05 \x01(\x0b\x32\x1a.skywalking.v3.LogDataBody\x12\x31\n\x0ctraceContext\x18\x06 \x01(\x0b\x32\x1b.skywalking.v3.TraceContext\x12$\n\x04tags\x18\x07 \x01(\x0b\x32\x16.skywalking.v3.LogTags\x12\r\n\x05layer\x18\x08 \x01(\t\"\x9e\x01\n\x0bLogDataBody\x12\x0c\n\x04type\x18\x01 \x01(\t\x12&\n\x04text\x18\x02 \x01(\x0b\x32\x16.skywalking.v3.TextLogH\x00\x12&\n\x04json\x18\x03 \x01(\x0b\x32\x16.skywalking.v3.JSONLogH\x00\x12&\n\x04yaml\x18\x04 \x01(\x0b\x32\x16.skywalking.v3.YAMLLogH\x00\x42\t\n\x07\x63ontent\"\x17\n\x07TextLog\x12\x0c\n\x04text\x18\x01 \x01(\t\"\x17\n\x07JSONLog\x12\x0c\n\x04json\x18\x01 \x01(\t\"\x17\n\x07YAMLLog\x12\x0c\n\x04yaml\x18\x01 \x01(\t\"G\n\x0cTraceContext\x12\x0f\n\x07traceId\x18\x01 \x01(\t\x12\x16\n\x0etraceSegmentId\x18\x02 \x01(\t\x12\x0e\n\x06spanId\x18\x03 \x01(\x05\":\n\x07LogTags\x12/\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32!.skywalking.v3.KeyStringValuePair2R\n\x10LogReportService\x12>\n\x07\x63ollect\x12\x16.skywalking.v3.LogData\x1a\x17.skywalking.v3.Commands\"\x00(\x01\x42\x85\x01\n,org.apache.skywalking.apm.network.logging.v3P\x01Z3skywalking.apache.org/repo/goapi/collect/logging/v3\xaa\x02\x1dSkyWalking.NetworkProtocol.V3b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'logging.Logging_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n,org.apache.skywalking.apm.network.logging.v3P\001Z3skywalking.apache.org/repo/goapi/collect/logging/v3\252\002\035SkyWalking.NetworkProtocol.V3'
  _globals['_LOGDATA']._serialized_start=84
  _globals['_LOGDATA']._serialized_end=318
  _globals['_LOGDATABODY']._serialized_start=321
  _globals['_LOGDATABODY']._serialized_end=479
  _globals['_TEXTLOG']._serialized_start=481
  _globals['_TEXTLOG']._serialized_end=504
  _globals['_JSONLOG']._serialized_start=506
  _globals['_JSONLOG']._serialized_end=529
  _globals['_YAMLLOG']._serialized_start=531
  _globals['_YAMLLOG']._serialized_end=554
  _globals['_TRACECONTEXT']._serialized_start=556
  _globals['_TRACECONTEXT']._serialized_end=627
  _globals['_LOGTAGS']._serialized_start=629
  _globals['_LOGTAGS']._serialized_end=687
  _globals['_LOGREPORTSERVICE']._serialized_start=689
  _globals['_LOGREPORTSERVICE']._serialized_end=771
# @@protoc_insertion_point(module_scope)
