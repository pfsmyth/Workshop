"""
Program Name : AbeatsB
Author       : Peter Smyth
Date written : 26/10/16
Description  : The program accepts two country codes as input from the user.
               Reads the Rio_medals_table.csv file to confirm that the countries exist and
               that the 2nd country has a lower positiob than the first.
               It then calculates how many extra medals the second team requires to beat the first
               

Inputs       : Rio_medals_table.csv
Outputs      : Reults printed to screen

Calls        : N/A
Is called by : N/A
"""

import sys

country_a = raw_input("Give country code of first team > ") 
country_b = raw_input("Give country code of second team > ")
pos_a = 0
pos_b = 0


g_a = 0
s_a = 0
b_a = 0
g_b = 0
s_b = 0
b_b = 0

fr = open('D:\python_data\Rio_medals_table.csv', 'r')
hline = fr.readline() # header line - ignore this

for line in fr :
    l = line.split(',')
    if l[1] == country_a :
        g_a = l[2]
        s_a = l[3]
        b_a = l[4]
        pos_a = l[0]
    if l[1] == country_b :
        g_b = l[2]
        s_b = l[3]
        b_b = l[4]
        pos_b = l[0]
        
fr.close()

if pos_a == 0 :
    print "First Team not found in table"
    sys.exit()
if pos_b == 0 :
    print "Second Team not found in table"
    sys.exit()
if pos_a > pos_b :
    print "Teams wrong way around?"
    sys.exit()
    

# set up variables

gd = int(g_a) - int(g_b)
sd = int(s_a) - int(s_b)
bd = int(b_a) - int(b_b)

gn = gd + 1
sn = sd + 1
bn = bd + 1
    
# useful for debugging, but not need for final version
#print(pos_a, pos_b)
#print (g_a, s_a, b_a)
#print (g_b, s_b, b_b)

# calculate and print medals needed.  Refer to flow chart Lesson10.jpg
if bd < 0 :
    if sd < 0 :
        if gd == 0 :
            pass
        else :
            print gd, "more Golds"
    else :
        if gd == 0 :
            print sd, "more Silvers"
        else :
            print gn, "more Golds"
            print gd, "more Golds and", sn, "more Silvers"
else :                                                           # bd > = 0
    if sd < 0 :
        if gd == 0 :
            pass
        else :  
            print gd, "more Golds"
    else :
        if gd == 0 :
            print sn, "more Silvers"
            print sd, "more Silvers and ", bn, "more Bronzes"
        else :
            print gn, "more Golds,"
            print gd, "more Golds,", sn, "more Silvers"
            print gd, "more Golds,", sd, "more Silvers and ", bn, "more Bronzes"
        
