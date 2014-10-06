def remove_duplicates(l):
    new = []
    for e in l:
        if e not in new:
            new.append(e)
        else: 
            False
    return new
            
x = [1,1,2,2]

print remove_duplicates(x)
