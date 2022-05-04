d={}

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
for i in range(n):
    ext, mt = input().split() #extension, MIME type
    d[ext.lower()] = mt
    #print("INPUT: {}, {}".format(ext, mt), file=sys.stderr)

for i in range(q):
    fname = input()

    if "." in fname: 
        ext = fname.rsplit(".")[-1:][0].lower()
        if ext in d.keys():
            print(d.get(ext))
        else:
            print("UNKNOWN")
    else:
        print("UNKNOWN")

