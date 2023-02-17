from copy   import copy
from sys    import exit
import streamlit as st
import shutil
import os
import re
import zipfile


# pythonソースコードの属性
class Language_Node:
	
	def _init_(self):
		len   = None #ソースコード本文
		order = None #ソースコードの行番号



# ディレクトリを作成
def create_dir():

	input    = "/app/educationapp/marking/input"
	c_file   = "/app/educationapp/marking/input/c_file"
	txt_file = "/app/educationapp/marking/input/txt_file"
	output   = "/app/educationapp/marking/output"

	if os.path.exists(input):
		shutil.rmtree(input)

	if os.path.exists(c_file):
		shutil.rmtree(c_file)

	if os.path.exists(txt_file):
		shutil.rmtree(txt_file)

	if os.path.exists(output):
		shutil.rmtree(output)

	os.mkdir(input)
	os.mkdir(c_file)
	os.mkdir(txt_file)
	os.mkdir(output)



# ans.c を byte型 → str型に変更
def decode_ans_c():
	global upload_file1

	if upload_file1.name != "ans.c":
		st.write("エラー ans.c以外のファイルがアップロードされています")
		exit()

	f = open("/app/educationapp/marking/ans.c", 'w', encoding="utf-8", newline='')
	f.write(upload_file1.getvalue().decode('utf-8'))
	f.close()



def decode_ans_txt():
	global upload_file2

	if upload_file2.name != "ans.txt":
		st.write("エラー ans.txt以外のファイルがアップロードされています")
		exit()

	f = open("/app/educationapp/marking/ans.txt", 'w', encoding="utf-8", newline='')
	f.write(upload_file2.getvalue().decode('utf-8'))
	f.close()


def decode_prob_c():
	global upload_file3

	if upload_file3.name != "prob.c":
		st.write("エラー prob.c以外のファイルがアップロードされています")
		exit()

	f = open("/app/educationapp/marking/prob.c", 'w', encoding="utf-8", newline='')
	f.write(upload_file3.getvalue().decode('utf-8'))
	f.close()



def decode_student_c():
	global upload_file4
	global file1_list

	if upload_file4.name != "student_c.zip":
		st.write("エラー student_c.zip以外のファイルがアップロードされています")
		exit()

	with zipfile.ZipFile(upload_file4, 'r') as inputFile:
		inputFile.extractall("/app/educationapp/marking/input/c_file")

	file1_list  = os.listdir("/app/educationapp/marking/input/c_file")
	out1        = re.compile(r'^(100)')
	out2        = re.compile(r'.c')

	for f_name in file1_list:
		st.write(f_name)
		
		if out2.search(f_name) == None:
			st.write("エラー zipファイル中のファイルで検出。拡張子が「.c」ではないファイルがアップロードされています(student_c.zipファイル内のファイル拡張子を「.c」に変更してください)")
			exit()

		if out1.search(f_name) == None:
			st.write("エラー zipファイル中のファイルで検出。student_c.zip内のファイルを指定されたファイル名に変更してください")
			exit()



def decode_student_txt():
	global upload_file5
	global file2_list

	if upload_file5.name != "student_txt.zip":
		st.write("エラー student_txt.zip以外のファイルがアップロードされています")
		exit()

	with zipfile.ZipFile(upload_file5, 'r') as inputFile:
		inputFile.extractall("/app/educationapp/marking/input/txt_file")

	file2_list = os.listdir("/app/educationapp/marking/input/txt_file")
	out1       = re.compile(r'^(100)')
	out2       = re.compile(r'.c')

	for f_name in file1_list:
		st.write(f_name)

		if out2.search(f_name) == None:
			st.write("エラー 拡張子が「.txt」ではないファイルがアップロードされています(student_txt.zipファイル内のファイル拡張子を「.txt」に変更してください)")
			exit()

		if out1.search(f_name) == None:
			st.write("エラー student_txt.zip内のファイルを指定されたファイル名に変更してください")
			exit()



def check_student_num():
	global file1_list
	global file2_list

	file1_names = sorted(file1_list)
	file2_names = sorted(file2_list)
	size1       = len(file1_list)
	size2       = len(file2_list)

	st.write(file1_list)
	st.write(file2_list)

	if size1 != size2:
		st.write("エラー student_c.zip と student_txt.zip 内のファイル数が一致しません")
		exit()

	for i in range(size1):

		if file1_names[i].replace(".c", '') != file2_names[i].replace(".txt", ''):
			st.write("エラー student_c.zip と student_txt.zip 内のファイル名が一致しない組があります")
			exit()

	file1_list.clear()
	file2_list.clear()



