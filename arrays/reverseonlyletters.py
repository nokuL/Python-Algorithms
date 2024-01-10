def reverseonlyletters(string):
    arr = list(string)

    start = 0
    end = len(string) - 1

    while start < end:
        if arr[start].isalpha() and arr[end].isalpha():
            arr[start], arr[end] = arr[end], arr[start]
        elif not arr[start].isalpha():
            start += 1
        elif not arr[end].isalpha():
            end -= 1
    return "".join(arr)
