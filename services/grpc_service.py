import grpc
from concurrent import futures
import grpc_service_pb2
import grpc_service_pb2_grpc

class PeerService(grpc_service_pb2_grpc.PeerServiceServicer):
    def ListFiles(self, request, context):
        try:
            lista_de_archivos = ["file1.txt", "file2.txt", "file3.txt"]
            if not lista_de_archivos:
                context.set_details("No files available.")
                context.set_code(grpc.StatusCode.NOT_FOUND)
                return grpc_service_pb2.ListFilesResponse()
            return grpc_service_pb2.ListFilesResponse(files=lista_de_archivos)
        except Exception as e:
            context.set_details(str(e))
            context.set_code(grpc.StatusCode.INTERNAL)
            return grpc_service_pb2.ListFilesResponse()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    grpc_service_pb2_grpc.add_PeerServiceServicer_to_server(PeerService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()