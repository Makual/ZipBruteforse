f = open('passes.txt','w') 


for a in range(0,10):
    for b in range(0,10):
        for c in range(0,10):
            for d in range(0,10):
                f.write('pass' + str(a) + str(b) + str(c) + str(d))
                f.write('\n')
f.close()
print('Готово')
