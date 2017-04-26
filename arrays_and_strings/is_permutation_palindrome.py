# Given a string, is there a permutation of the string that is a palindrome

def permutation_palindrome(string):
    d = {}
    for s in string:
        if s != " ":
            if s not in d.keys():
                d[s] = 1
            else:
                d[s] += 1

    odd_count = 0

    for k in d.keys():
        if d[k] % 2 == 0:
            continue
        else:
            odd_count += 1

        if odd_count > 1:
            return False

    return True


s1 = "racecar"
s2 = "bunny rabbit"
s3 = "abba"

test = [s1, s2, s3]

for t in test:
    print permutation_palindrome(t)
