# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: browser/BrowserPerf.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ..common import Command_pb2 as common_dot_Command__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x62rowser/BrowserPerf.proto\x12\rskywalking.v3\x1a\x14\x63ommon/Command.proto\"\xe8\x02\n\x0f\x42rowserPerfData\x12\x0f\n\x07service\x18\x01 \x01(\t\x12\x16\n\x0eserviceVersion\x18\x02 \x01(\t\x12\x0c\n\x04time\x18\x03 \x01(\x03\x12\x10\n\x08pagePath\x18\x04 \x01(\t\x12\x14\n\x0credirectTime\x18\x05 \x01(\x05\x12\x0f\n\x07\x64nsTime\x18\x06 \x01(\x05\x12\x10\n\x08ttfbTime\x18\x07 \x01(\x05\x12\x0f\n\x07tcpTime\x18\x08 \x01(\x05\x12\x11\n\ttransTime\x18\t \x01(\x05\x12\x17\n\x0f\x64omAnalysisTime\x18\n \x01(\x05\x12\x0f\n\x07\x66ptTime\x18\x0b \x01(\x05\x12\x14\n\x0c\x64omReadyTime\x18\x0c \x01(\x05\x12\x14\n\x0cloadPageTime\x18\r \x01(\x05\x12\x0f\n\x07resTime\x18\x0e \x01(\x05\x12\x0f\n\x07sslTime\x18\x0f \x01(\x05\x12\x0f\n\x07ttlTime\x18\x10 \x01(\x05\x12\x15\n\rfirstPackTime\x18\x11 \x01(\x05\x12\x0f\n\x07\x66mpTime\x18\x12 \x01(\x05\"\x94\x02\n\x0f\x42rowserErrorLog\x12\x10\n\x08uniqueId\x18\x01 \x01(\t\x12\x0f\n\x07service\x18\x02 \x01(\t\x12\x16\n\x0eserviceVersion\x18\x03 \x01(\t\x12\x0c\n\x04time\x18\x04 \x01(\x03\x12\x10\n\x08pagePath\x18\x05 \x01(\t\x12.\n\x08\x63\x61tegory\x18\x06 \x01(\x0e\x32\x1c.skywalking.v3.ErrorCategory\x12\r\n\x05grade\x18\x07 \x01(\t\x12\x0f\n\x07message\x18\x08 \x01(\t\x12\x0c\n\x04line\x18\t \x01(\x05\x12\x0b\n\x03\x63ol\x18\n \x01(\x05\x12\r\n\x05stack\x18\x0b \x01(\t\x12\x10\n\x08\x65rrorUrl\x18\x0c \x01(\t\x12\x1a\n\x12\x66irstReportedError\x18\r \x01(\x08*R\n\rErrorCategory\x12\x08\n\x04\x61jax\x10\x00\x12\x0c\n\x08resource\x10\x01\x12\x07\n\x03vue\x10\x02\x12\x0b\n\x07promise\x10\x03\x12\x06\n\x02js\x10\x04\x12\x0b\n\x07unknown\x10\x05\x32\xb3\x01\n\x12\x42rowserPerfService\x12L\n\x0f\x63ollectPerfData\x12\x1e.skywalking.v3.BrowserPerfData\x1a\x17.skywalking.v3.Commands\"\x00\x12O\n\x10\x63ollectErrorLogs\x12\x1e.skywalking.v3.BrowserErrorLog\x1a\x17.skywalking.v3.Commands\"\x00(\x01\x42\x93\x01\n3org.apache.skywalking.apm.network.language.agent.v3P\x01Z:skywalking.apache.org/repo/goapi/collect/language/agent/v3\xaa\x02\x1dSkyWalking.NetworkProtocol.V3b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'browser.BrowserPerf_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n3org.apache.skywalking.apm.network.language.agent.v3P\001Z:skywalking.apache.org/repo/goapi/collect/language/agent/v3\252\002\035SkyWalking.NetworkProtocol.V3'
  _globals['_ERRORCATEGORY']._serialized_start=708
  _globals['_ERRORCATEGORY']._serialized_end=790
  _globals['_BROWSERPERFDATA']._serialized_start=67
  _globals['_BROWSERPERFDATA']._serialized_end=427
  _globals['_BROWSERERRORLOG']._serialized_start=430
  _globals['_BROWSERERRORLOG']._serialized_end=706
  _globals['_BROWSERPERFSERVICE']._serialized_start=793
  _globals['_BROWSERPERFSERVICE']._serialized_end=972
# @@protoc_insertion_point(module_scope)
