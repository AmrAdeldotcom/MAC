import webbrowser
import time

total_break = 3
break_count = 0
print "this program started on " + time.ctime()
while break_count < total_break:
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=Py6SZdUrLtY")
    break_count += 1
