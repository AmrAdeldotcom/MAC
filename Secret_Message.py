import os
def rename_files():
    # get file names
    file_list = os.listdir(r"D:\Documents\AmrAdel\Desktop\udacity\ipnd-starter-code-master\stage_3\lesson_3.2_using_functions\secret_message\prank")
        # rename each file
    saved_path = os.getcwd() #crrent working dir
    print "Current Dir "+ saved_path
    #change Working Dir
    os.chdir(r"D:\Documents\AmrAdel\Desktop\udacity\ipnd-starter-code-master\stage_3\lesson_3.2_using_functions\secret_message\prank")
    for file in file_list:
        os.rename(file,file.translate(None,"0123456789"))
    os.chdir(saved_path)
rename_files()
