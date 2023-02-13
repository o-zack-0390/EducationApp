def bsg(path1, path2, path3):
    read_file(path3)
    write_file(path1, path2)


def read_file(path3):
    global word_list
    global symbol_list
    
    f1   = open(path3, 'r', encoding="utf-8")
    line = f1.readline()
    
    while line:
    
        s_line = line.split(' ')[1].replace("\n", '')
    
        if symbol_search(s_line) == 1:
            symbol_list.append(s_line)
            
        else:
            word_list.append(s_line)
            
        line = f1.readline()
            
    f1.close()
    
    
def symbol_search(line):
    global s_list
    
    for _str in s_list:
    
        if line == _str:
            return 1
            
    return 0
    
    
def write_file(path1, path2):
    global word_list
    global symbol_list
    
    f1 = open(path1, 'w', encoding="utf-8", newline='')
    f2 = open(path2, 'w', encoding="utf-8", newline='')
    
    for word in word_list:
        f1.write(word + "\n")
        
    for symbol in symbol_list:
        f2.write(symbol + "\n")


s_list = [                                                    \
					' ', ',', ';', '\t', '\n', '=',           \
					'[', ']', '(', ')' , '{' , '}',           \
					"<=", ">=", "==", "!=",                   \
					"+=", "-=", "*=", "/=", "%=", "++", "--", \
					"&&", "||",                               \
					"->", '#', '"', '\'',                     \
					'*', '+', '-', '*', '/', '%',             \
					'<', '>',                                 \
					'.', '&', '|', '?',                       \
					]
                    
word_list   = []
symbol_list = []