def sort_tfidf(path1):
    read_file(path1)
    write_file(path1)
    
    
def read_file(path1):
    global data
    
    f1   = open(path1, 'r', encoding="utf-8")
    line = f1.readline()
    
    while line:
        data.append(line.split(' '))
        line = f1.readline()
        
    data = sorted(data, key = lambda x:(x[0], x[1]), reverse = True)
    f1.close()
        
        
def write_file(path1):
    global data
    
    f1   = open(path1, 'w', encoding="utf-8", newline='')
    size = len(data)
    
    for i in range(size):
    
        str_data = str(data[i])\
        .replace("\\n", '')\
        .replace('[', '')\
        .replace(']', '')\
        .replace(',', '')\
        .replace('\'', '')
        
        f1.write(str_data + "\n")
        
    f1.close()
        
data = []