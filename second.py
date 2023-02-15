def caesarCipher(s, k):
    # Write your code here
    a="abcdefghijklmnopqrstuvwxyz"
    A="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cap_alphabets=[i for i in A]
    aplhabets=[i for i in a]
    new_s=""
    for i in s:
        if i in aplhabets:
            indx=aplhabets.index(i)
            if (indx+k) <26:
                new_s+=aplhabets[indx+k]
            else:
                m=(indx+k)-26
                while m>25:
                    m=m-26
                new_s+=aplhabets[m]
        elif i in cap_alphabets:
            indx=cap_alphabets.index(i)
            if (indx+k) <26:
                new_s+=cap_alphabets[indx+k]
            else:
                m=(indx+k)-26
                while m>25:
                    m=m-26
                new_s+=cap_alphabets[m]
        else:
            new_s+=i
    return new_s

def test():
    a = "jnfenbibh-bdejenfbh"
    b = 5
    c = "asdfghjk-lopinbfgf"
    d = 9

    print(caesarCipher(a,b))
    print(caesarCipher(a,b))
    print(caesarCipher(c,d))


test()