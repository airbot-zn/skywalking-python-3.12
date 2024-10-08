# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: profile/Profile.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ..common import Command_pb2 as common_dot_Command__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15profile/Profile.proto\x12\rskywalking.v3\x1a\x14\x63ommon/Command.proto\"\\\n\x17ProfileTaskCommandQuery\x12\x0f\n\x07service\x18\x01 \x01(\t\x12\x17\n\x0fserviceInstance\x18\x02 \x01(\t\x12\x17\n\x0flastCommandTime\x18\x03 \x01(\x03\"\x83\x01\n\x0eThreadSnapshot\x12\x0e\n\x06taskId\x18\x01 \x01(\t\x12\x16\n\x0etraceSegmentId\x18\x02 \x01(\t\x12\x0c\n\x04time\x18\x03 \x01(\x03\x12\x10\n\x08sequence\x18\x04 \x01(\x05\x12)\n\x05stack\x18\x05 \x01(\x0b\x32\x1a.skywalking.v3.ThreadStack\"%\n\x0bThreadStack\x12\x16\n\x0e\x63odeSignatures\x18\x01 \x03(\t\"S\n\x17ProfileTaskFinishReport\x12\x0f\n\x07service\x18\x01 \x01(\t\x12\x17\n\x0fserviceInstance\x18\x02 \x01(\t\x12\x0e\n\x06taskId\x18\x03 \x01(\t2\x90\x02\n\x0bProfileTask\x12[\n\x16getProfileTaskCommands\x12&.skywalking.v3.ProfileTaskCommandQuery\x1a\x17.skywalking.v3.Commands\"\x00\x12M\n\x0f\x63ollectSnapshot\x12\x1d.skywalking.v3.ThreadSnapshot\x1a\x17.skywalking.v3.Commands\"\x00(\x01\x12U\n\x10reportTaskFinish\x12&.skywalking.v3.ProfileTaskFinishReport\x1a\x17.skywalking.v3.Commands\"\x00\x42\x97\x01\n5org.apache.skywalking.apm.network.language.profile.v3P\x01Z<skywalking.apache.org/repo/goapi/collect/language/profile/v3\xaa\x02\x1dSkyWalking.NetworkProtocol.V3b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'profile.Profile_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n5org.apache.skywalking.apm.network.language.profile.v3P\001Z<skywalking.apache.org/repo/goapi/collect/language/profile/v3\252\002\035SkyWalking.NetworkProtocol.V3'
  _globals['_PROFILETASKCOMMANDQUERY']._serialized_start=62
  _globals['_PROFILETASKCOMMANDQUERY']._serialized_end=154
  _globals['_THREADSNAPSHOT']._serialized_start=157
  _globals['_THREADSNAPSHOT']._serialized_end=288
  _globals['_THREADSTACK']._serialized_start=290
  _globals['_THREADSTACK']._serialized_end=327
  _globals['_PROFILETASKFINISHREPORT']._serialized_start=329
  _globals['_PROFILETASKFINISHREPORT']._serialized_end=412
  _globals['_PROFILETASK']._serialized_start=415
  _globals['_PROFILETASK']._serialized_end=687
# @@protoc_insertion_point(module_scope)
