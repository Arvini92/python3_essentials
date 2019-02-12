t = 1, 2, 3, 4, 5
t = (1,)
print(len(t))
print(max(t))
x = [1, 2, 3]
t = (range(25))
print(10 in t)
print(50 not in t)
print(t.count(5))
x.extend(range(20))
print(x)
x.insert(12, 100)
x.remove(12)
del x[12]
x.pop()
x.pop(0)

d = { 'one': 1, 'two': 2}
print('one' in d)
print(d.get('three'))
d.pop('one')

fin = open('utf8.txt', 'r', encoding = 'utf_8')
fout = open('utf8.html', 'w')
outbytes = bytearray()
for line in fin:
    for c in line:
        if ord(c) > 127:
            outbytes += bytes('&#{:04d};'.format(ord(c)), encoding = 'utf_8')
        else: outbytes.append(ord(c))
outstr = str(outbytes,encoding = 'utf_8')
print(outstr, file = fout)
print(outstr)
print('Done.')