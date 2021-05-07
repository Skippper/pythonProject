

tupl = ('html', 'js', 'css', 'python')

for item in tupl:
     print(tupl.index(item) + 1 , item)


print('=====')

for i,item in enumerate(tupl,1):
    print(i,item)