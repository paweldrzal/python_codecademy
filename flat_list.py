#flattening a list

n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]

def flatten(lists):
    results = []
    for li in lists:
        for m in li:
            results.append(m)
    return results

print flatten(n)
#output [1, 2, 3, 4, 5, 6, 7, 8, 9]
