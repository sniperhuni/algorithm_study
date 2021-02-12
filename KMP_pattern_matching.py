'''
KMP(Knuth Morris Pratt) Pattern searching
'''

# Find The longest proper prefix which is also suffix
def longest_proper_prefix(pat, M):

    # lps[0] is always 0
    length=0
    lps = [0]

    # Start with index i = 1
    i = 1
    while i<M:

        if pat[length] == pat[i]:

            length += 1
            lps.append(length)
            i += 1

        else:

            if length == 0:
                lps.append(0)
                i +=1

            # We will not increase the index to compare with new position
            else:

                length = lps[length-1]

    return lps

def KMP(txt, pattern):

    M = len(pattern)
    N = len(txt)

    lps = longest_proper_prefix(pattern, M)

    i = 0
    j = 0
    while i < N:

        if txt[i] == pattern[j]:

            i += 1
            j += 1

            if j == M:

                print('Pattern Founded at ', (i-j))
                J = lps[j-1]

        else:

            j = lps[j-1]
            if j == 0:
                i += 1


txt = 'ABABDABACDABABCABAB'
pattern = 'ABABCABAB'

KMP(txt, pattern)

