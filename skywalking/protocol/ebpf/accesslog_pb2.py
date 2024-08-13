# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ebpf/accesslog.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ..common import Common_pb2 as common_dot_Common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14\x65\x62pf/accesslog.proto\x12\rskywalking.v3\x1a\x13\x63ommon/Common.proto\"\xf4\x01\n\x14\x45\x42PFAccessLogMessage\x12\x32\n\x04node\x18\x01 \x01(\x0b\x32$.skywalking.v3.EBPFAccessLogNodeInfo\x12\x36\n\nconnection\x18\x02 \x01(\x0b\x32\".skywalking.v3.AccessLogConnection\x12\x35\n\nkernelLogs\x18\x03 \x03(\x0b\x32!.skywalking.v3.AccessLogKernelLog\x12\x39\n\x0bprotocolLog\x18\x04 \x01(\x0b\x32$.skywalking.v3.AccessLogProtocolLogs\"\xdd\x01\n\x15\x45\x42PFAccessLogNodeInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x43\n\rnetInterfaces\x18\x02 \x03(\x0b\x32,.skywalking.v3.EBPFAccessLogNodeNetInterface\x12(\n\x08\x62ootTime\x18\x03 \x01(\x0b\x32\x16.skywalking.v3.Instant\x12\x13\n\x0b\x63lusterName\x18\x04 \x01(\t\x12\x32\n\x06policy\x18\x05 \x01(\x0b\x32\".skywalking.v3.EBPFAccessLogPolicy\"0\n\x13\x45\x42PFAccessLogPolicy\x12\x19\n\x11\x65xcludeNamespaces\x18\x01 \x03(\t\"I\n\x1d\x45\x42PFAccessLogNodeNetInterface\x12\r\n\x05index\x18\x01 \x01(\x05\x12\x0b\n\x03mtu\x18\x02 \x01(\x05\x12\x0c\n\x04name\x18\x03 \x01(\t\"\x96\x02\n\x13\x41\x63\x63\x65ssLogConnection\x12/\n\x05local\x18\x01 \x01(\x0b\x32 .skywalking.v3.ConnectionAddress\x12\x30\n\x06remote\x18\x02 \x01(\x0b\x32 .skywalking.v3.ConnectionAddress\x12(\n\x04role\x18\x03 \x01(\x0e\x32\x1a.skywalking.v3.DetectPoint\x12:\n\x07tlsMode\x18\x04 \x01(\x0e\x32).skywalking.v3.AccessLogConnectionTLSMode\x12\x36\n\x08protocol\x18\x05 \x01(\x0e\x32$.skywalking.v3.AccessLogProtocolType\"\x85\x01\n\x11\x43onnectionAddress\x12=\n\nkubernetes\x18\x01 \x01(\x0b\x32\'.skywalking.v3.KubernetesProcessAddressH\x00\x12&\n\x02ip\x18\x02 \x01(\x0b\x32\x18.skywalking.v3.IPAddressH\x00\x42\t\n\x07\x61\x64\x64ress\"z\n\x18KubernetesProcessAddress\x12\x13\n\x0bserviceName\x18\x01 \x01(\t\x12\x0f\n\x07podName\x18\x02 \x01(\t\x12\x15\n\rcontainerName\x18\x03 \x01(\t\x12\x13\n\x0bprocessName\x18\x04 \x01(\t\x12\x0c\n\x04port\x18\x05 \x01(\x05\"\'\n\tIPAddress\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\x05\"\xe0\x02\n\x12\x41\x63\x63\x65ssLogKernelLog\x12\x41\n\x07\x63onnect\x18\x01 \x01(\x0b\x32..skywalking.v3.AccessLogKernelConnectOperationH\x00\x12?\n\x06\x61\x63\x63\x65pt\x18\x02 \x01(\x0b\x32-.skywalking.v3.AccessLogKernelAcceptOperationH\x00\x12=\n\x05\x63lose\x18\x03 \x01(\x0b\x32,.skywalking.v3.AccessLogKernelCloseOperationH\x00\x12;\n\x04read\x18\x04 \x01(\x0b\x32+.skywalking.v3.AccessLogKernelReadOperationH\x00\x12=\n\x05write\x18\x05 \x01(\x0b\x32,.skywalking.v3.AccessLogKernelWriteOperationH\x00\x42\x0b\n\toperation\"Y\n\x15\x41\x63\x63\x65ssLogProtocolLogs\x12\x34\n\x04http\x18\x01 \x01(\x0b\x32$.skywalking.v3.AccessLogHTTPProtocolH\x00\x42\n\n\x08protocol\"\xb3\x02\n\x15\x41\x63\x63\x65ssLogHTTPProtocol\x12/\n\tstartTime\x18\x01 \x01(\x0b\x32\x1c.skywalking.v3.EBPFTimestamp\x12-\n\x07\x65ndTime\x18\x02 \x01(\x0b\x32\x1c.skywalking.v3.EBPFTimestamp\x12<\n\x07version\x18\x03 \x01(\x0e\x32+.skywalking.v3.AccessLogHTTPProtocolVersion\x12<\n\x07request\x18\x04 \x01(\x0b\x32+.skywalking.v3.AccessLogHTTPProtocolRequest\x12>\n\x08response\x18\x05 \x01(\x0b\x32,.skywalking.v3.AccessLogHTTPProtocolResponse\"\xd6\x01\n\x1c\x41\x63\x63\x65ssLogHTTPProtocolRequest\x12\x41\n\x06method\x18\x01 \x01(\x0e\x32\x31.skywalking.v3.AccessLogHTTPProtocolRequestMethod\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x1a\n\x12sizeOfHeadersBytes\x18\x03 \x01(\x04\x12\x17\n\x0fsizeOfBodyBytes\x18\x04 \x01(\x04\x12\x30\n\x05trace\x18\x05 \x01(\x0b\x32!.skywalking.v3.AccessLogTraceInfo\"h\n\x1d\x41\x63\x63\x65ssLogHTTPProtocolResponse\x12\x12\n\nstatusCode\x18\x01 \x01(\x05\x12\x1a\n\x12sizeOfHeadersBytes\x18\x03 \x01(\x04\x12\x17\n\x0fsizeOfBodyBytes\x18\x04 \x01(\x04\"\x8a\x01\n\x12\x41\x63\x63\x65ssLogTraceInfo\x12;\n\x08provider\x18\x01 \x01(\x0e\x32).skywalking.v3.AccessLogTraceInfoProvider\x12\x0f\n\x07traceId\x18\x02 \x01(\t\x12\x16\n\x0etraceSegmentId\x18\x03 \x01(\t\x12\x0e\n\x06spanId\x18\x04 \x01(\t\"\x92\x01\n\x1f\x41\x63\x63\x65ssLogKernelConnectOperation\x12/\n\tstartTime\x18\x01 \x01(\x0b\x32\x1c.skywalking.v3.EBPFTimestamp\x12-\n\x07\x65ndTime\x18\x02 \x01(\x0b\x32\x1c.skywalking.v3.EBPFTimestamp\x12\x0f\n\x07success\x18\x03 \x01(\x08\"\x80\x01\n\x1e\x41\x63\x63\x65ssLogKernelAcceptOperation\x12/\n\tstartTime\x18\x01 \x01(\x0b\x32\x1c.skywalking.v3.EBPFTimestamp\x12-\n\x07\x65ndTime\x18\x02 \x01(\x0b\x32\x1c.skywalking.v3.EBPFTimestamp\"\x90\x01\n\x1d\x41\x63\x63\x65ssLogKernelCloseOperation\x12/\n\tstartTime\x18\x01 \x01(\x0b\x32\x1c.skywalking.v3.EBPFTimestamp\x12-\n\x07\x65ndTime\x18\x02 \x01(\x0b\x32\x1c.skywalking.v3.EBPFTimestamp\x12\x0f\n\x07success\x18\x03 \x01(\x08\"\xff\x02\n\x1d\x41\x63\x63\x65ssLogKernelWriteOperation\x12/\n\tstartTime\x18\x01 \x01(\x0b\x32\x1c.skywalking.v3.EBPFTimestamp\x12-\n\x07\x65ndTime\x18\x02 \x01(\x0b\x32\x1c.skywalking.v3.EBPFTimestamp\x12;\n\x07syscall\x18\x03 \x01(\x0e\x32*.skywalking.v3.AccessLogKernelWriteSyscall\x12?\n\tl4Metrics\x18\x04 \x01(\x0b\x32,.skywalking.v3.AccessLogKernelWriteL4Metrics\x12?\n\tl3Metrics\x18\x05 \x01(\x0b\x32,.skywalking.v3.AccessLogKernelWriteL3Metrics\x12?\n\tl2Metrics\x18\x06 \x01(\x0b\x32,.skywalking.v3.AccessLogKernelWriteL2Metrics\"\xe0\x01\n\x1d\x41\x63\x63\x65ssLogKernelWriteL4Metrics\x12\x15\n\rtotalDuration\x18\x01 \x01(\x04\x12!\n\x19totalTransmitPackageCount\x18\x02 \x01(\x03\x12#\n\x1btotalRetransmitPackageCount\x18\x03 \x01(\x03\x12\x46\n\x12lossPackageMetrics\x18\x04 \x03(\x0b\x32*.skywalking.v3.AccessLogLossPackageMetrics\x12\x18\n\x10totalPackageSize\x18\x05 \x01(\x03\">\n\x1b\x41\x63\x63\x65ssLogLossPackageMetrics\x12\x10\n\x08location\x18\x01 \x01(\t\x12\r\n\x05\x63ount\x18\x02 \x01(\x05\"\xeb\x01\n\x1d\x41\x63\x63\x65ssLogKernelWriteL3Metrics\x12\x15\n\rtotalDuration\x18\x01 \x01(\x04\x12\x1a\n\x12totalLocalDuration\x18\x02 \x01(\x04\x12\x1b\n\x13totalOutputDuration\x18\x03 \x01(\x04\x12\x1c\n\x14totalResolveMACCount\x18\x05 \x01(\x04\x12\x1f\n\x17totalResolveMACDuration\x18\x06 \x01(\x04\x12\x1b\n\x13totalNetFilterCount\x18\x07 \x01(\x04\x12\x1e\n\x16totalNetFilterDuration\x18\x08 \x01(\x04\"\xaf\x01\n\x1d\x41\x63\x63\x65ssLogKernelWriteL2Metrics\x12\x15\n\rtotalDuration\x18\x01 \x01(\x04\x12\x0f\n\x07ifindex\x18\x02 \x01(\r\x12\"\n\x1atotalEnterQueueBufferCount\x18\x03 \x01(\x04\x12\x1e\n\x16totalReadySendDuration\x18\x04 \x01(\x04\x12\"\n\x1atotalNetDeviceSendDuration\x18\x05 \x01(\x04\"\xfa\x02\n\x1c\x41\x63\x63\x65ssLogKernelReadOperation\x12/\n\tstartTime\x18\x01 \x01(\x0b\x32\x1c.skywalking.v3.EBPFTimestamp\x12-\n\x07\x65ndTime\x18\x02 \x01(\x0b\x32\x1c.skywalking.v3.EBPFTimestamp\x12:\n\x07syscall\x18\x03 \x01(\x0e\x32).skywalking.v3.AccessLogKernelReadSyscall\x12>\n\tl2Metrics\x18\x04 \x01(\x0b\x32+.skywalking.v3.AccessLogKernelReadL2Metrics\x12>\n\tl3Metrics\x18\x05 \x01(\x0b\x32+.skywalking.v3.AccessLogKernelReadL3Metrics\x12>\n\tl4Metrics\x18\x06 \x01(\x0b\x32+.skywalking.v3.AccessLogKernelReadL4Metrics\"\xb3\x01\n\x1c\x41\x63\x63\x65ssLogKernelReadL2Metrics\x12\x0f\n\x07ifindex\x18\x01 \x01(\r\x12\x19\n\x11totalPackageCount\x18\x02 \x01(\r\x12\x18\n\x10totalPackageSize\x18\x03 \x01(\x04\x12#\n\x1btotalPackageToQueueDuration\x18\x04 \x01(\x04\x12(\n totalRcvPackageFromQueueDuration\x18\x05 \x01(\x04\"\xa9\x01\n\x1c\x41\x63\x63\x65ssLogKernelReadL3Metrics\x12\x15\n\rtotalDuration\x18\x01 \x01(\x04\x12\x19\n\x11totalRecvDuration\x18\x02 \x01(\x04\x12\x1a\n\x12totalLocalDuration\x18\x03 \x01(\x04\x12\x1b\n\x13totalNetFilterCount\x18\x04 \x01(\x04\x12\x1e\n\x16totalNetFilterDuration\x18\x05 \x01(\x04\"5\n\x1c\x41\x63\x63\x65ssLogKernelReadL4Metrics\x12\x15\n\rtotalDuration\x18\x01 \x01(\x04\"R\n\rEBPFTimestamp\x12\x34\n\x06offset\x18\x01 \x01(\x0b\x32\".skywalking.v3.EBPFOffsetTimestampH\x00\x42\x0b\n\ttimestamp\"%\n\x13\x45\x42PFOffsetTimestamp\x12\x0e\n\x06offset\x18\x01 \x01(\x04\"\x19\n\x17\x45\x42PFAccessLogDownstream*0\n\x1a\x41\x63\x63\x65ssLogConnectionTLSMode\x12\t\n\x05Plain\x10\x00\x12\x07\n\x03TLS\x10\x01*4\n\x1c\x41\x63\x63\x65ssLogHTTPProtocolVersion\x12\t\n\x05HTTP1\x10\x00\x12\t\n\x05HTTP2\x10\x01*8\n\x1a\x41\x63\x63\x65ssLogTraceInfoProvider\x12\n\n\x06Zipkin\x10\x00\x12\x0e\n\nSkyWalking\x10\x01*\x86\x01\n\"AccessLogHTTPProtocolRequestMethod\x12\x07\n\x03Get\x10\x00\x12\x08\n\x04Post\x10\x01\x12\x07\n\x03Put\x10\x02\x12\n\n\x06\x44\x65lete\x10\x03\x12\x08\n\x04Head\x10\x04\x12\t\n\x05Patch\x10\x05\x12\x0b\n\x07Options\x10\x06\x12\t\n\x05Trace\x10\x07\x12\x0b\n\x07\x43onnect\x10\x08*\x83\x01\n\x1b\x41\x63\x63\x65ssLogKernelWriteSyscall\x12\t\n\x05Write\x10\x00\x12\n\n\x06Writev\x10\x01\x12\x08\n\x04Send\x10\x02\x12\n\n\x06SendTo\x10\x03\x12\x0b\n\x07SendMsg\x10\x04\x12\x0c\n\x08SendMmsg\x10\x05\x12\x0c\n\x08SendFile\x10\x06\x12\x0e\n\nSendFile64\x10\x07*d\n\x1a\x41\x63\x63\x65ssLogKernelReadSyscall\x12\x08\n\x04Read\x10\x00\x12\t\n\x05Readv\x10\x01\x12\x08\n\x04Recv\x10\x02\x12\x0c\n\x08RecvFrom\x10\x03\x12\x0b\n\x07RecvMsg\x10\x04\x12\x0c\n\x08RecvMmsg\x10\x05*8\n\x15\x41\x63\x63\x65ssLogProtocolType\x12\x07\n\x03TCP\x10\x00\x12\n\n\x06HTTP_1\x10\x01\x12\n\n\x06HTTP_2\x10\x02\x32r\n\x14\x45\x42PFAccessLogService\x12Z\n\x07\x63ollect\x12#.skywalking.v3.EBPFAccessLogMessage\x1a&.skywalking.v3.EBPFAccessLogDownstream\"\x00(\x01\x42s\n3org.apache.skywalking.apm.network.ebpf.accesslog.v3P\x01Z:skywalking.apache.org/repo/goapi/collect/ebpf/accesslog/v3b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ebpf.accesslog_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n3org.apache.skywalking.apm.network.ebpf.accesslog.v3P\001Z:skywalking.apache.org/repo/goapi/collect/ebpf/accesslog/v3'
  _globals['_ACCESSLOGCONNECTIONTLSMODE']._serialized_start=4918
  _globals['_ACCESSLOGCONNECTIONTLSMODE']._serialized_end=4966
  _globals['_ACCESSLOGHTTPPROTOCOLVERSION']._serialized_start=4968
  _globals['_ACCESSLOGHTTPPROTOCOLVERSION']._serialized_end=5020
  _globals['_ACCESSLOGTRACEINFOPROVIDER']._serialized_start=5022
  _globals['_ACCESSLOGTRACEINFOPROVIDER']._serialized_end=5078
  _globals['_ACCESSLOGHTTPPROTOCOLREQUESTMETHOD']._serialized_start=5081
  _globals['_ACCESSLOGHTTPPROTOCOLREQUESTMETHOD']._serialized_end=5215
  _globals['_ACCESSLOGKERNELWRITESYSCALL']._serialized_start=5218
  _globals['_ACCESSLOGKERNELWRITESYSCALL']._serialized_end=5349
  _globals['_ACCESSLOGKERNELREADSYSCALL']._serialized_start=5351
  _globals['_ACCESSLOGKERNELREADSYSCALL']._serialized_end=5451
  _globals['_ACCESSLOGPROTOCOLTYPE']._serialized_start=5453
  _globals['_ACCESSLOGPROTOCOLTYPE']._serialized_end=5509
  _globals['_EBPFACCESSLOGMESSAGE']._serialized_start=61
  _globals['_EBPFACCESSLOGMESSAGE']._serialized_end=305
  _globals['_EBPFACCESSLOGNODEINFO']._serialized_start=308
  _globals['_EBPFACCESSLOGNODEINFO']._serialized_end=529
  _globals['_EBPFACCESSLOGPOLICY']._serialized_start=531
  _globals['_EBPFACCESSLOGPOLICY']._serialized_end=579
  _globals['_EBPFACCESSLOGNODENETINTERFACE']._serialized_start=581
  _globals['_EBPFACCESSLOGNODENETINTERFACE']._serialized_end=654
  _globals['_ACCESSLOGCONNECTION']._serialized_start=657
  _globals['_ACCESSLOGCONNECTION']._serialized_end=935
  _globals['_CONNECTIONADDRESS']._serialized_start=938
  _globals['_CONNECTIONADDRESS']._serialized_end=1071
  _globals['_KUBERNETESPROCESSADDRESS']._serialized_start=1073
  _globals['_KUBERNETESPROCESSADDRESS']._serialized_end=1195
  _globals['_IPADDRESS']._serialized_start=1197
  _globals['_IPADDRESS']._serialized_end=1236
  _globals['_ACCESSLOGKERNELLOG']._serialized_start=1239
  _globals['_ACCESSLOGKERNELLOG']._serialized_end=1591
  _globals['_ACCESSLOGPROTOCOLLOGS']._serialized_start=1593
  _globals['_ACCESSLOGPROTOCOLLOGS']._serialized_end=1682
  _globals['_ACCESSLOGHTTPPROTOCOL']._serialized_start=1685
  _globals['_ACCESSLOGHTTPPROTOCOL']._serialized_end=1992
  _globals['_ACCESSLOGHTTPPROTOCOLREQUEST']._serialized_start=1995
  _globals['_ACCESSLOGHTTPPROTOCOLREQUEST']._serialized_end=2209
  _globals['_ACCESSLOGHTTPPROTOCOLRESPONSE']._serialized_start=2211
  _globals['_ACCESSLOGHTTPPROTOCOLRESPONSE']._serialized_end=2315
  _globals['_ACCESSLOGTRACEINFO']._serialized_start=2318
  _globals['_ACCESSLOGTRACEINFO']._serialized_end=2456
  _globals['_ACCESSLOGKERNELCONNECTOPERATION']._serialized_start=2459
  _globals['_ACCESSLOGKERNELCONNECTOPERATION']._serialized_end=2605
  _globals['_ACCESSLOGKERNELACCEPTOPERATION']._serialized_start=2608
  _globals['_ACCESSLOGKERNELACCEPTOPERATION']._serialized_end=2736
  _globals['_ACCESSLOGKERNELCLOSEOPERATION']._serialized_start=2739
  _globals['_ACCESSLOGKERNELCLOSEOPERATION']._serialized_end=2883
  _globals['_ACCESSLOGKERNELWRITEOPERATION']._serialized_start=2886
  _globals['_ACCESSLOGKERNELWRITEOPERATION']._serialized_end=3269
  _globals['_ACCESSLOGKERNELWRITEL4METRICS']._serialized_start=3272
  _globals['_ACCESSLOGKERNELWRITEL4METRICS']._serialized_end=3496
  _globals['_ACCESSLOGLOSSPACKAGEMETRICS']._serialized_start=3498
  _globals['_ACCESSLOGLOSSPACKAGEMETRICS']._serialized_end=3560
  _globals['_ACCESSLOGKERNELWRITEL3METRICS']._serialized_start=3563
  _globals['_ACCESSLOGKERNELWRITEL3METRICS']._serialized_end=3798
  _globals['_ACCESSLOGKERNELWRITEL2METRICS']._serialized_start=3801
  _globals['_ACCESSLOGKERNELWRITEL2METRICS']._serialized_end=3976
  _globals['_ACCESSLOGKERNELREADOPERATION']._serialized_start=3979
  _globals['_ACCESSLOGKERNELREADOPERATION']._serialized_end=4357
  _globals['_ACCESSLOGKERNELREADL2METRICS']._serialized_start=4360
  _globals['_ACCESSLOGKERNELREADL2METRICS']._serialized_end=4539
  _globals['_ACCESSLOGKERNELREADL3METRICS']._serialized_start=4542
  _globals['_ACCESSLOGKERNELREADL3METRICS']._serialized_end=4711
  _globals['_ACCESSLOGKERNELREADL4METRICS']._serialized_start=4713
  _globals['_ACCESSLOGKERNELREADL4METRICS']._serialized_end=4766
  _globals['_EBPFTIMESTAMP']._serialized_start=4768
  _globals['_EBPFTIMESTAMP']._serialized_end=4850
  _globals['_EBPFOFFSETTIMESTAMP']._serialized_start=4852
  _globals['_EBPFOFFSETTIMESTAMP']._serialized_end=4889
  _globals['_EBPFACCESSLOGDOWNSTREAM']._serialized_start=4891
  _globals['_EBPFACCESSLOGDOWNSTREAM']._serialized_end=4916
  _globals['_EBPFACCESSLOGSERVICE']._serialized_start=5511
  _globals['_EBPFACCESSLOGSERVICE']._serialized_end=5625
# @@protoc_insertion_point(module_scope)
