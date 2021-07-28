fname = input("Enter file name: ")
fh=open(fname)
count=0
tot=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    str=line
    cpos=str.find(':')
    piece=str[cpos+1:]
    count=count+1
    tot=tot+float(piece)
print("Average spam confidence:",tot/count)
