import sys
import kalman

file = open('out.txt','w')
file.write("RA 32/2014 Stevan Matovic")
file.write('\nfile  sum')

for i in range(0,10):
    r = kalman.resenje("videos/video-" + str(i) + ".avi")
    file.write("\nvideo-"+ str(i) + ".avi\t" + str(r))