# 模範プログラムを保存する
def read_ans(len_list):

#	正解プログラムを読み込む
	f     = open("/app/educationapp/marking/ans.c", 'r', encoding = "utf-8")
	line  = f.readline()
	order = 1

#	正解プログラムのソースコードを1行ごとに保存している
	while line:
		node = Language_Node()
		set_element(node,line,order)
		len_list.append(node)
		order += 1
		line   = f.readline()
		
	f.close()
	return order



def read_ans_exe():
	global ans_exe

	f     = open("/app/educationapp/marking/ans.txt", 'r', encoding = "utf-8")
	line  = f.readline()

	while line:
		ans_exe.append(line)
		line = f.readline()

	f.close()



# ソースコードの情報を1行ずつ記録している
def set_element(node, line, order):
	node.len   = line   
	node.order = order



# 参照するファイルを登録する
def input_file(path):

	list  = []
	files = os.listdir(path)
	
#	listdirでファイル一覧を取得している
	for f in files:
		
#		ファイルが存在するか確認する
		if os.path.isfile(os.path.join(path, f)):
		
#			変なファイルが無いか確認する
			if file_check(f) == 0:
				list.append(f)

			else:
				st.write(".zip内のファイルが「.c」,「.txt」のいずれかに統一されていません")
				exit()
	
	return list



# 害悪なファイルが存在する場合は削除する
def file_check(f_name):

	out1 = re.compile(r'$(.c)')
	out2 = re.compile(r'$(.txt)')
	
	if   out1.search(f_name) == None:
		return 1
	
	elif out2.search(f_name) == None:
		return 1
	
	elif f_name == "ans.c":
		return 1
	
	else:
		return 0



# 全てのcファイルを登録する
def c_check(file_list):
	c_list = []
	c_size = len(file_list)
	
	for i in range(c_size):
		if ".c" in file_list[i]:
			c_list.append(file_list[i])

	return c_list



# 全てのtxtファイルを登録する
def txt_check(file_list):
	txt_list = []
	txt_size = len(file_list)

	for i in range(txt_size):
		if ".txt" in file_list[i]:
			txt_list.append(file_list[i])
			
	return txt_list



# コメントと空白文字を読み込まないようにする
def delete_sorce(line):
	s_line = line
	
#	"//"が存在するか調べる
	pos1 = s_line.find("//")
	
#	"//"が存在するなら削除する
	if pos1 != -1:
		s_line = line[:pos1]
	
#	"/*"と"*/"が存在するか調べる
	pos2 = s_line.find("/*")
	pos3 = s_line.find("*/")
	
#	"/*"が存在する場合
	if pos2 != -1:
	
#		"/*" と "*/" が存在する場合
		if pos3 != -1:
			s_line = s_line[:pos2] + s_line[pos3+2:]
		
#		"/*"のみが存在する場合
		else:
			s_line = s_line[:pos2]


#	空白文字を削除
	s_line = s_line.replace(' ','')
	
#	コメントと空白文字を考慮したソースコードを返却する
	return s_line



# 学習者のプログラムを保存する
def read_leaner(f_name, len_list, miss_list, correct_list, order, path):
	global error_list
	
#	相違点の有無を示す値 (0:有り 1:無し)
	eq = 1

#	学習者プログラムのソースコード行数を数える
	len_count = 0

#	学習者のプログラムを読み込む
	f    = open(path + '/' + f_name)
	line = f.readline()
	
	
#	1行ごとに保存
	while line:
		
		if len_count <= len(len_list)-1:
		
#			正解プログラムと学習者のプログラムを比較している
			if compare_sorce(len_list[len_count].len,line) == 1: # 「模範解答のソースコード != 学習者のソースコード」 の場合
				eq = 0
				
#				字面が一致しない場合は、ミスリストに登録
				miss_list.append(str(len_count+1) + "行 : " + line)
				
#				比較できるように正解プログラムのソースコードも登録する
				correct_list.append(str(len_list[len_count].order) + "行 : " + str(len_list[len_count].len))
		
