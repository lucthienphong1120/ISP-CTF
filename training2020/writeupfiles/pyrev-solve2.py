import base64
cc = open('data.dat','r').read() # data.dat have encrypted string
cc = cc[::8]
cc = cc[:2:-1]
print(base64.b64decode((cc[1:19:2]+cc[19::3]).replace("ispclub6910832",'').replace("imustDOTHISCHALL011014",'').encode('utf-8')))