'''
This is a naive approach
'''

def naive_pattern_search(txt, pattern):
    
    M = len(pattern)
    N = len(txt)

    # A loop to slide pattern one by one
    for i in range(N-M+1):       

        found = 1

        for j in range(M):

            if txt[i+j] != pattern[j]:
                found = 0
                break

        if found:

            print('Pattern found at index ', i)

txt = 'AABAACAADAABAAABAA'
pattern = 'AABA'

naive_pattern_search(txt, pattern)