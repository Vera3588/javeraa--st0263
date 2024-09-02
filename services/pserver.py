import subprocess

def start_rest_service():
    subprocess.Popen(['python', 'services/rest_service.py'])

def start_grpc_service():
    subprocess.Popen(['python', 'services/grpc_service.py'])

def start_mom_service():
    subprocess.Popen(['python', 'services/mom_service.py'])

if __name__ == '__main__':
    start_rest_service()
    start_grpc_service()
    start_mom_service()
