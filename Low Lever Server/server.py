from socket import *
import socket 
import socket

#Path for primary files
file_1= r"C:\Users\joshu\Documents\Practice\django\clint and server\file_1"
file_2= r"C:\Users\joshu\Documents\Practice\django\clint and server\file_2"
file_3= r"C:\Users\joshu\Documents\Practice\django\clint and server\file_3"
file_4= r"C:\Users\joshu\Documents\Practice\django\clint and server\file_4"

FILES=[file_1, file_2, file_3, file_4] #lIST OF PRIMARY DOCUMENTS CLIENT CAN READ FROM

#Function for getting the ip address every time the programe is run for automation
def ip ():
    try:
        host_name=socket.gethostname()
        ip_address=socket.gethostbyname(host_name)
        return ip_address
    
    except socket.error as e:
        print (f"Error: {e}")
        return None

#Invocking function
domain=ip()

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Socket object

server.bind((domain, 80))#Bind is used to associate the socket to a specific network

server.listen (5)

try:



    while True:

        #Code for establishing a connection with the clint and reading request
        (clientsocket, adress)=server.accept() #Accepting the request

        recieve=clientsocket.recv(5000).decode() #Converting from utf-8 to bytes for storage
        
        piece=recieve.split("\n")#converts request to list
        if len(piece) > 0: #Checks if the request is empty
            
            #handling potential input errors
            piece[0]=piece[0].upper()
            piece[1]=piece[1].lower()

            print(piece[0]) #Returns the verb
            

        else:
            print("Request is empty")

        

        #Handling request if verb is OPTIONS
        try:

            if piece[0]== "OPTIONS":
                file_message="The following files are available: "
                interaction_message="You can do the following: Update files, Retrieve files and Create new files"

                for file_name in FILES:
                    clientsocket.sendall(file_message.encode())
                    clientsocket.sendall(file_name.encode())
                    clientsocket.sendall(interaction_message.encode())
                
                clientsocket.shutdown(SHUT_WR)
        
        except Exception as e:
            print(f"There was an issue with the OPTIONS method: {e}")



        #Handling request if verb is HEAD
        try:

            if piece[0]== "HEAD":
                head_data="""
                HTTP/1.1 with statuse code-200. Connection Achieved\r\n
                Allow: GET, OPTIONS, CONNECT, POST, UPDATE\r\n
                \r\n
                """
                clientsocket.shutdown(SHUT_WR)

        except Exception as e:
            print(f"There was an issue with the HEAD method: {e}")



        #Handling request if verb is POST
        try:

            if piece[0]== "POST":
                return_message=f"A new file has been created with the title {piece[0]}"
                FILES.append(piece[1])

                #Creating a new file to work on
                with open(piece[1], "x") as post_f:
                    pass

                #Writting on the content with the new file
                with open(piece[1], "w") as post_w:
                    for content in piece[3: ]:
                        post_w.write(content)

                clientsocket.sendall(return_message.encode())
                clientsocket.shutdown(SHUT_WR)

        except Exception as e:
            print(f"There was an issue with the POST method: {e}")



        #Handling request if verb is UPDATE
        try:

            if piece[0]=="UPDATE":

                #Updating the files in the list in the list
                for file in FILES:
                    piece_info = f"{file} is not in the file list. However, It has been added!"
                    final_statement="File has been updated! Any other changes?"
                
                    if piece[1] in FILES:
                        FILES[FILES.index(file)] = piece[1]

                    else:
                        FILES.append(piece[1])
                        clientsocket.sendall(piece_info.encode())
                        
                    #Updating the contents of the file    
                    with open (piece[1], "w") as f:
                        for content in piece[3: ]:
                            f.write(content)                    

                #Responding to updation statuse
                clientsocket.sendall(final_statement.encode())
                
                clientsocket.shutdown(SHUT_WR)
                        
        except Exception as e:
            print(f"There was an issue with the UPDATE method: {e}")



        #Handling request if verb is GET
        try:

            if piece[0]== "GET":

                if piece[1] in FILES:
                    with open(piece[1], "r") as f_get:
                        reader=f_get.readlines()

                        for line in reader:
                            clientsocket.sendall(line.encode())
            
            clientsocket.shutdown(SHUT_WR)

        except Exception as e:
            print(f"There was an issue with the GET method: {e}")



        #Handling request if verb is CONNECT
        try:
            
            if piece[0]=="CONNECT":
                connection_data="""
                HTTP/1.1. Statuse Code in range of 200-299; OK\r\n
                User-Agent: Wndows 64; x64\r\n\r\n
                Content-Type: File/txt\r\n\r\n
                """

                clientsocket.sendall(connection_data.encode())
                clientsocket.shutdown(SHUT_WR)
        
        except Exception as e:
            print(f"There was an issue with the CONNECT method: {e}")
    


    #Closing server when all operations are done



except ConnectionRefusedError as e:
    print(f"The Connection Server has an issue: {e}")



finally:
    server.close()