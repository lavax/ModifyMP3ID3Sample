# coding:utf-8
import os
import sys
import logging
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2, TALB, TPE1, TPE2, TRCK

logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    # 文件所在目录
    dir1 = 'F:\Downloads\三体-哈哈笑\三体2_黑暗森林[全85集](播音——哈哈笑)'
    dir2 = 'F:\Downloads\三体-哈哈笑\三体3_死神永生[全99集](播音——哈哈笑)'
    file_suffix = '.mp3'

    files = os.listdir(dir1)
    for old_file_name in files:
        tit2_str = old_file_name.replace(file_suffix, '').replace('_', '-')  # 标题
        tokens = tit2_str.split('-')
        talb_str = '三体2'  # 唱片集
        tpe2_str = '哈哈笑'  # 唱片集艺术家
        tpe1_str = '刘慈欣;'  # 参与创作的艺术家
        trck_str = tokens[1]  # #
        tit2_str = '黑暗森林-' + trck_str
        new_file_name = talb_str + '-' + tit2_str + file_suffix
        logging.debug('%s,%s,%s,%s', tit2_str, talb_str, tpe2_str, trck_str)

        tit2 = TIT2(text=tit2_str)  # 标题
        talb = TALB(text=talb_str)  # 唱片集
        tpe2 = TPE2(text=tpe2_str)  # 唱片集艺术家
        tpe1 = TPE1(text=tpe1_str)  # 参与创作的艺术家
        trck = TRCK(text=trck_str)  # #

        old_file_path = os.path.join(dir1, old_file_name)
        new_file_path = os.path.join(dir1, new_file_name)
        os.rename(old_file_path, new_file_path)
        logging.debug(new_file_path)
        id3 = ID3(new_file_path)
        id3.add(tit2)
        id3.add(talb)
        id3.add(tpe1)
        id3.add(tpe2)
        id3.add(trck)
        id3.save()

    files = os.listdir(dir2)
    for old_file_name in files:
        # tit2_str = old_file_name.replace(file_suffix, '')
        tokens = old_file_name.replace(file_suffix, '').split('-')
        token = tokens[1]

        talb_str = '三体3'  # 唱片集
        tpe2_str = '哈哈笑'  # 唱片集艺术家
        tpe1_str = '刘慈欣;'  # 参与创作的艺术家
        trck_str = token[-3:]  # #
        tit2_str = '死神永生-' + trck_str  # 标题
        new_file_name = talb_str + '-' + tit2_str  + file_suffix
        logging.debug('%s,%s,%s,%s', tit2_str, talb_str, tpe2_str, trck_str)

        tit2 = TIT2(text=tit2_str)  # 标题
        talb = TALB(text=talb_str)  # 唱片集
        tpe2 = TPE2(text=tpe2_str)  # 唱片集艺术家
        tpe1 = TPE1(text=tpe1_str)  # 参与创作的艺术家
        trck = TRCK(text=trck_str)  # #

        old_file_path = os.path.join(dir2, old_file_name)
        new_file_path = os.path.join(dir2, new_file_name)
        os.rename(old_file_path, new_file_path)
        logging.debug(new_file_path)
        id3 = ID3(new_file_path)
        id3.add(tit2)
        id3.add(talb)
        id3.add(tpe1)
        id3.add(tpe2)
        id3.add(trck)
        id3.save()
