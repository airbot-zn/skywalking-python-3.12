# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: browser/BrowserPerfCompat.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ..common import Command_pb2 as common_dot_Command__pb2
from ..browser import BrowserPerf_pb2 as browser_dot_BrowserPerf__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x62rowser/BrowserPerfCompat.proto\x1a\x14\x63ommon/Command.proto\x1a\x19\x62rowser/BrowserPerf.proto2\xb3\x01\n\x12\x42rowserPerfService\x12L\n\x0f\x63ollectPerfData\x12\x1e.skywalking.v3.BrowserPerfData\x1a\x17.skywalking.v3.Commands\"\x00\x12O\n\x10\x63ollectErrorLogs\x12\x1e.skywalking.v3.BrowserErrorLog\x1a\x17.skywalking.v3.Commands\"\x00(\x01\x42\xab\x01\n:org.apache.skywalking.apm.network.language.agent.v3.compatP\x01ZAskywalking.apache.org/repo/goapi/collect/language/agent/v3/compat\xb8\x01\x01\xaa\x02$SkyWalking.NetworkProtocol.V3.Compatb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'browser.BrowserPerfCompat_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n:org.apache.skywalking.apm.network.language.agent.v3.compatP\001ZAskywalking.apache.org/repo/goapi/collect/language/agent/v3/compat\270\001\001\252\002$SkyWalking.NetworkProtocol.V3.Compat'
  _globals['_BROWSERPERFSERVICE']._serialized_start=85
  _globals['_BROWSERPERFSERVICE']._serialized_end=264
# @@protoc_insertion_point(module_scope)
