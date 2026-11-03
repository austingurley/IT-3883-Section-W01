# Program Name: Assignment4_ProgramA.py
# Course: IT3883/Section W01
# Student Name: Austin Gurley
# Assignment Number: Assignment 4
# Due Date: 11/06/2026
# Purpose: This program acts as the client. It prompts the user to type in
#          a string, sends that string over a TCP socket to Program B, then
#          waits for Program B's response and prints whatever it receives
#          (the original string converted to upper case) to the console.
# Resources used:
#   - Python 3 documentation, socket module:
#     https://docs.python.org/3/library/socket.html

import socket

# Connection settings (hard coded per the assignment)
# These must match the IP address and port used in Program B.
HOST = "127.0.0.1"
PORT = 45678
BUFFER_SIZE = 1024  # maximum number of bytes to read at one time


def main():
    # Prompt the user for the string to send
    message = input("Enter a string to send to Program B: ")

    # Create a TCP/IPv4 socket. The "with" block closes it automatically.
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:

        # Connect to Program B; show a helpful message if it isn't running
        try:
            client_socket.connect((HOST, PORT))
        except ConnectionRefusedError:
            print(f"Could not connect to {HOST}:{PORT}. "
                  "Make sure Program B is running first.")
            return

        # Encode the string into bytes and send it to Program B
        client_socket.sendall(message.encode("utf-8"))

        # Listen for the response from Program B and decode it to a string
        data = client_socket.recv(BUFFER_SIZE)
        response = data.decode("utf-8")

    # Print whatever was received from Program B
    print(f"Received from Program B: {response}")


# Run main() only when this file is executed directly
if __name__ == "__main__":
    main()
