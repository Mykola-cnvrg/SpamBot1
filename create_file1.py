import time

f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

time.sleep(3000)
