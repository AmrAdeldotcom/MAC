import os
def rename_files():
    # get file names
    file_list = os.listdir(r"prank")
        # rename each file
    print file_list
    saved_path = os.getcwd() #crrent working dir
    print "Current Dir "+ saved_path
    #change Working Dir
    os.chdir(r"prank")
    for file in file_list:
        os.rename(file,file.translate(None,"0123456789"))
    os.chdir(saved_path)
rename_files()
