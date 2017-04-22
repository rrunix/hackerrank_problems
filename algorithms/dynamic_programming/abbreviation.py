#source https://www.hackerrank.com/challenges/abbr/

def can_transform(text, query):
    # Influenced by https://www.hackerrank.com/eugalt?hr_r=1 answer.

    text = list(text)
    query = list(query)

    query_len = len(query)

    #Uppercase letters from text
    fixed_text = list(filter(lambda x: x.isupper(), text))

    # Equals
    if fixed_text == query:
        return "YES"

    # Impossible to be equals
    elif not set(fixed_text).issubset(set(query)) or len(fixed_text) > len(query):
        return "NO"

    # Query window
    dp = [True] + [False] * len(query)

    # Initialize with first letter
    i = 0
    while i < query_len and text[i].upper() == query[i]:
        i += 1
        dp[i] = True

    for i in range(len(text) - len(query)):
        for j, b in enumerate(query):
            a = text[i + j + 1]

            if a.isupper():
                dp[j + 1] = dp[j] and a == b
            elif a.upper() == b:
                dp[j + 1] = dp[j] or dp[j + 1]

    return "YES" if dp[-1] else "NO"

N = int(input())
for _ in range(N):
    print(can_transform(input(), input()))
