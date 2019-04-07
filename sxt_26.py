#测试join
import time
time01=time.time()#起始时间
a=""
for i in range(1000000):
    a+='jungkook'
time02=time.time()#终止时间
print("运算时间: "+str(time02-time01))

time03=time.time()
jungkook=[]
for i in range(1000000):
    jungkook.append("jungkook")
a="".join(jungkook)
time04=time.time()
print("运算时间："+str(time04-time03))
