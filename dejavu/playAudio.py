import pyglet

filename = "20141103_000124"
prefix ='./mp3t/Living_'
suffix ='.mp3'
fullFilename=prefix+filename+suffix
source=pyglet.media.load(fullFilename)
player=pyglet.media.Player()
player.queue(source)
player.play()
