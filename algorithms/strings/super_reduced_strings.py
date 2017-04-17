def reduceString(string):
    changed = False
    if len(string) > 1:
        idx_last = 0
        for idx in range(1, len(string)):
            if string[idx] == string[idx_last]:
                string = string[:idx_last] + string[idx + 1:]
                changed = True
                break
            idx_last = idx

    if changed:
        return reduceString(string)
    return string

reducedString = reduceString(input())
if len(reducedString) == 0:
    print("Empty String")
else:
    print(reducedString)



