f=open('Dinner.dat')                                    # x.txt python ,
l1=f.readlines()                                   # l1 list, , '/n'
l1=[x.split('\t') for x in l1]
l1=[[x[0],x[1].replace('\n','')] for x in l1]   # '/n'
f.close()                                                   #

f=('y.txt','w')# ,
l2=[[x[0],x[1]] for x in l1]
l2.sort()
l2=[x[0]+'\t'+x[1]+'\n' for x in l2]
f.writelines(l2)
f.close()
