def func(a):
    try:
        return a.strip()
    except Exception as e:
        pass
    return False

v = func("213")
v2 = 123 if not v else v
print(v2)

R=True + 100
print(R)