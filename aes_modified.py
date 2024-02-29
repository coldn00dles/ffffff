def keyExpansion(key,numround,rci,s_box):
    round_const = rci[numround-1]
    gw3 = [key[3][1],key[3][2],key[3][3],key[3][0]]
    for i in range(4):
        u = hex(s_box[int(gw3[i][2],16)][int(gw3[i][3],16)])
        if(u == "0x0"):
            u = "0x00"
        elif(len(u.lstrip("0x"))<=1):
            u = "0x0"+u.lstrip("0x")
        gw3[i] = u
    a = 1
    b = 1
    if(gw3[0] == "0x00" or gw3[0] == "0x0"):
        a = 0
    else:
        a = int(gw3[0].lstrip("0x"),16)
    x = hex(int(a^int(round_const.lstrip("0x"),16)))
    if(x == "0x0"):
        x = "0x00"
    elif(len(x.lstrip("0x"))<=1):
        x = "0x0"+x.lstrip("0x")
    gw3[0] = x
    w4 = []
    for i in range(4):
        r = 1
        p = 1
        if(gw3[i] == "0x00" or gw3[i] == "0x0"):
            r = 0
        else:
            r = int(gw3[i].lstrip("0x"),16)
        if(key[0][i] == "0x00" or key[0][i] == "0x0"):
            p = 0
        else:
            p = int(key[0][i].lstrip("0x"),16)
        y = hex(r^p)
        if(y == "0x0"):
            y = "0x00"
        elif(len(y.lstrip("0x")) <= 1):
            y = "0x0"+y.lstrip("0x")
        w4.append(y)
    w5 = []
    w6 = []
    w7 = []
    for i in range(4):
        r = 1
        p = 1
        if(w4[i] == "0x00" or w4[i] == "0x0"):
            r = 0
        else:
            r = int(w4[i].lstrip("0x"),16)
        if(key[1][i] == "0x00" or key[1][i] == "0x0"):
            p = 0
        else:
            p = int(key[1][i].lstrip("0x"),16)
        y = hex(r^p)
        if(y == "0x0"):
            y = "0x00"
        elif(len(y.lstrip("0x")) <= 1):
            y = "0x0"+y.lstrip("0x")
        w5.append(y)
    for i in range(4):
        r = 1
        p = 1
        if(w5[i] == "0x00" or w5[i] == "0x0"):
            r = 0
        else:
            r = int(w5[i].lstrip("0x"),16)
        if(key[2][i] == "0x00" or key[2][i] == "0x0"):
            p = 0
        else:
            p = int(key[2][i].lstrip("0x"),16)
        y = hex(r^p)
        if(y == "0x0"):
            y = "0x00"
        elif(len(y.lstrip("0x")) <= 1):
            y = "0x0"+y.lstrip("0x")
        w6.append(y)
    for i in range(4):
        r = 1
        p = 1
        if(w6[i] == "0x00" or w6[i] == "0x0"):
            r = 0
        else:
            r = int(w6[i].lstrip("0x"),16)
        if(key[3][i] == "0x00" or key[3][i] == "0x0"):
            p = 0
        else:
            p = int(key[3][i].lstrip("0x"),16)
        y = hex(r^p)
        if(y == "0x0"):
            y = "0x00"
        elif(len(y.lstrip("0x")) <= 1):
            y = "0x0"+y.lstrip("0x")
        w7.append(y)
    return [w4,w5,w6,w7]

def addRoundKey(pt,rk):
    for i in range(4):
        for j in range(4):
            x = 0
            y = 0
            if(pt[j][i] != "0x00"):
                x = int(pt[j][i].lstrip("0x"),16)
            if(rk[j][i] != "0x00"):
                y = int(rk[j][i].lstrip("0x"),16)
            z = hex(x^y)
            if(z == "0x0"):
                z = "0x00"
            elif(len(z.lstrip("0x")) <= 1):
                z = "0x0"+z.lstrip("0x")
            pt[j][i] = z
    return pt

def substitute(pt,s_box):
    for i in range(4):
        for j in range(4):
            u = hex(s_box[int(pt[i][j][2],16)][int(pt[i][j][3],16)])
            if(u == "0x0"):
                u = "0x00"
            elif(len(u.lstrip("0x"))<=1):
                u = "0x0"+u.lstrip("0x")
            pt[i][j] = u
    return pt

def shiftRow(pt):
    pt[0][1],pt[1][1],pt[2][1],pt[3][1] = pt[1][1],pt[2][1],pt[3][1],pt[0][1]
    pt[0][2],pt[1][2],pt[2][2],pt[3][2] = pt[2][2],pt[3][2],pt[0][2],pt[1][2]
    pt[0][3],pt[1][3],pt[2][3],pt[3][3] = pt[3][3],pt[0][3],pt[1][3],pt[2][3]
    return pt

def mixMulCol(col,mul2,mul3):
    temp = []
    i = mul2[int(col[0][2],16)][int(col[0][3],16)]
    j = mul3[int(col[1][2],16)][int(col[1][3],16)]
    k = int(col[2],16)
    l = int(col[3],16)
    m = hex(i^j^k^l)
    if(m == "0x0"):
        m = "0x00"
    elif(len(m.lstrip("0x")) <= 1):
        m = "0x0"+m.lstrip("0x")
    temp.append(m)

    i = int(col[0],16)
    j = mul2[int(col[1][2],16)][int(col[1][3],16)]
    k = mul3[int(col[2][2],16)][int(col[2][3],16)]
    l = int(col[3],16)
    m = hex(i^j^k^l)
    if(m == "0x0"):
        m = "0x00"
    elif(len(m.lstrip("0x")) <= 1):
        m = "0x0"+m.lstrip("0x")
    temp.append(m)

    i = int(col[0],16)
    j = int(col[1],16)
    k = mul2[int(col[2][2],16)][int(col[2][3],16)]
    l = mul3[int(col[3][2],16)][int(col[3][3],16)]
    m = hex(i^j^k^l)
    if(m == "0x0"):
        m = "0x00"
    elif(len(m.lstrip("0x")) <= 1):
        m = "0x0"+m.lstrip("0x")
    temp.append(m)

    i = mul3[int(col[0][2],16)][int(col[0][3],16)]
    j = int(col[1],16)
    k = int(col[2],16)
    l = mul2[int(col[3][2],16)][int(col[3][3],16)]
    m = hex(i^j^k^l)
    if(m == "0x0"):
        m = "0x00"
    elif(len(m.lstrip("0x")) <= 1):
        m = "0x0"+m.lstrip("0x")
    temp.append(m)
    return temp
def mixCol(mul2,mul3,pt):
    res = []
    for i in range(4):
        temp = []
        temp.append(pt[i][0])
        temp.append(pt[i][1])
        temp.append(pt[i][2])
        temp.append(pt[i][3])
        res.append(mixMulCol(temp,mul2,mul3))
    return res

def printMatrix(m):
    for i in range(4):
        for j in range(4):
            y = m[j][i]
            if(y == "0x00"):
                y = "00"
            elif(len(y.lstrip("0x")) <= 1):
                y = "0"+y.lstrip("0x")
            else:
                y = y.lstrip("0x")
            print(y.upper(),end=" ")
        print(" ")
def printCipher(m):
    for i in range(4):
        for j in range(4):
            y = m[i][j]
            if(y == "0x00"):
                y = "00"
            elif(len(y.lstrip("0x")) <= 1):
                y = "0"+y.lstrip("0x")
            else:
                y = y.lstrip("0x")
            print(y.upper(),end=" ")
    print(" ")