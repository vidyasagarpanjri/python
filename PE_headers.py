#script to take folder as input and put put the DOS headers next file offset and compile timestamp

import pefile
import glob
import datetime


#print d
def FaritPE(folder):
    ret_list=[]
    d = glob.glob(folder)
    for f in d:
        p = pefile.PE(f)
        ret_list.append([datetime.datetime.fromtimestamp(p.FILE_HEADER.TimeDateStamp),p.DOS_HEADER.e_lfanew])
    return ret_list
    

if __name__=='__main__':
    print FaritPE("C:\\path\\to\\exe\\folder\\*")
