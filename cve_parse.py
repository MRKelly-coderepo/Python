def mainParse():
    import csv
    typeDict = {}
    #allitems.csv is downloadable from https://cve.mitre.org/data/downloads/allitems.csv
    with open('allitems.csv', encoding='ISO-8859-1') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            for word in row[2].split(" "):
                if regexParse(word):
                    line_count += 1
                #    print(f'{row[0]} - ' + word)
                    if word in typeDict:
                        typeDict[word] += 1
                    else:
                        typeDict[word] = 1
            
        print(f'Processed {line_count} lines.')
        new = sorted(typeDict.items(), key=lambda x: x[1], reverse=True)
        for item in new:
            if item[1] > 10:
                print(item[0], item[1])
        
def regexParse(word):
    import re
    pattern = r"\.[A-Za-z]{1,4}$"
    return re.match(pattern,word)

mainParse()