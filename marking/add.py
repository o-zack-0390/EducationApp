import os

def change_file():
    
    path  = "/app/educationapp/marking/output"
    files = os.listdir(path)
    files = [f for f in files if os.path.isfile(os.path.join(path, f))]
    index = -1

    for f_name in files:

      index   += 1
      tmp_path = path + '/' + str(index) + ".txt"

      os.rename(path + '/' + f_name, tmp_path)

    for i in range(index+1):
       
       tmp_path = path + '/' + str(i)
       f        = open(tmp_path, 'r', encoding = "utf-8", newline = '')

       os.rename(tmp_path, path + '/' + f.readline())
       f.close()


change_file()