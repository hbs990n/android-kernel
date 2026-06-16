import re, sys
with open(sys.argv[1]) as f:
    c = f.read()
c = re.sub(r'^print (.)', r'print(\1', c, flags=re.MULTILINE)
with open(sys.argv[1], 'w') as f:
    f.write(c)
