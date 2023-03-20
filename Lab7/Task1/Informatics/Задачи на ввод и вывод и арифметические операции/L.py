n = int(input())
h = n // 3600
n = n % 3600
m = n // 60
s = n % 60
sh = str(h % 24)
sm = str(m)
if len(sm)<2:
    sm = "0"+sm
ss = str(s)
if len(ss)<2:
    ss = "0"+ss
print(sh + ':' + sm + ':' + ss)