# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from ..common import Command_pb2 as common_dot_Command__pb2
from ..language_agent import Meter_pb2 as language__agent_dot_Meter__pb2


class MeterReportServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.collect = channel.stream_unary(
                '/MeterReportService/collect',
                request_serializer=language__agent_dot_Meter__pb2.MeterData.SerializeToString,
                response_deserializer=common_dot_Command__pb2.Commands.FromString,
                )


class MeterReportServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def collect(self, request_iterator, context):
        """Meter data is reported in a certain period. The agent/SDK should report all collected metrics in this period through one stream.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MeterReportServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'collect': grpc.stream_unary_rpc_method_handler(
                    servicer.collect,
                    request_deserializer=language__agent_dot_Meter__pb2.MeterData.FromString,
                    response_serializer=common_dot_Command__pb2.Commands.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'MeterReportService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MeterReportService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def collect(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/MeterReportService/collect',
            language__agent_dot_Meter__pb2.MeterData.SerializeToString,
            common_dot_Command__pb2.Commands.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
