def fibonacci():
    fibNMinusTwo = 0
    fibNMinusOne = 1

    yield fibNMinusTwo
    yield fibNMinusOne

    while True:
        fibN = fibNMinusOne + fibNMinusTwo
        yield fibN
        fibNMinusTwo, fibNMinusOne = fibNMinusOne, fibN
