fname = input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:

    line=line.rstrip()
    wds=line.split()

    for a in wds:
        if a not in lst:
            lst.append(a)
            lst.sort()

print(lst)
        # if b==a:
               #continue
               #lst.append(a)

        #if  b not in a:
            #continue
            #lst.append(b)
        #for b in lst:
        #    if b=lst:
            #    continue
            #    lst.append(b)



        #z
         #  print(a)
        #for g in lst:
        #     if g==a:
        #        continue
        #        lst.append(a)
#print(lst)

        #a=line.find(wds)
    #    if a==wds:
            #lst.append(a)
            #continue
    #if  lst==line:
     # continue
    #lst.append(line)
    #print(wds)
    #lst.sort()
    #print(lst)
