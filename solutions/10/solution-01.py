# Notebook 10 - solution-01

half_width = 2
s = half_width
e = len(x)-half_width

for i in range(s,e):
    print(f'center = {i}, values={x[i-half_width:i+half_width+1]}')