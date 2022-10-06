import base64


def get_base64_diff_value(s1, s2):
    base64chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    for i in range(len(s2)):
        if s1[i] != s2[i]:
            return abs(base64chars.index(s1[i]) - base64chars.index(s2[i]))
    return 0


def solve_stego(stego_str_list):
    bin_str = ''
    for stego_str in stego_str_list:
        stego_str = stego_str.replace('\n', '')
        norm_str = base64.b64encode(base64.b64decode(stego_str)).decode()
        diff = get_base64_diff_value(stego_str, norm_str)
        pads_num = stego_str.count('=')
        if pads_num > 0:
            bin_str += bin(diff)[2:].zfill(pads_num * 2)

    ret = b''
    for i in range(0, len(bin_str), 8):
        ret += int(bin_str[i:i + 8], 2).to_bytes(1, 'little')
    return ret


def main():
    with open('strawberriesncigarettes.enc', 'rb') as fp:
        file_lines = fp.readlines()
    stego_str_list = []
    for each in file_lines:
        stego_str_list.append(each.decode().replace('\n', ''))
    print(solve_stego(stego_str_list))


if __name__ == '__main__':
    main()