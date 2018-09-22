def fibonacci(position):
    fibNMinusTwo = 0
    fibNMinusOne = 1

    initials = (fibNMinusTwo, fibNMinusOne)
    if position < 2:
        return initials[position]

    return fibonacci(position - 1) + fibonacci(position - 2)
