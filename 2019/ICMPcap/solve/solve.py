#! /bin/usr/env python3
# Author: incidrhreat@hackmethod.com
# 
# Purpose:      Reads in data from stdin and prints the output to stdout 
# 

import sys, binascii

def main():
    msg = []
    # read in from standard in
    for line in sys.stdin.readlines():
        # convert hex to ascii, line[11::] removes 'icmp    8   ' and remove all newlines
        unhexed = binascii.unhexlify(str(line[11::]).strip())
        
        # removes b' and / from the left side and ' from the right then splits 
        # each line by / and puts them in an array like so:
        # ['X\\xd9\\r\\x00\\x00\\x00\\x00\\x000', '01100010', '01100010', '01100010', '01100010', '01']
        splitting = str(unhexed).lstrip("b'").rstrip("'").lstrip("/").split("/")
        
        # assigns the 1 index to the binary variable
        binary = splitting[1]

        # converts the binary string into an int and then converts to ascii
        x = (chr(int(binary[:8], 2)))

        # appends x to the msg array
        msg.append(x)
    
    # prints the joined array 
    print(''.join(msg))

if __name__ == "__main__":
    main()
