import urllib
import subprocess
import re
import time

#Run Speedtest-cli and get output
process = subprocess.Popen(["speedtest-cli", "--share"], stdout=subprocess.PIPE)
out, err = process.communicate()
#print(out)

#Extract URL
time.sleep(10)
url = out.split('Share results: ', 1) [1]

#Download score image and put it in the widget
image = urllib.URLopener()
#image.retrieve(url,"/var/www/html/plugins/widget/core/images/bw.png")
image.retrieve(url,"/home/matt/Images/bw.png")

process = subprocess.Popen(["sudo", "cp", "/home/matt/Images/bw.png", "/var/www/html/plugins/widget/core/images/bw.png"], stdout=subprocess.PIPE)
out2, err = process.communicate()
