
infile = 'D:\python_data\Rio_medals_table.csv'
fr = open(infile, 'r')
for line in fr:
    print(str(len(line)) + "<>" + line)

fr.close()


infile = 'D:\python_data\Rio_medals_table.csv'
outfile = 'D:\python_data\Rio_medals_table_out.csv'
fr = open(infile, 'r')
fw = open(outfile, 'w')
for line in fr:
    print(str(len(line)) + "<>" + line)
    fw.write(line)

fr.close()
fw.close()
