# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: language-agent/TracingCompat.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ..common import Command_pb2 as common_dot_Command__pb2
from ..language_agent import Tracing_pb2 as language__agent_dot_Tracing__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"language-agent/TracingCompat.proto\x1a\x14\x63ommon/Command.proto\x1a\x1clanguage-agent/Tracing.proto2\xaf\x01\n\x19TraceSegmentReportService\x12\x44\n\x07\x63ollect\x12\x1c.skywalking.v3.SegmentObject\x1a\x17.skywalking.v3.Commands\"\x00(\x01\x12L\n\rcollectInSync\x12 .skywalking.v3.SegmentCollection\x1a\x17.skywalking.v3.Commands\"\x00\x42\xab\x01\n:org.apache.skywalking.apm.network.language.agent.v3.compatP\x01ZAskywalking.apache.org/repo/goapi/collect/language/agent/v3/compat\xb8\x01\x01\xaa\x02$SkyWalking.NetworkProtocol.V3.Compatb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'language_agent.TracingCompat_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n:org.apache.skywalking.apm.network.language.agent.v3.compatP\001ZAskywalking.apache.org/repo/goapi/collect/language/agent/v3/compat\270\001\001\252\002$SkyWalking.NetworkProtocol.V3.Compat'
  _globals['_TRACESEGMENTREPORTSERVICE']._serialized_start=91
  _globals['_TRACESEGMENTREPORTSERVICE']._serialized_end=266
# @@protoc_insertion_point(module_scope)
