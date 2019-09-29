import pafy
v = pafy.new("cUowksRM7x0")
s = v.getbest(preftype = "mp4", ftypestrict = False) 
print('size is %s' % s.get_filesize())
filename = s.download()
print(filename)


