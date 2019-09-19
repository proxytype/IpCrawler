import socket
from joblib import Parallel, delayed

MAX = 4294967295
MIN = 0
PORTS = [21, 22, 80, 139, 443, 8080, 3389, 3306, 1433]

def convertIntToIp(ipInt):
    return '.'.join([str(int(ipHexField, 16)) for ipHexField in (map(''.join, zip(*[iter(str(hex(ipInt))[2:].zfill(8))]*2)))])

def makeConnection(ip, port):
    try:
        s = socket.socket()
        s.settimeout(3)
        s.connect((ip, port))
        s.sendall(b'')
        s.close()
        return "success"
    except socket.error as err:
        return "failure"


def threadRunner(i):
    ip = convertIntToIp(i)
    for x in PORTS:
        print("IPN:" + str(i) + " IP:" + ip + " Port:" + str(x) + " Status:" + makeConnection(ip, x))


if __name__ == '__main__':
    results = Parallel(n_jobs=10, backend="multiprocessing")(delayed(threadRunner)(i) for i in range(MIN, MAX))
