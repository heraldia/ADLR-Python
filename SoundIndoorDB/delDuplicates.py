from sets import Set
file("songList.txt","w").writelines( Set(file("result.txt", "r").readlines()) )
