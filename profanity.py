import urllib, os

def check(text):
    connection = urllib.urlopen("http://www.purgomalum.com/service/containsprofanity?text="+text)
    #http://www.wdylike.appspot.com/?q=love
    output = connection.read()
    if "true" in output:
        return True
    connection.close()
    return False
#import os
def read_file(file_path):
    file = open(file_path)
    content = file.read()
    file.close()
    return check(content)

print check("shit")
#print read_file(r'D:\Documents\AmrAdel\Desktop\udacity\run_Python_scripts_in_any_Cpanel_Hosting.htm')
#print read_file('D:/Documents/AmrAdel/Desktop/udacity/run_Python_scripts_in_any_Cpanel_Hosting.htm')
#print read_file('D:\\Documents\\AmrAdel\\Desktop\\udacity\\run_Python_scripts_in_any_Cpanel_Hosting.htm')
