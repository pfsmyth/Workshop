"""
Program Name : tied
Author       : Peter Smyth
Date written : 18/10/16
Description  : The program reads the medals table and decides which countries tied based
               on medals won. The country codes are listed along with the medals won


Inputs       : Rio_medals_table.csv
Outputs      : Reults printed to screen

Calls        : N/A
Is called by : N/A
"""

tieList = []                                                  # a list to store the countries which have tied
tieflag = False
Position = 0
Gold = 0
Silver = 0
Bronze = 0
fr = open('D:\python_data\Rio_medals_table.csv', 'r')
hline = fr.readline()                                          # header line - ignore this
fline = fr.readline()
la = fline.split(',')
for line in fr :
    lb = line.split(',')
    if lb[2] == la[2] and lb[3] == la[3] and lb[4] == la[4] :  # we have a tie, index[2,3 and 4] are Gold, Silver and Bronze medals
        if tieflag :
            tielist.append(lb[1])
        else :                                                 # new tie
            tielist = []
            tielist.append(la[1])
            tielist.append(lb[1])
            tieflag = True
            Position = lb[0]
            Gold = lb[2]
            Silver = lb[3]
            Bronze = lb[4]
    else :                                                     # not a tie
        if tieflag :
            print ','.join(tielist),'Tied in position', Position,  'with', str(Gold), 'Golds', str(Silver), 'Silver', str(Bronze), 'Bronze medals'
            tieflag = False
    la = lb
fr.close()
