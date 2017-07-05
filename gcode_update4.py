#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
import os
import sys
import re

if (len(sys.argv)!= 2):
    print "need file name"
    exit()

infile =  open(sys.argv[1], 'r')
outfile = "new_" + str(sys.argv[1]) 
outfile = open(outfile, 'w')

last_x = 0
last_e = 0
new_e = 0

insert_line1 = ";Five lines added for thermograph - to hide extruder from view\n"
insert_line2start = "G1 E"
insert_line2end = " F1800\n"
insert_line3 = "G0 X80.000\n"
insert_line4 = "G0 Y160.000\n"
insert_line5 = "G0 Z10.000\n"
insert_line6 = "G04 P20000\n"
insert_linestart7 = "G0 X"
insert_linestart8 = "G0 Y"
insert_linestart9 = "G0 Z"
insert_line10start = "G1 E" 
insert_line10end = " F1800\n" 

for line in infile:
    match1 = re.search(r"G0 F10500 .*X([0-9]+\.[0-9]+) Y([0-9\.]+) Z([0-9\.]+)", line)
    match2 = re.search(r"G.*X[0-9]+\.[0-9]+ Y[0-9\.]+ E([0-9\.]+)", line)
    if(match2 is not None):
        last_e = float(match2.group(1)) - 4.0 
        new_e =  last_e + 4.0 
    if(match1 is not None):
	outfile.write(line)
        last_x = match1.group(1)
        last_y = match1.group(2)
        last_z = float(match1.group(3))
        new_z =  last_z + 50 
        insert_line2 = insert_line2start + str(last_e) + insert_line2end
        insert_line7 = insert_linestart7 + str(last_x) + "\n"
        insert_line8 = insert_linestart8 + str(last_y) + "\n"
        insert_line9= insert_linestart9 + str(last_z) + "\n"
        insert_line10 = insert_line10start + str(new_e) + insert_line10end
        outfile.write(insert_line1)
        outfile.write(insert_line2)
        outfile.write(insert_line3)
        outfile.write(insert_line4)
        outfile.write(insert_line6)
        outfile.write(insert_line7)
        outfile.write(insert_line8)
        outfile.write(insert_line10)
    else:     
        outfile.write(line)

infile.close()
outfile.close()
