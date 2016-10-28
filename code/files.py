# read a file and print the length of each line and its contents
infile = 'D:\python_data\Rio_medals_table.csv'
fr = open(infile, 'r')
for line in fr:
    print(str(len(line)) + "<>" + line)

fr.close()

# read a file and write each line to a different file
infile = 'D:\python_data\Rio_medals_table.csv'
outfile = 'D:\python_data\Rio_medals_table_out.csv'
fr = open(infile, 'r')
fw = open(outfile, 'w')

for line in fr:
    # this is where your main processing goes
    # that changes the input to produce the output
    fw.write(line)

fr.close()
fw.close()


