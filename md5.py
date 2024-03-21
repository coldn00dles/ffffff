import math

A = 0x67452301
B = 0xEFCDAB89
C = 0x98BADCFE
D = 0x10325476

vectors = [A,B,C,D]

K = [int(abs(math.sin(i+1)) * (2**32)) & 0xFFFFFFFF for i in range(64)]


s = [7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
			 5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20,
			 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
			 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21]

def padding(msg):
    m_length = (8*len(msg)) & 0xffffffffffffffff
    msg.append(0x80)  #0x80 -> 0b1000000 (appending the first 1)
    
    while len(msg)%64 !=56:  #448 mod 512 is the same as 56 mod 64, length needs to be congruent to it.
        msg.append(0)
    
    msg+=m_length.to_bytes(8,byteorder="little")  
    return msg


def left_shift_by_s(x,s_val):
    x&=0xFFFFFFFF
    return (x << s_val | x >> (32-s_val)) & 0xFFFFFFFF

def processMessage(msg):
	init_temp = vectors[:] 
	
	
	for os in range(0, len(msg), 64):
		A, B, C, D = init_temp 
		block = msg[os : os+64] 

		for i in range(64):
			if i < 16:

				func = lambda b, c, d: (b & c) | (~b & d)
				index_func = lambda i: i

			elif i >= 16 and i < 32:

				func = lambda b, c, d: (d & b) | (~d & c)

				index_func = lambda i: (5*i + 1)%16

			elif i >= 32 and i < 48:

				func = lambda b, c, d: b ^ c ^ d

				index_func = lambda i: (3*i + 5)%16
			
			elif i >= 48 and i < 64:

				func = lambda b, c, d: c ^ (b | ~d)
				index_func = lambda i: (7*i)%16

			F = func(B, C, D) 
			G = index_func(i) 

			to_rotate = A + F + K[i] + int.from_bytes(block[4*G : 4*G + 4], byteorder='little')
			newB = (B + left_shift_by_s(to_rotate, s[i])) & 0xFFFFFFFF
				
			A, B, C, D = D, newB, B, C


		for i, val in enumerate([A, B, C, D]):
			init_temp[i] += val
			init_temp[i] &= 0xFFFFFFFF

	return sum(buffer_content<<(32*i) for i, buffer_content in enumerate(init_temp))



def hex_string(dig):
	raw = dig.to_bytes(16, byteorder='little')
	return '{:032x}'.format(int.from_bytes(raw, byteorder='big'))


msg = input("Enter string to be hashed : ")
og_pt = msg
msg = bytearray(msg, 'ascii') 
msg = padding(msg)
processed_msg = processMessage(msg)

message_hash = hex_string(processed_msg)
print(f"MD5 Hash for {og_pt}: ", message_hash)
