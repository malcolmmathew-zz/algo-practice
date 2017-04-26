def is_unique(string):
    d = set()
    for s in string:
        if s not in d:
            d.add(s)
        else:
            return False
    return True

def is_unique_without_ds(string):
    for i1, s1 in enumerate(string):
        for i2, s2 in enumerate(string):
            if i1 != i2:
                if s1 == s2:
                    return False
    return True

s1 = "hell"
s2 = "octa"
s3 = "anomelisa"

test = [s1, s2, s3]

for t in test:
    print is_unique_without_ds(t)
