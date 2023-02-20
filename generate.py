from random import shuffle
import streamlit as st
import re

def generate(_path1, _path2, _path3, _path4):
    global bsg_list
    global bsg2_list
    global marker1
    global marker2
    global path1
    global path2
    global path3
    global path4
    
    path1 = _path1
    path2 = _path2
    path3 = _path3
    path4 = _path4
    
    read_file()
    print_ans()
    generate_blank(bsg2_list, marker2)
    generate_blank(bsg_list , marker1)
    print_blank()
    print_code()

    st.download_button(
    label     = 'ファイルをダウンロード',
    data      = ''.join(code_list),
    file_name ='prob.c',
    mime      ='c'
    )


def read_file():
	global code_list
	global bsg_list
	global bsg2_list
	global path1
	global path2
	global path3
	global path4
	
#   ans.c
	f1    = open(path1, 'r', encoding = "utf-8")
	line1 = f1.readline()

	while line1:
		code_list.append(line1)
		line1 = f1.readline()
	f1.close()
	
#   bsg.txt
	f2    = open(path3, 'r', encoding = "utf-8")
	line2 = f2.readline()

	while line2:
		line2 = line2.replace("\n",'')
		bsg_list.append(line2)
		line2 = f2.readline()
	f2.close()
	
#   bsg2.txt
	f3    = open(path4, 'r', encoding = "utf-8")
	line3 = f3.readline()

	while line3:
		line3 = line3.replace("\n",'')
		bsg2_list.append(line3)
		line3 = f3.readline()
	f3.close()
	
	bsg_list  = bsg_list[:int(len(bsg_list)/2)]
	bsg2_list = bsg2_list[:int(len(bsg2_list)/2)+1]


# 正解プログラムを表示
def print_ans():
	global code_list

	sorce = ''

	for line in code_list:
		sorce += line

	with st.expander("ソースコード"):
		st.code(sorce)


# 空欄を生成する
def generate_blank(bsg_list, marker):
	global code_list
	global rand_list
	global bi_list
	global bs_list
	
	order     = 0
	bsg_size  = len(bsg_list)
	code_size = len(code_list)
	rand_list = list(range(code_size))
	shuffle(rand_list)
	
	if marker == "/* ○ ○ ○ */":
		order = 1
	
#	bsg.txtの行数まで繰り返し
	for i in range(bsg_size):
		bsg_line   = bsg_list[i]
		bsg_length = len(bsg_line)
		
#		ソースコード行数まで繰り返し
		for j in range(code_size):
			index     = rand_list[j]
			code_line = code_list[index]
			pos       = code_line.find(bsg_line)
			
#			変換対象がある       空欄が生成されてない
			if (-1 < pos) and (index not in bi_list):
			
				if escape(code_line) == 0 :
					code_line = code_line.replace(bsg_line, marker)
					
					if order == 0:
						pre_str  = word_blank_checker(code_line, bsg_line)
						this_str = ''

						while True:
							this_str = word_blank_checker(pre_str, bsg_line)
							if pre_str == this_str:
								break
							pre_str = this_str
						
						code_list[index] = this_str
						
					else:
						code_list[index] = symbol_blank_checker(code_line, bsg_line)
					
					if marker in code_list[index]:
						bi_list.append(index)
						bs_list.append(bsg_line)
						break
	

# 不適切な空欄を解除する
def word_blank_checker(line, target):
	start_pos  = line.find("/*")
	end_pos    = line.find("*/")
	line_size  = len(line)
	
	if end_pos < start_pos:
		end_pos    = line.find("*/",start_pos,line_size)
	
	while (start_pos != -1) and (end_pos != -1):
		flag = 0
		
#		最初の変数が空欄の場合
		if start_pos == 0:
			end_str = line[end_pos+2]
			
#			*/ の次が文字か数字
			if (end_str.isalpha() == True) or (end_str.isdigit() == True):
				flag = 1
			
# 			後の文字が _
			elif end_str == '_':
				flag = 1
			
#			空欄を解除
			if flag == 1:
				line = target + line[end_pos+2:]
		
		else:
			start_str = line[start_pos-1]
			end_str   = line[end_pos+2]
			
