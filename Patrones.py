import sys

s = sys.argv[1]
new_s = s
while(len(new_s) >= len(s)/2):
    i = (new_s+new_s).find(new_s, 1, -1)
    a = None if i == -1 else s[:i]
    if a:
        print (a)
        break
    new_s = new_s[:-1]