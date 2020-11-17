ll =[1,1,2,2,3,3,5,5,4,7,7]
c = [one for one in ll if one not in  ll[ll.index(one)+1:]]
print( c)