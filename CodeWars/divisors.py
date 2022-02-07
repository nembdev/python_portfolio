def divisors(integer):

    results = []

    for i in range(integer + 1):
        # print(i)
        if i == 0:
            continue
        if integer % i == 0:
            results.append(i)

    if results[0] == 1 and results[1] == integer:
        return f"{integer} is prime"
    else:
        results.pop(0)
        results.pop(-1)
        return results
