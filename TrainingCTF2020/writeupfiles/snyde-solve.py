from Crypto import Random
from Crypto.Cipher import AES
import base64

flag_enc = "<~<AI$bA4K[9=>;<a2`Y\h;`$j79M&/LAi4]g:dmiu<bHA2G#W'BE(+5S=u&Eg:N0`XBJb!TB5;^73&X;n:es&[5t5ck.s<X]@UjCf7VHa<Dc&Y\~>"

def decrypt(encrypted, passphrase):
    IV = Random.new().read(AES.BLOCK_SIZE)
    aes = AES.new(passphrase, AES.MODE_CFB, IV)
    return aes.decrypt(base64.b64decode(encrypted))

def solved():
	u = 'administrator'
	k = '©×ïûÐ»ĐĭĥĤŁĕğ'
	p = list()
	for i in range(len(u)):
		p.append(chr(ord(k[i]) - i*10 - ord(u[i])))
	print(decrypt(base64.a85decode(flag_enc, adobe=True).decode('utf-8'), ''.join(p)))
solved()