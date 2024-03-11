s = "abcdf"
f = "2.0"
i= "1"

def checkContent(x):
    if len(x)>=1 and len(x)<=100:
        try:
            x=int(x)
            return "Intiger"
        except ValueError: pass
        try: 
            x=float(x)
            return "Float"
        except ValueError: pass
        return "String"
print(checkContent(s))
print(checkContent(f))
print(checkContent(i))