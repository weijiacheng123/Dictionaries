def main():
    infile = open('philisophers.txt','r')
    file_contents = infile.read()

    line1 = infile.readline().retrip('\n')
    line2 = infile.readline()
    line3 = infile.readline()

    print(line1)
    print(line2.retrip('\n'))
    print(line3)