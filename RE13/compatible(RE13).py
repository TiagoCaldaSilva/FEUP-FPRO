def compatible(A,B):
    if len(A[0]) == len(B):
        return 'A and B can be multiplied'
    else:
        return AssertionError('A and B cannot be multiplied',)
