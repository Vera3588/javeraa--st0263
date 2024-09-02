import grpc
import grpc_service_pb2
import grpc_service_pb2_grpc

def get_files(peer_address):
    with grpc.insecure_channel(peer_address) as channel:
        stub = grpc_service_pb2_grpc.PeerServiceStub(channel)
        response = stub.ListFiles(grpc_service_pb2.ListFilesRequest())
        print(response.files)

if __name__ == '__main__':
    get_files('localhost:50051')
