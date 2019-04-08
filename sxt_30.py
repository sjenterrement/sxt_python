import io
s="hello.sxt"
sio=io.StringIO(s)
print(sio.getvalue())
sio.seek(6)
sio.write("g")
print(sio.getvalue())
