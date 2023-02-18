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
	out2       = re.compile(r'.txt')

	for f_name in file2_list:

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

	if size1 != size2:
		st.write("エラー student_c.zip と student_txt.zip 内のファイル数が一致しません")
		exit()

	for i in range(size1):

		if file1_names[i].replace(".c", '') != file2_names[i].replace(".txt", ''):
			st.write("エラー student_c.zip と student_txt.zip 内のファイル名が一致しない組があります")
			exit()

	file1_list.clear()
	file2_list.clear()



def create_output_txt(file_path):

	f = open(file_path, 'w', encoding = "utf-8")
	f.close()



def dif_code(ans_c, c_file, output, ans_sum_lines):

	c_file_sum_lines = None

	with open(c_file) as myfile:
			c_file_sum_lines = sum(1 for line in myfile)

	ans_f    = open(ans_c,  'r', encoding = "utf-8")
	c_file_f = open(c_file, 'r', encoding = "utf-8")
	output_f = open(output, 'w', encoding = "utf-8", newline = '')

	if ans_sum_lines != c_file_sum_lines:
		output_f.write("制約違反のファイル")
	
	else:

		ans_line    = ans_f.readline()
		c_file_line = c_file_f.readline()
		index       = 1
		flag        = 0

		output_f.write("コードの相違点\n\n")

		while ans_line:

			if ans_line != c_file_line:
				output_f.write("{} : {}\n\n".format(index, ans_line))
				output_f.write("{} : {}\n\n".format(index, c_file_line))
				flag = 1

			ans_line    = ans_f.readline()
			c_file_line = c_file_f.readline()
			index      += 1

		if flag == 0:
			output_f.write("相違点なし")

	ans_f.close()
	c_file_f.close()
	output_f.close()



# zipファイルを作成
def create_zip(path3):

	shutil.make_archive('student', format = 'zip', root_dir = path3)

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

		create_dir()
		decode_ans_c()
		decode_ans_txt()
		decode_prob_c()
		decode_student_c()
		decode_student_txt()
		check_student_num()
		
		path1   = "/app/educationapp/marking/input/c_file"
		path2   = "/app/educationapp/marking/input/txt_file"
		path3   = "/app/educationapp/marking/output"

		ans_c   = "/app/educationapp/marking/ans.c"
		ans_txt = "/app/educationapp/marking/ans.txt"
		prob_c  = "/app/educationapp/marking/prob.c"
		
		ans_sum_lines = None

#		ans.cの行数を取得
		with open(ans_c) as myfile:
			ans_sum_lines = sum(1 for line in myfile)

		files = os.listdir(path1)
		files = [f for f in files if os.path.isfile(os.path.join(path1, f))]

		for f_name in files:

			c_file   = path1 + '/' + f_name
			txt_file = path2 + '/' + f_name.replace(".c", ".txt")
			output   = path3 + '/' + f_name.replace(".c", ".txt")

			create_output_txt(output)

			dif_code(ans_c, c_file, output, ans_sum_lines)

		create_zip(path3)
