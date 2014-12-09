from sets import Set
file("result2.txt","w").writelines( Set(file("result.txt", "r").readlines()) )
