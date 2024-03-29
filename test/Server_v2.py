import socket
import select
import time
import datetime
import os
 
class SocketServer:
    """ Simple socket server that listens to one single client. """
 
    def __init__(self, host = '192.168.0.100', port = 8000, indexfile = []):
        """ Initialize the server with a host and port to listen to. """
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.host = host
        self.port = port
        self.sock.bind((host, port))
        self.sock.listen(1)
        self.indexfile = indexfile
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' ' + 'Starting socket server (host {}, port {})'.format(self.host, self.port))

    def reinit(self):
        self.sock.listen(1)
 
    def close(self):
        """ Close the server socket. """
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' ' + 'Closing server socket (host {}, port {})'.format(self.host, self.port))
        if self.sock:
            self.sock.close()
            self.sock = None
 
    def run_server(self):
        """ Accept and handle an incoming connection. """
        #print('Starting socket server (host {}, port {})'.format(self.host, self.port))
 
        client_sock, client_addr = self.sock.accept()
 
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' ' + 'Client {} connected'.format(client_addr))
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' ' + 'Socket {} connected'.format(client_sock))

        #delete files in directory
        #mydir = 'test_data/'
        #filelist = [ f for f in os.listdir(mydir) if f.endswith(".csv") ]
        #for f in filelist:
        #    os.remove(os.path.join(mydir, f))

        #number of files in directory
        mydir = 'test_data/'
        #n_files = len(os.listdir(mydir))
        #print(f'number of files in the directory: {n_files}')
 
        stop = False
        #x = 1
        while not stop:

            time.sleep(1)

            if client_sock:

                """
                # Check if the client is still connected and if data is available:
                try:
                    rdy_read, rdy_write, sock_err = select.select([client_sock,], [], [])
                except select.error:
                    print('Select() failed on socket with {}'.format(client_addr))
                    return 1
 
                if len(rdy_read) > 0:
                    read_data = client_sock.recv(255)
                    # Check if socket has been closed
                    if len(read_data) == 0:
                        print('{} closed the socket.'.format(client_addr))
                        stop = True
                    else:
                        print('>>> Received: {}'.format(read_data.rstrip()))
                        if read_data.rstrip() == 'quit':
                            stop = True
                        else:
                            client_sock.send(b'cool data')
                """
                #if len(os.listdir(mydir)) > n_files:
                filelist = [ f for f in os.listdir(mydir) if f.endswith(".csv") ]
                #i = 1
                #print('Neue Files vorhanden')
                #print(filelist)
                for f in filelist:

                    #print(f'fileindex: {self.fileindex}')
                    
                    if f not in self.indexfile:

                    #if i > n_files:
                        file  = open(mydir+f, 'r')
                        message = file.read()
                        message_binary = str.encode(message)
                        #print(f'Neues File {f} wird gesendet')
                        try:
                            client_sock.send(message_binary)
                            self.indexfile.append(f)
                            print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' ' + f'file {f} has been sent to {client_addr}')
                        except:
                            stop = True
                        file.close()

                    #i += 1
                #print('Alle neuen Files wurden gesendet')
                #n_files = len(os.listdir(mydir))
                #print(f'number of files in the directory: {n_files}')

            
            else:
                print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' ' + "No client is connected, SocketServer can't receive data")
                stop = True
 
        # Close socket
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' ' + 'Closing connection with {}'.format(client_addr))
        client_sock.close()
        client_sock = None
        return 0
 
def main():
    try:
        mydir = 'test_data/'
        server = SocketServer()
        while True:
            server.run_server()
            server.reinit()
    except KeyboardInterrupt:
        #clean directory
        filelist = [ f for f in os.listdir(mydir) if f.endswith(".csv") ]
        for f in filelist:
            os.remove(os.path.join(mydir, f))
        print(' KeyboardInterrupt')
        server.close()
        server = None
 
if __name__ == "__main__":
    main()