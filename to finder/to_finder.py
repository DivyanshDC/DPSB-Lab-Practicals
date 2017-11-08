y=0
try:
    fobj=open("tofinder.txt",'r')
    a=fobj.readline()
    while a:
        print a
        x=len(a)
        for i in range(x):
            if a[i].upper()=='T':
                if a[i+1].upper()=='O':
                    if (a[i-1] ==" ") or (a[i-1] == "\n"):
                        try:
                            if (a[i+2] == " ") or (a[i+2] == "\n"):
                                y+=1
                        except IndexError:
                            y+=1
                            pass
        print y
        a=fobj.readline()
    print "Search completed."
    fobj.close()
except IOError:
    print "file doesn't exist"
    pass
except EOFError:
    pass
print 'Number of "to" are : ', y
