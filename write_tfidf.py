import linecache

def write_tfidf(path1, path2, path3, path4, fname):
    read_file(path1, path2, path4, fname)
    fix_line()
    write_file(path3)
    

def read_file(path1, path2, path4, fname):
    global target_line
    global word_line
    
    f1        = open(path2, 'r', encoding="utf-8")
    f2        = open(path4, 'r', encoding="utf-8")
    word_line = f1.readline()
    line      = f2.readline()
    count     = 1
    
    while line:
        
        if line == fname:
            break
            
        line   = f2.readline()
        count += 1
        
    target_line = linecache.getline(path1, count)
    f1.close()
    f2.close()
    
    
def fix_line():
    global target_line
    global word_line
    
    target_line = " ".join(target_line.split()).split(' ')
    word_line   = word_line\
                .replace("Dainariicoru" , "<=")\
                .replace("Syonariicoru" , ">=")\
                .replace("Icoru132"     , "==")\
                .replace("Noticoru"     , "!=")\
                .replace("Plusicoru"    , "+=")\
                .replace("Mainusicoru"  , "-=")\
                .replace("Kakeruicoru"  , "*=")\
                .replace("Pasenticoru"  , "%=")\
                .replace("Plusplus"     , "++")\
                .replace("Mainusmainus" , "--")\
                .replace("Katukatu"     , "&&")\
                .replace("Matawamatawa" , "||")\
                .replace("Mainussyonari", "->")\
                .replace("Kakeru"       , "*")\
                .replace("Pulas132"     , "+")\
                .replace("Mainus132"    , "-")\
                .replace("Waru132"      , "/")\
                .replace("Amari132"     , "%")\
                .replace("Dainyu132"    , "=")\
                .replace("Dainari132"   , "<")\
                .replace("Syonari132"   , ">")\
                .replace("And131"       , "&")\
                .replace("Bikxtukuri"   , "!")\
                .split(' ')


def write_file(path3):
    global target_line
    global word_line
    
    f    = open(path3, 'w', encoding="utf-8", newline='')
    size = len(word_line) - 1
    
    for i in range(size):
        
        if target_line[i] == "0.":
            continue
            
        f.write("{:.4f} {}\n".format(float(target_line[i]), word_line[i]))
    
    f.close()


target_line = ''
word_line   = ''