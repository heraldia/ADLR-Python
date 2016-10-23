import time
def generateJsonFile(interval = 10, filename = "Phil_20160402_015844.csv" ):
    #filename = r'allIn2.csv'
    for line in open(filename):
        if line[0] in ['L','S'] and line[1] == ':':
            f_json = open (r'asr\allIn1.json','w')
            f_json.write(line)
            f_json.close()
            time.sleep(1.0 * interval / 100)
        if line[0] in ['O'] and line[1] == ':':
            f_json = open (r'asr\allIn1.json','w')
            lineE = line.split(',')
            if "2016" in lineE[2] :
                f_json.write(lineE[0]+","+lineE[1]+","+lineE[3]+","+lineE[4]+",")
            else :
                f_json.write(line)
            f_json.close()
            time.sleep(1.0 * interval / 100)

if __name__ == '__main__':
    generateJsonFile(10)
