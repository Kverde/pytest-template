from main import sum2

def test_sum2():
    assert sum2(0, 0) == 0
    assert sum2(1, 1) == 2
    assert sum2(2, 3) == 5
    assert sum2(10, 15) == 25

