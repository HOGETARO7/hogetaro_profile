#############################
#
# Yotaro Yamashita
#
#
#############################

###モジュールインポート
import sys
import glob

###変数定義
filename1 = r'replace/test.bat'
filename2 = r'replace/test2.bat'
str_be1 = '@@@backet_name'
str_be2 = '@@@test'
str_af = ''
DIR = r'conf/*.ps1'

###関数定義
#置換用
def replace(filename,str_be,str_af):

    with open(filename, 'r') as f:
        inputdata = f.read()

    outputdata = inputdata.replace(str_be, str_af)

    with open (filename ,'w') as f:
        f.write(outputdata)

#変数引用用
def get_data(str_be):
    for file in glob.glob(DIR):
        with open(file, 'r') as a:
            lists = a.readlines()
            for list in lists:
                data = list.split('=')
                if data[0] == str_be:
                    #シングルクォーテションを削除する。
                    str_af = data[1].replace("'", "")
                    print(str_af, end='')
                    return str_af

#メッセージ用
def messageout(str_name):
    message = str_name + 'の置換を始めます。'
    return message

###主処理
#処理開始用メッセージの取得
message1 = messageout(str_be1)
#処理開始用メッセージの出力
print(message1)
str_af1 = get_data(str_be1)
replace(filename1,str_be1,str_af1)
