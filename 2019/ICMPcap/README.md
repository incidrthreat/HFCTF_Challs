Narrative:
- There is an unusually high amount of activity on one of our Linux servers.  Network analysis was cut down to these two hosts. Help us find the leaked data.

Notes to organizers:
- Only give players the narrative above and the Between2Hosts.pcap

Solve/walkthrough/guide: 
    The pcap is a capture of FTP, SSH, and ICMP traffic. 
    Many things stand out in this pcap.  There is clear-text FTP data with a few transfers.  There is some SSH traffic that isn't
    really readable, but the odd standing out packets of all the constant ICMP traffic.
    Once we narrow down the protocol and the data we want to pull run the following tshark command to grab the data and put it in a file.

    tshark -r dataeverywhere.pcapng -T fields -e "icmp.type" -e data.data -Y data.data >> data.txt

    The output looks like:
    icmp	8	feec0c0000000000302f30313031303130302f30313031303130302f30313031303130302f30313031303130302f3031
    icmp	0	feec0c0000000000302f30313031303130302f30313031303130302f30313031303130302f30313031303130302f3031
    icmp	8	d462050000000000302f30313130313030302f30313130313030302f30313130313030302f30313130313030302f3031
    icmp	0	d462050000000000302f30313130313030302f30313130313030302f30313130313030302f30313130313030302f3031        


    The first part is the protocol, the second is the ICMP type, and the third is the data sent in that packet.  You'll notice that
    the data is repeated.  This is the request (icmp type 8) and reply (icmp type 0) msg.
    
    More about this can be found here: https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol#Control_messages

    Using the command `cat data.txt | grep "icmp    8" >> data2.txt` will give us only the ICMP Request data.
    
    This new data file will look like:
    icmp	8	feec0c0000000000302f30313031303130302f30313031303130302f30313031303130302f30313031303130302f3031
    icmp	8	d462050000000000302f30313130313030302f30313130313030302f30313130313030302f30313130313030302f3031

    As we focus more on the third section (the data passed), we see that it is hex.  Converting this sample hex into 
    ascii looks like this:
    icmp	8	........0/01010100/01010100/01010100/01010100/01
    icmp	8	.b......0/01101000/01101000/01101000/01101000/01

    Again, we see a repeating pattern here split on 8 chars of binary data.  Converting this sample binary to ascii we get
    the following data:
    icmp	8	........0/T/T/T/T/01
    icmp	8	.b......0/h/h/h/h/01

    Luckily we dont have to do this by hand for all 113 lines.  Use the provided solve.py ;)

    Running the following command will provide a nice pretty output:
    cat data2.txt | python3 solve.py

    If all went well you should get the following output:
    There is a secret here, do not let anyone else see it.\n', '\n', 'The flag is: HF-2b4e41a1691ca72542f84e94fe695d06



FLAG:
- `HF-2b4e41a1691ca72542f84e94fe695d06`


SETUP if new flag is needed:
```
New PCAP of only the ICMP traffic:
    Files can be found in the build folder.
    - Run server.py  
    - Start wireshark. 
    - Run client.py with one of the examples below:
                python3 client.py --host "127.0.0.1" --msg "This is a secret msg"
                                or
                python3 client.py --host "127.0.0.1" --file .\secret.txt
```

