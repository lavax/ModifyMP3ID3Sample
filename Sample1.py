# coding:utf-8
import os
import sys
import logging
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2, TALB, TPE1, TPE2, TRCK

logging.basicConfig(level=logging.DEBUG)


# fileSub = ".mp3"
# # filePath = "F:\Downloads\明朝那些事儿-刘纪同\明朝那些事儿第三部[全71集](播音—刘纪同)"
# filePath = 'F:\Downloads\明朝那些事儿-刘纪同\\test'
# fileNameToken = "_[Ã¼+ñ¦²-Ú-°www.qktsw.com]"
# fileNewNameToken = ""


# if len(sys.argv) == 4:
#     # 如果只有3个参数，那么说明把fileNameToken替换成空字符串
#     fileNewNameToken = ''
#     fileSuffix = sys.argv[3]
# elif len(sys.argv) == 5:
#     fileNewNameToken = sys.argv[3]
#     fileSuffix = sys.argv[4]
# else:
#     logging.error("参数错误，应为3或4个！")
#     sys.exit(-1)
# filePath = sys.argv[1]
# fileNameToken = sys.argv[2]


def rename(file_path, replace_tokens, file_suffix):
    files = os.listdir(file_path)
    for old_file_name in files:
        # fileName
        old_file_path = os.path.join(file_path, old_file_name)  # 获取path与filename组合后的路径
        if os.path.isfile(old_file_path) and old_file_name.endswith(file_suffix):
            for file_name_token, file_new_name_token in replace_tokens.items():
                if old_file_name.find(file_name_token) != -1:
                    new_file_name = old_file_name.replace(file_name_token, file_new_name_token)
                    new_file_path = os.path.join(file_path, new_file_name)
                    logging.info(new_file_path)
                    # os.rename(old_file_path, new_file_path)


def files2tag(file_dir, file_suffix):
    files = os.listdir(file_dir)
    for file_name in files:
        tit2_str = file_name.replace(file_suffix, '')
        tokens = tit2_str.split('-')
        talb_str = tokens[0]
        tpe2_str = tokens[1]
        trck_str = tokens[2]
        logging.debug('%s,%s,%s,%s', tit2_str, talb_str, tpe2_str, trck_str)

        tit2 = TIT2(text=tit2_str)  # 标题
        talb = TALB(text=talb_str)  # 唱片集
        tpe2 = TPE2(text=tpe2_str)  # 唱片集艺术家
        tpe1 = TPE1(text='当年明月')  # 参与创作的艺术家
        trck = TRCK(text=trck_str)  # #

        file_path = os.path.join(file_dir, file_name)
        id3 = ID3(file_path)
        id3.add(tit2)
        id3.add(talb)
        id3.add(tpe1)
        id3.add(tpe2)
        id3.add(trck)
        id3.save()

    # 备注
    # COMM::eng = ''
    # fileName = 'F:\Downloads\明朝那些事儿-刘纪同\明朝那些事儿第一部[全119集](播音—刘纪同)\明朝那些事儿1-刘纪同-119.mp3'
    # mp3 = ID3(fileName)
    # for k, v in mp3.items():
    #     logging.debug('%s=%s', k, v)
    #

def files2tag2(file_dir, file_suffix):
    files = os.listdir(file_dir)
    for file_name in files:
        tit2_str = file_name.replace(file_suffix, '')
        tokens = tit2_str.split('-')
        talb_str = tokens[0]
        tpe2_str = tokens[1]
        trck_str = tokens[2]
        logging.debug('%s,%s,%s,%s', tit2_str, talb_str, tpe2_str, trck_str)

        tit2 = TIT2(text=tit2_str)  # 标题
        talb = TALB(text=talb_str)  # 唱片集
        tpe2 = TPE2(text=tpe2_str)  # 唱片集艺术家
        tpe1 = TPE1(text='当年明月')  # 参与创作的艺术家
        trck = TRCK(text=trck_str)  # #

        file_path = os.path.join(file_dir, file_name)
        id3 = ID3(file_path)
        id3.add(tit2)
        id3.add(talb)
        id3.add(tpe1)
        id3.add(tpe2)
        id3.add(trck)
        id3.save()

if __name__ == "__main__":
    # 文件所在目录
    dirList = ['F:\Downloads\明朝那些事儿-刘纪同\明朝那些事儿第五部[全39集](播音—刘纪同)', 'F:\Downloads\明朝那些事儿-刘纪同\明朝那些事儿第四部[全80集](播音—刘纪同)',
               'F:\Downloads\明朝那些事儿-刘纪同\明朝那些事儿第三部[全71集](播音—刘纪同)', 'F:\Downloads\明朝那些事儿-刘纪同\明朝那些事儿第二部[全37集](播音—刘纪同)',
               'F:\Downloads\明朝那些事儿-刘纪同\明朝那些事儿第一部[全119集](播音—刘纪同)']
    # 替换字符串
    replaceTokens = {
        '+¸¦»-Ãð®--Â¨Á+--¦+_-§+--¼': '明朝那些事儿4-刘纪同-',
        '+¸¦»-Ãð®--Â¨Á++²¦+_-§+--¼': '明朝那些事儿3-刘纪同-',
        '+¸¦»-Ãð®--Â¨Á+Â¦¦+_-§+--¼': '明朝那些事儿2-刘纪同-'}

    fileSuffix = ".mp3"

    logging.debug('dirList=%s', dirList)
    logging.debug('replaceTokens=%s', replaceTokens)
    logging.debug('fileSuffix=%s', fileSuffix)

    for filePath in dirList:
        rename(filePath, replaceTokens, fileSuffix)
        files2tag(filePath, fileSuffix)