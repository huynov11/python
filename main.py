import time
s = str(input('Moi nhap vao : '))
t = time.time()
def BW(s):
    x = s
    ss = [s]
    for i in range(len(s)):
        s = s[-1] + s[:-1]
        ss.append(s)
    ss.sort()
    u = ''.join(x[-1] for x in ss)
    d = ss.index(x)
    return u,d

(u,d) =BW(s)
print('Output u:',u,' d:',d)

(u,d) =BW(s)
print('Time: ',time.time()-t)