#		(正解プログラムの行数 < 学習者プログラムの行数) の場合はエラーリストに登録
		else:
			error_list.append(path + '/' + f_name)
			return eq
			
		
		len_count += 1
		
#		学習者プログラムの次の行を読み込む
		line = f.readline()
	
	
#	(学習者プログラムの行数 < 正解プログラムの行数) の場合はエラーリストに登録
	if len_count < order-1:
		error_list.append(path + '/' + f_name)
	
	f.close()
	return eq



#ソースコードを比較している
def compare_sorce(answer_p,leaner_p):
	
#	字面が一致しない場合
	if answer_p != leaner_p:
		s_answer_p = delete_sorce(answer_p) # コメントと空白文字を削除
		s_leaner_p = delete_sorce(leaner_p)
		
#		修正しても字面が一致しない場合
		if s_answer_p != s_leaner_p:
			return 1
		
#		修正したら字面が一致した場合
		else:
			return 0
			
#	字面が一致した場合
	else:
		return 0



# 相違点の有無を判定する
def print_eq(correct_list, miss_list, eq, path):
	f    = open(path, 'a', encoding="utf-8", newline='')
	size = len(miss_list)

#	両ソースコードの相違点を表示する
	f.write("\n\n相違点 : ")
	
#	字面が一致した場合、相違点は無いと表示する
	if eq == 1:
		f.write("無し\n\n\n")

#	字面が一致しない場合は相違点を表示する(実行結果は同じかもしれないので、正否は実行しないと分からない)
	else:
		f.write("あり\n\n\n")
		
		for i in range(size):
			f.write("学習者の解答\n\n" + miss_list[i] + "\n\n")
			f.write("模範解答\n\n" + correct_list[i] + "\n\n\n")

	f.close()
	
	

#実行結果を表示する
def print_answer(ans_exe, leaner_exe, path):
	f = open(path, 'a', encoding="utf-8", newline='')
	f.write("実行結果\n\n")
	
	ans_size    = len(ans_exe)
	leaner_size = len(leaner_exe)
	
	f.write("模範プログラム\n")
	for i in range(ans_size):
		f.write(ans_exe[i])
	f.write("\n\n")
	
	f.write("学習者のプログラム\n")
	for j in range(leaner_size):
		f.write(leaner_exe[j])
	f.write("\n\n")
	
	f.close()



#実行結果を比較する
def judge(answer1, answer2):
	size = len(answer1)
	
#	解答が一致しているか確認する
	for i in range(size):
	
#		模範プログラムと異なる実行結果の場合は不正解とする
		if answer1[i] != answer2[i]:
			return 1
	
#	全て一致した場合は正解とする
	return 0



# 実行結果の正誤判定をする
def print_judge(ans_exe, leaner_exe, miss_list, path, print_path):
	global another_list
	f = open(path, 'a', encoding="utf-8", newline='')
	
	if judge(ans_exe,leaner_exe) == 0:
	
		if 0 < len(miss_list):
			another_list.append(print_path)
			
		f.write("\n判定 : 一致\n\n\n")
		
	else:
		f.write("\n判定 : 不一致\n\n\n")
	
	f.close()



# 実行結果を記録する
def execution_results(c_file_name, txt_list, txt_size, path):
	exe_list = []
	pos = -1
	
#	名前に".c"があるので".txt"に変換して同名のファイルを探索する
	search_name = c_file_name.replace(".c",".txt")
	
#	cファイルの実行結果が記録されているtxtファイルを探索する
	for i in range(txt_size):
		
		if search_name == txt_list[i]:
			pos = i
	
#	対となるtxtファイルが存在する場合はファイル読み込みを開始する
	if pos != -1:
		f    = open(path + '/' + txt_list[pos])
		line = f.readline()
	
#	対となるtxtファイルが存在しない場合は終了
	else:
		print("Unknown file : {}".format(path + '/' + search_name))
		return []
	
#	実行結果をリストに記録する
	while line:
		exe_list.append(line)
		line = f.readline()
	
	f.close()
	return exe_list



# 配点の定義
def def_score(r_path, people_num):
	global correction_list
	global sub_score_list
	global total_score
	global bi_list
	
	total_score = 0
	count       = 0
	index       = 1
	f           = open(r_path, 'r', encoding="utf-8")
	line        = f.readline()
	