#			/* の直前が文字か数字
			if (start_str.isalpha() == True) or (start_str.isdigit() == True):
				flag = 1
		
#			*/ の直後が文字か数字
			elif (end_str.isalpha() == True) or (end_str.isdigit()   == True):
				flag = 1
			
#			前後の文字どちらかが _ の場合
			elif (start_str == '_') or (end_str == '_'):
				flag = 1
			
#			空欄を解除
			if flag == 1:
				line = line[:start_pos] + target + line[end_pos+2:]
		
		line_size = len(line)
		start_pos = line.find("/*",end_pos+2,line_size)
		end_pos   = line.find("*/",end_pos+2,line_size)
		
		if end_pos < start_pos:
			end_pos = line.find("*/",start_pos,line_size)
	
	return line
	
	'''
	空欄が t の場合
	
	if(s/* □ □ □ */rcmp(/* □ □ □ */->word,/* □ □ □ */arge/* □ □ □ */->word)<0){
	                         ↑
					ここだけ残して他の空欄は解除する
					
	'''
	

# 不適切な空欄を解除する
def symbol_blank_checker(line, target):

	if "*//*" in line:
		return line.replace("/* ○ ○ ○ *//* ○ ○ ○ */","/* ○ ○ ○ */")
		
	else:
		return line


# 空欄にしない構文をバインドする
def escape(line):
	
#	コメント
	if "/*" in line:
		return 1
	
	elif "*/" in line:
		return 1
	
#	#define, printf などの定義
	elif '#' in line:
		return 1
	
	elif "printf" in line:
		return 1

#	関数名のプロトタイプ
	elif re.compile(r'(int|void|char|struct|double)( |\*)+[a-zA-Z0-9_]+\(').search(line):
		return 1

	elif re.compile(r'(int|void|char|struct|double)(( |\*)+[a-zA-Z0-9_]+)+\(').search(line):
		return 1

#	典型的なfor文宣言 for(i=0; i<size; i++) ← ここを空欄にするなら別の箇所を空欄にしたいので出題しない
	elif re.compile(r'for *\( *(int)* *(i|j) *= *[+-|a-z|A-Z|0-9]+ *; *(i|j) *< *[+-|a-z|A-Z|0-9]+ *; *(i|j) *\+\+ *\)').search(line):
		return 1
	
#	配列の要素の初期値 x = {1,2,3}; ← 空欄になると推測不可能なので出題しない
	elif re.compile(r'( *} *; *)$').search(line) != None :
		return 1
	
#	"文字列" ("Canada", "America", "Brazil") ← 空欄になると推測不可能なので出題しない
	elif ( '"' in line ) and ("scanf" not in line):
		return 1

	elif ( "'" in line ) and ("scanf" not in line):
		return 1
	
	else:
		return 0
	

# 空欄補充問題の作成
def write_prob(path):
	global code_list
	f = open(path, 'w', encoding = "utf-8", newline = '')
	
	for line in code_list:
		f.write(line)
		
	f.close()
	

# 空欄の「数・位置・置換文字」を表示
def print_blank():
	global bi_list
	global bs_list
	
	print_list = list(zip(bi_list, bs_list))
	print_size = len(print_list)
	
	print_list.sort(key = lambda x:x[0])
	bs_list.clear()
	bi_list.clear()
	
	with st.expander("空欄の行 : 計{}行".format(print_size)):
		for i in range(print_size):
			st.write("##### (行番号,置換文字) : ({},{})\n".format(print_list[i][0]+1, print_list[i][1]))


# ブラウザにソースコードを表示
def print_code():
	global code_list

	sorce = ''

	for line in code_list:
		sorce += line

	with st.expander("空欄補充問題"):
		st.code(sorce)


s_list = [                                           \
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

code_list = []
bsg_list  = []
bsg2_list = []
rand_list = []
tp_list   = []
bi_list   = []
bs_list   = []

marker1   = "/* □ □ □ */"
marker2   = "/* ○ ○ ○ */"

'''
実行コマンド
python generate.py
'''
