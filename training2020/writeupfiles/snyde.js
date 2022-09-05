const CryptoJS = require('crypto-js')
const { encode } = require('./ascii.js')
const flag = require('./flag.js')

let pass = '?????????????' // input here

const key_check = '©×ïûÐ»ĐĭĥĤŁĕğ'
const user = 'administrator'

const checkPass = (username, password) => {
    for (let i = 0; i < user.length; i++) {
        if ((username.charCodeAt(i) + password.charCodeAt(i) + i * 10) !== key_check.charCodeAt(i)) {
            return false
        }
    }
    return true
}

if (checkPass(user, pass)) {
    console.log(encode(CryptoJS.AES.encrypt(flag, pass).toString()))
} else {
    console.log(encode(CryptoJS.AES.encrypt('ispclub{ffffffff}', pass).toString()))
}
// output console: <~<AI$bA4K[9=>;<a2`Y\h;`$j79M&/LAi4]g:dmiu<bHA2G#W'BE(+5S=u&Eg:N0`XBJb!TB5;^73&X;n:es&[5t5ck.s<X]@UjCf7VHa<Dc&Y\~>