#	空欄の数を計算する
	while line:
		if ("/* □ □ □ */" in line) or ("/* ○ ○ ○ */" in line):
			count += 1
			bi_list.append(index)
		line = f.readline()
		index += 1
	f.close()
	
	sub_score_list = [1]*count
	sub_score_size = len(sub_score_list)
	
#	補正を掛ける
	for i in range(sub_score_size):
		hurdle_point = correction_list[bi_list[i]]
		
		if 0 < hurdle_point:
			hurdle_point += hurdle_point * (hurdle_point / people_num)
			
		else:
			hurdle_point += 1
		
#		各空欄の配点を計算
		hurdle_point      = int(round(hurdle_point,1) * 10)
		sub_score_list[i] = hurdle_point
		
#		総合点を計算
		total_score += hurdle_point
			
	

# 学習者プログラムの採点
def cal_score(w_path):
	global backup_miss_list
	global sub_score_list
	global bi_list
	backup_size = len(backup_miss_list)
	score_size  = len(sub_score_list)
	bi_size     = len(bi_list)
	total_score = 0
	
#	総合点を取得
	for i in range(score_size):
		total_score += sub_score_list[i]
	
#	miss_listを取得
	for i in range(backup_size):
		leaner_score_list = copy(sub_score_list)
		pos               = backup_miss_list[i]
		pos_size          = len(pos)
		
#		間違えた箇所のindexを取得
		for j in range(pos_size):
			index = pos[j]
			
#			indexの配点を取得
			for k in range(bi_size):
				
#				配点を0に変更
				if index == bi_list[k]:
					leaner_score_list[k] = 0
		
#		学習者の点数を計算
		leaner_score = 0
		
		for l in range(score_size):
			leaner_score += leaner_score_list[l]
		leaner_score = int((leaner_score / total_score) * 100)
		print_score(leaner_score_list, sub_score_list, score_size, path4 + '/' + result_list[i])
		
		f = open(path4 + '/' + result_list[i], 'a', encoding="utf-8", newline='')
		f.write("score : {}".format(leaner_score))
		f.close()
	
	
	
def print_score(leaner_score_list, sub_score_list, size, path):
	f = open(path, 'a', encoding="utf-8", newline='')

	for i in range(size):

		if leaner_score_list[i] == 0:
			f.write("空欄{} : ✕(配点{})\n".format(i+1, sub_score_list[i]))

		else:
			f.write("空欄{} : 〇(配点{})\n".format(i+1, sub_score_list[i]))
	
	f.close()



# 学習者全員のミスリストから間違いが多かった空欄を集計する
def total_miss(miss_list):
	global correction_list
	global backup_miss_list
	
	miss_size = len(miss_list)
	list      = []
	
	for i in range(miss_size):
		pos = miss_list[i].find('行')
		pos = int(miss_list[i][:pos])
		list.append(pos)
		correction_list[pos] += 1
	
	backup_miss_list.append(list)
	


# 別解の可能性があるファイルを表示する
def print_possibility(file_list):
	global error_list

	size1 = len(file_list)
	size2 = len(error_list)
	
	if size1 == 0:
		return
	
	else:
		with st.expander("別解のファイル一覧"):

			for i in range(size1):
				for j in range(size2):

					if file_list[i].replace('.txt', '.c') != error_list[j]:
						st.write(file_list[i])



# 制約違反のファイルを表示する
def print_error(error_list):

	size = len(error_list)
	
	if size == 0:
		return
	
	else:
		with st.expander("制約違反のファイル一覧"):
			for i in range(size):
				st.write(error_list[i])



def print_file():

	path1 = '/app/educationapp/marking/output'
	files = os.listdir(path1)
	f_list = []
	l_list = []
	index  = 0

	for f_name in files:
		
		f    = open(path1 + '/' + f_name, 'r', encoding = "utf-8")
		line = f.readline()

		while line:
			l_list.append(line)
			line = f.readline()

		f.close()

		f_list.append(copy(l_list))
		l_list.clear()

	f_size = len(f_list)
	for i in range(f_size):

		f      = open(path1 + '/' + f_list[i][0].replace(' ', ''), 'w', encoding = "utf-8", newline='')
		l_size = len(f_list[i])

		for j in range(l_size):
			f.write(f_list[index][j])

		index += 1
		f.close()



