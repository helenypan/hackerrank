import re
m=re.search(r'([0-9a-zA-Z])\1',input().strip())
if m:
    print(m.group(1))
else:
    print(-1)