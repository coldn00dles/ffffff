import socket
import codecs
def hexatobinary(s):
    mp = {'0': "0000",
          '1': "0001",
          '2': "0010",
          '3': "0011",
          '4': "0100",
          '5': "0101",
          '6': "0110",
          '7': "0111",
          '8': "1000",
          '9': "1001",
          'a': "1010",
          'b': "1011",
          'c': "1100",
          'd': "1101",
          'e': "1110",
          'f': "1111"}
    bin_str = ""
    for char in s:
        bin_str += mp[char.lower()] 
    return bin_str

def text_to_hex(text):
    hex_text = ''.join(format(ord(char), '02x') for char in text)
    return hex_text

def binarytohex(s):
    mp = {"0000": '0',
          "0001": '1',
          "0010": '2',
          "0011": '3',
          "0100": '4',
          "0101": '5',
          "0110": '6',
          "0111": '7',
          "1000": '8',
          "1001": '9',
          "1010": 'A',
          "1011": 'B',
          "1100": 'C',
          "1101": 'D',
          "1110": 'E',
          "1111": 'F'}
    hex_str = ""
    for i in range(0, len(s), 4):
        ch = ""
        ch = ch + s[i]
        ch = ch + s[i + 1]
        ch = ch + s[i + 2]
        ch = ch + s[i + 3]
        hex_str = hex_str + mp[ch]
    return hex_str


def binarytodecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal

def decimaltobinbary(num):
    res = bin(num).replace("0b", "")
    if(len(res) % 4 != 0):
        div = len(res) / 4
        div = int(div)
        counter = (4 * (div + 1)) - len(res)
        for i in range(0, counter):
            res = '0' + res
    return res

def permutatingfunc(k, arr, n):
    permutation = ""
    for i in range(0, n):
        permutation = permutation + k[arr[i] - 1]
    return permutation

def circularleftshift(k, nth_shifts):
    s = ""
    for i in range(nth_shifts):
        for j in range(1, len(k)):
            s = s + k[j]
        s = s + k[0]
        k = s
        s = ""
    return k
 
def xor(a, b):
    ans = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            ans = ans + "0"
        else:
            ans = ans + "1"
    return ans

IP = [58, 50, 42, 34, 26, 18, 10, 2,60, 52, 44, 36, 28, 20, 12, 4,62, 54, 46, 38, 30, 22, 14, 6,64, 56, 48, 40, 32, 24, 16, 8,57, 49, 41, 33, 25, 17, 9, 1,59, 51, 43, 35, 27, 19, 11, 3,61, 53, 45, 37, 29, 21, 13, 5,63, 55, 47, 39, 31, 23, 15, 7]
 

E_P = [32, 1, 2, 3, 4, 5, 4, 5,
       6, 7, 8, 9, 8, 9, 10, 11,
       12, 13, 12, 13, 14, 15, 16, 17,
       16, 17, 18, 19, 20, 21, 20, 21,
       22, 23, 24, 25, 24, 25, 26, 27,
       28, 29, 28, 29, 30, 31, 32, 1]
 

per = [16, 7, 20, 21,29, 12, 28, 17,1, 15, 23, 26,5, 18, 31, 10,2,  8, 24, 14,32, 27,  3,  9,19, 13, 30, 6, 22, 11,  4, 25]
 

sbox = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],[0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],[4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],[15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],
        [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],[3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],[0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],[13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],
 		[[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],[13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],[13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],[1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],
 		[[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],[13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],[10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],[3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],
 		[[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],[14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],[4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],[11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],
 		[[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],[10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],[9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],[4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],
 		[[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],[13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],[1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],[6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],
 		[[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],[1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],[7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],[2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]

pfinal = [40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
    	36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25]

P_56 = [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4]

ROUNDS = [1, 1, 2, 2,2, 2, 2, 2,1, 2, 2, 2,2, 2, 2, 1]

p_48 = [14, 17, 11, 24, 1, 5,3, 28, 15, 6, 21, 10,23, 19, 12, 4, 26, 8,16, 7, 27, 20, 13, 2,41, 52, 31, 37, 47, 55,30, 40, 51, 45, 33, 48,44, 49, 39, 56, 34, 53,46, 42, 50, 36, 29, 32]

 
def des_encrypt(pt, round_keys_bin):
    pt = hexatobinary(pt)
    pt = permutatingfunc(pt, IP, 64)
    left = pt[0:32]
    right = pt[32:64]
    for i in range(0, 16):
        right_expanded = permutatingfunc(right, E_P, 48)
        xor_x = xor(right_expanded, round_keys_bin[i])
        sbox_str = ""
        for j in range(0, 8):
            row = binarytodecimal(int(xor_x[j * 6] + xor_x[j * 6 + 5]))
            col = binarytodecimal(
                int(xor_x[j * 6 + 1] + xor_x[j * 6 + 2] + xor_x[j * 6 + 3] + xor_x[j * 6 + 4]))
            val = sbox[j][row][col]
            sbox_str = sbox_str + decimaltobinbary(val)
        sbox_str = permutatingfunc(sbox_str, per, 32)
        result = xor(left, sbox_str)
        left = result
        if(i != 15):
            left, right = right, left
    combine = left + right
    cipher_text = permutatingfunc(combine, pfinal, 64)
    return cipher_text
def hextotext(hex_text):
    text = bytearray.fromhex(hex_text).decode('utf-8')
    return text

key = "AABB09182736CCDD"
key = hexatobinary(key)
key = permutatingfunc(key, P_56, 56)

left = key[0:28]  
right = key[28:56]  
 
round_keys_bin = []

for i in range(0, 16):
    left = circularleftshift(left, ROUNDS[i])
    right = circularleftshift(right, ROUNDS[i])
    combine_str = left + right

    round_key = permutatingfunc(combine_str, p_48, 48)
 
    round_keys_bin.append(round_key)




client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12345
client_socket.connect((host, port))


plaintext_text = str(input("Enter message to be encrypted"))

# Convert text to hex
plaintext_hex = text_to_hex(plaintext_text)

# Encrypt the hex version of the text
cipher_text = binarytohex(des_encrypt(plaintext_hex, round_keys_bin))
round_keys_bin_rev = round_keys_bin[::-1]

cipher_block = f"{cipher_text}|"

for i in round_keys_bin_rev:
    cipher_block+=i

client_socket.send(cipher_block.encode())
print("Cipher text sent : ",cipher_block.split("|")[0])
returned_plaintext = client_socket.recv(1024).decode("utf-8")

print("Decrypted text received is : ",returned_plaintext)

client_socket.close()