# zipファイルを作成
def create_zip():

	shutil.make_archive('student', format = 'zip', root_dir = '/app/educationapp/marking/output')

	with open("student.zip", "rb") as fp:
		btn = st.download_button(
        label     = "ファイルをダウンロード",
        data      = fp,
        file_name = "student.zip",
        mime      = "application/zip"
    )



# 不要なファイルを削除
def remove_file():

	shutil.rmtree("/app/educationapp/marking/input/c_file")
	shutil.rmtree("/app/educationapp/marking/input/txt_file")
	shutil.rmtree("/app/educationapp/marking/output")

	os.remove("/app/educationapp/marking/ans.c")
	os.remove("/app/educationapp/marking/prob.c")



st.markdown("## 空欄補充問題採点アプリ")

upload_file1 = st.file_uploader('ans.c (提出ファイル数上限 : 1)'          , type = 'c'  )
upload_file2 = st.file_uploader('ans.txt (提出ファイル数上限 : 1)'        , type = 'txt')
upload_file3 = st.file_uploader('prob.c (提出ファイル数上限 : 1)'         , type = 'c'  )
upload_file4 = st.file_uploader('student_c.zip (提出ファイル数上限 : 1)'  , type = 'zip')
upload_file5 = st.file_uploader('student_txt.zip (提出ファイル数上限 : 1)', type = 'zip')


if upload_file1 and upload_file2 and upload_file3 and upload_file4 and upload_file5:

	if st.button("採点を開始"):

#		エラーチェック
		create_dir()
		decode_ans_c()
		decode_ans_txt()
		decode_prob_c()
		decode_student_c()
		decode_student_txt()
		check_student_num()
		
#		参照ファイルのパス
		path1 = "/app/educationapp/marking/input/c_file"
		path2 = "/app/educationapp/marking/input/txt_file"
		path3 = "/app/educationapp/marking/prob.c"
		path4 = "/app/educationapp/marking/output"

#		模範プログラムを保存する
		len_list = []
		order    = read_ans(len_list)

#		参照するファイルを登録する
		file1_list = os.listdir(path1)
		file2_list = os.listdir(path2)
		file1_list = [i for i in file1_list if ".c" in i]
		file2_list = [i for i in file2_list if ".txt" in i]

#		cファイルのリスト
		c_list = c_check(file1_list)
		c_size = len(c_list)

#		txtファイルのリスト
		txt_list = txt_check(file2_list)
		txt_size = len(txt_list)

#		正誤判定を記録するファイル
		result_list = [i for i in file2_list if ".txt" in i]

#		採点で使用
		correction_list  = [0]*order
		backup_miss_list = []
		error_list       = []
		bi_list          = []
		sub_score_list   = None
		total_score      = None

#		別解の可能性があるファイルを登録する
		another_list = []

#		模範プログラムの実行結果を格納
		ans_exe = []
		read_ans_exe()

#		cファイル数まで繰り返し
		for i in range(c_size):

#			模範解答と異なる記述の行を記録する
			miss_list = []

#			学習者の解答と異なる記述の行を記録する
			correct_list = []

#			学習者のプログラムを保存し、相違点の有無を示す値をeqに代入する
			eq = read_leaner(c_list[i], len_list, miss_list, correct_list, order, path1)
			
#			実行しているファイル名を表示
			path = path4 + '/' + result_list[i]
			f    = open(path, 'w', encoding="utf-8", newline='')
			f.write(c_list[i])
			f.close()
			
#			両ソースコードの相違点を表示する
			print_eq(correct_list, miss_list, eq, path)
			
#			学習者の実行結果を記録する
			leaner_exe = execution_results(c_list[i], txt_list, txt_size, path2)
			
#			実行結果を表示する
			print_answer(ans_exe,leaner_exe, path)
			
#			正誤判定を行う
			print_path = path1 + '/' + result_list[i]
			print_judge(ans_exe,leaner_exe, miss_list, path, print_path)
			
#			学習者全員のミスリストをカウントすることで間違いが多かった空欄を集計する
			total_miss(miss_list)

			print("write : {}".format(path))

		print_file()
#		別解の可能性があるファイルを表示する
		print_possibility(another_list)

#		制約違反3に該当するファイルを表示する
		print_error(error_list)

#		各空欄の配点と総合点数を定義する
		def_score(path3, c_size)

#		学習者の点数を計算する
		cal_score(path4)

#		採点ファイルをzipファイルに圧縮
		create_zip()

#		ファイルを削除
		remove_file()