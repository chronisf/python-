with open('inputdata.txt',) as f:
    content=f.read().splitlines()
numlist=[]
for i in content:
    
    numbers=i.split(',')
    for n in numbers:
        import math 
        numlist.append(float(n))
        s=sum(numlist)
        N=len(numlist)
        m=s/N
        a=(((float(n)-m)**2)/N)
        ta=math.sqrt(a)
print(m)
print(ta)
with open ('outputdata.txt', 'w') as af:
    af.write('Μέσος όρος -'+str(m))
    af.write('\nΤυπική απόκλιση-'+str(ta))
    

