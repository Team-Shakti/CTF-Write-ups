Challenge name: Transforms
Convert me!

nc challenges.ctfd.io 30008
We have to do 100 conversion correctly. For example:

convert bytearray to hexdigest: [129, 141, 112, 176, 251, 106, 160, 102] @@@@@

convert integer to bytearray: 1639309969325418938 @@@@@

convert bytearray to integer: [55, 107, 189, 150, 85, 213, 147, 94] @@@@@
and so on


import binascii
from pwn import *

def parse_message(message):
    try:
        message = message.replace(b"convert", b"").strip()
        message = message.replace(b" @@@@@", b"").strip()
        base_a = message.split(b"to")[0].replace(b"convert", b"").strip()
        base_b = message.split(b"to")[1].split(b":")[0].strip()
        pivot = (f"{base_b.decode()}:").encode()
        value = message.split(pivot)[-1].strip()
        return base_a.decode(), base_b.decode(), value
    except Exception as e:
        print(f"Exception raised: {e} with message: {message}")

if __name__ == "__main__":

    conn = remote('challenges.ctfd.io', 30008)
    for i in range(0, 120):
        for j in range(0, 2):
            print(conn.recvline())

        line = conn.recvline()
        base_a, base_b, value = parse_message(line)
        print(line)
        print(f" Parsed to: from **{base_a}** to **{base_b}** ===> ", value)

        response = None
        #1 - Convert start types in byte. stop
        if base_a == "bytearray":
            bytes_value = bytes( bytearray ( eval ( value ) ) )
        elif base_a == "hexdigest":
            bytes_value = bytes.fromhex( value.decode() )  # TypeError: fromhex() argument must be str, not bytes
        elif base_a == "string":
            bytes_value = value.strip()  # (?)
        elif base_a == "integer":
            bytes_value = (int(value)).to_bytes(8, 'big')

        #2 - Convert byte from what you want.
        if base_b == "bytearray":
            response = str( list( bytearray(bytes_value) ) )
        elif base_b == "hexdigest":
            response = bytes_value.hex()
        elif base_b == "string":
            response = bytes_value.strip()
        elif base_b == "integer":
            response = str( int.from_bytes(bytes_value, byteorder='big', signed=False) )

        if response is not None:
            print(b"Going to send response ===> ", response)
            conn.send(response)
            conn.send(b"\n")
            print(b"Response from challenge: " + conn.recvline())
            print(conn.recvline())
            print(f"\n {i+1} ===================================\n")
        else:
            print("No response was provided")

