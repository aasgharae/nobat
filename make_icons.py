import zlib, struct
def png(size, path):
    bg=(15,118,110); fg=(255,255,255)
    t=size//2; w=size//10; L=size//4
    rows=[]
    for y in range(size):
        row=bytearray([0])
        for x in range(size):
            plus=(abs(x-t)<w and abs(y-t)<L) or (abs(y-t)<w and abs(x-t)<L)
            row+=bytes(fg if plus else bg)
        rows.append(bytes(row))
    raw=b''.join(rows)
    def ch(tag,data):
        c=struct.pack('>I',len(data))+tag+data
        return c+struct.pack('>I',zlib.crc32(tag+data)&0xffffffff)
    open(path,'wb').write(b'\x89PNG\r\n\x1a\n'+ch(b'IHDR',struct.pack('>IIBBBBB',size,size,8,2,0,0,0))+ch(b'IDAT',zlib.compress(raw))+ch(b'IEND',b''))
png(192,'docs/icon-192.png'); png(512,'docs/icon-512.png')
