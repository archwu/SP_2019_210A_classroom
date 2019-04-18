def fib(n):
    """Return nth fibonacci number with recursion."""
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib (n - 2)

def fib2(n):
    """Another function that returns nth fibonacci number with low time and space used."""
    a, b = 0, 1
    if n == 0:
        return 0
    for _ in range(n - 1):
        a, b = b, a + b
    return b

def lucas(n):
    a, b = 2, 1
    if n == 0:
        return 2
    for _ in range(n - 1):
        a, b = b, a + b
    return b


def test_fib():
    """Test the correctness of above functions"""
    assert fib(0) == 0
    assert fib2(0) == 0
    assert fib(1) == 1
    assert fib2(1) == 1
    assert fib(2) == 1
    assert fib2(2) == 1
    assert fib(3) == 2
    assert fib2(3) == 2
    assert fib(4) == 3
    assert fib2(4) == 3
    assert fib(5) == 5
    assert fib2(5) == 5
    assert fib(6) == 8
    assert fib2(6) == 8
    assert fib(7) == 13
    assert fib2(7) == 13
    assert fib(8) == 21
    assert fib2(8) == 21
    assert fib(9) == 34
    assert fib2(9) == 34
    assert fib2(1000) == 43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875
