from calc import calc_execute


def test_addition_of_numbers():
    res1 = calc_execute("1 + 1")
    res2 = calc_execute("1 + -4 + 6")
    res3 = calc_execute("6 + 7 + 8")
    res4 = calc_execute("8.5 + 5.4  + 3")
    res5 = calc_execute("-8.5 + 7")

    assert res1 == 2.0
    assert res2 == 3.0
    assert res3 == 21.0
    assert res4 == 16.9
    assert res5 == -1.5


def test_subtraction_of_numbers():
    res1 = calc_execute("1 - 1")
    res2 = calc_execute("1 - 4 - 6")
    res3 = calc_execute("16 - 7 - -8")
    res4 = calc_execute("8.5 - 5.4  - 3")

    assert res1 == 0.0
    assert res2 == -9.0
    assert res3 == 17.0
    assert round(res4) == 0


def test_multiplaction_of_numbers():
    res1 = calc_execute("1 * 1")
    res2 = calc_execute("1 x -4 x 6")
    res3 = calc_execute("6 x 7 x 8")
    res4 = calc_execute("8.5 x 5.4 x 3")
    res5 = calc_execute("-8.5 x 7")

    assert res1 == 1.0
    assert res2 == -24.0
    assert res3 == 336
    assert res4 == 137.70000000000002
    assert res5 == -59.5


def test_division_of_numbers():
    res1 = calc_execute("1 / 1")
    res2 = calc_execute("1 / 4 / 6")
    res3 = calc_execute("16 / 7 / -8")
    res4 = calc_execute("8.5 / 5.4 / 3")

    assert res1 == 1
    assert res2 == 0.041666666666666664
    assert res3 == -0.2857142857142857
    assert res4 == 0.5246913580246914
