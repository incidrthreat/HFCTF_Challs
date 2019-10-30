#
# This script is used to read a gcode file and parse for F4800.000 lines and replace the 
# last three chars with a decimal convertion of each flag.
#
# The GCODE must have F4800.000 in the code to work.
#
# I.E. A == 065 and would replace F4800.000 with F4800.065

import sys, argparse, string

# Arguments
parser = argparse.ArgumentParser()
parser.add_argument("-fn", "--filename", action='store', dest='filename', help="Please enter the filename you want read.", required=True)
parser.add_argument("-fl","--flag", action='store', dest='flag',help="Please enter the flag you want to use.", required=True)
args = parser.parse_args()

# Variables
count = 0

# The Code Section
while count < len(args.flag):
    for i in args.flag:
        dec_Char = ord(i)
        s = open(args.filename).read()
        if len(str(dec_Char)) < 3:
            dec_Char = '%03d' % dec_Char
            s = s.replace('F1350.000', 'F1350.'+str(dec_Char), 1)
            f = open(args.filename, 'w')
            f.write(s)
            f.close()
            count += 1

        else:
            s = s.replace('F1350.000', 'F1350.'+str(dec_Char), 1)
            f = open(args.filename, 'w')
            f.write(s)
            f.close()
            count += 1