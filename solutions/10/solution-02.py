# Notebook 10 - solution-02

result = np.copy(x)
for i in range(s,e):
    neighbourhood = x[i-half_width:i+half_width+1]
    result[i] = np.median(neighbourhood)
    
print(f'result = {result}')