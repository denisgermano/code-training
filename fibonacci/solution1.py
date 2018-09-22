def fibonacci(position):
    fibNMinusTwo = 0
    fibNMinusOne = 1

    initials = (fibNMinusTwo, fibNMinusOne)
    if position < 2:
        return initials[position]

    for _ in range(position):
        fibN = fibNMinusOne + fibNMinusTwo
        fibNMinusOne, fibNMinusTwo = fibNMinusTwo, fibN

    return fibN
