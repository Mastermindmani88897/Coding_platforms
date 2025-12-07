def isPalinArray(arr):
    for x in arr:
        if str(x) != str(x)[::-1]:
            return False
    return True
