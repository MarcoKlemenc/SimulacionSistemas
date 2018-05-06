import sys

s = sys.argv[1]
i = (s+s).find(s, 1, -1)
print (None if i == -1 else s[:i])