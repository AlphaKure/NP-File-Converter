#TEST FOR GET previewTime

with open('','rb')as f: #<-Ender the file(acb)
    Data=f.read().hex()
    f.close()

print(Data[8620:8626]) #previewTimeStart
print(int(Data[8620:8626],16))

print('##################')
print(Data[8648:8654]) #previewTimeEnd
print(int(Data[8648:8654],16))