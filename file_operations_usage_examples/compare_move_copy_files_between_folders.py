'''
- compare the filenames (same/different) present in two different folders 
- Move/copy files from src to dst 
'''
import numpy as np
import os 
import shutil


def same_files(dirA, dirB): 
    """Returns filenames/images name present in both dirA and in dirB (same)"""
    c = [i for i in dirA if i in dirB]
    print("Count of same files in folderA and folderB : \n", c, len(c))
    return c

def diff_files(dirA, dirB):
    """Returns filenames/images name present in dirA but not in dirB (diff)"""
    dif = [i for i in dirA if i not in dirB]
    print("Count of files in folderA but not in folderB : \n", dif, len(dif))
    return dif

def move_copy_files(src_path, dst_path, filename_list, operation='move'):
    """Move/copy images/files from src to destination based on name list"""
    cnt = 0 
    for i in filename_list:
        src = os.path.join(src_path, i)
        dst = os.path.join(dst_path, i)
        if operation == 'move':
            shutil.move(src, dst)
        elif operation == 'copy':
            shutil.copy(src, dst)
        else:
            break
        cnt +=1 
    print(f'Finished copying {cnt} files from {src_path} to {dst_path}')

if __name__ == '__main__':
    
    a = r'C:\Users\kkeer\Desktop\Vignesh\demo\fol1'
    b = r'C:\Users\kkeer\Desktop\Vignesh\demo\fol3'

    list1 = os.listdir(a)
    list2 = os.listdir(b)

    same = same_files(list1, list2)
    diff = diff_files(list1, list2)
    copy_img = move_copy_files(a, b, list1, operation='copy')
