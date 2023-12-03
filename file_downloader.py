import socket 
import sys 

host = sys.argv[1]
textport = sys.argv[2]
file = sys.argv[3]

try: 
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error as e:
        print(f"error during socket creation : {e}")
        sys.exit(1)
try:
        port = int(textport)
except ValueError :
        try :
                port=socket.getservbyname(host,'tcp')
        except socket.error as e:
                print(f"port not found {e}")
                sys.exit(1)
try: 
        s.connect((host,port))
except socket.gaierror as e :
        print(f"error of server connection address : {e}")
        sys.exit(1)
except socket.error as e :
        print(f"connection error : {e}")
        sys.exit(1)
try:
       message = f"GET {file} HTTP/1.0\r\n\r\n"
       s.sendall(message.encode('utf-8')) 
except socket.error as e :
        print(f"data sending error : {e}")
        sys.exit(1)
while 1 :
        try:
                buf = s.recv(2048)
                buf = buf.decode('utf-8')
        except socket.error as e :
                print(f"data reception error : {e}")
                sys.exit(1)
        if not len(buf):
                break
        print(buf)        
                

