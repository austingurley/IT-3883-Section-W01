# Program Name: Assignment4_ProgramB.py
# Course: IT3883/Section W01
# Student Name: Austin Gurley
# Assignment Number: Assignment 4
# Due Date: 11/06/2026
# Purpose: This program acts as the server. It listens on a hard-coded IP
#          address and port for a connection from Program A, receives a
#          string, converts that string to all upper case, and sends the
#          converted string back to Program A.
# Resources used:
#   - Python 3 documentation, socket module:
#     https://docs.python.org/3/library/socket.html
#   - Python 3 documentation, str.upper():
#     https://docs.python.org/3/library/stdtypes.html#str.upper

import socket

# Connection settings (hard coded per the assignment)
# 127.0.0.1 is the local machine, so both programs run on one PC.
# Port 45678 is above 40000, so it should not be in use.
HOST = "127.0.0.1"
PORT = 45678
BUFFER_SIZE = 1024  # maximum number of bytes to read at one time


def main():
    # Create a TCP/IPv4 socket. The "with" block closes it automatically.
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:

        # Allow the port to be reused right away if the program is restarted
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # Bind the socket to the IP address and port, then start listening
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)
        print(f"Program B is listening on {HOST}:{PORT}...")

        # Wait (block) until Program A connects
        conn, addr = server_socket.accept()

        with conn:
            print(f"Connected to Program A at {addr[0]}:{addr[1]}")

            # Receive the data from Program A and decode bytes into a string
            data = conn.recv(BUFFER_SIZE)
            received_text = data.decode("utf-8")
            print(f"Received: {received_text}")

            # Convert the received string to all upper case
            upper_text = received_text.upper()

            # Encode the string back into bytes and send it to Program A
            conn.sendall(upper_text.encode("utf-8"))
            print(f"Sent back: {upper_text}")

    print("Connection closed. Program B is ending.")


# Run main() only when this file is executed directly
if __name__ == "__main__":
    main()
