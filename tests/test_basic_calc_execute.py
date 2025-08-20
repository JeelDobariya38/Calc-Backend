from calc import calc_execute


def test_whitespace_validation():
    code = "   \t \n"
    result = calc_execute(code)
    assert result == 0


def test_recognise_of_numbers():
    code = ["5836", "6", "-552", "5.8", "23.75"]
    exp_res = [5836.0, 6.0, -552.0, 5.8, 23.75]
    for i in range(len(code)):
        res = calc_execute(code[i])
        assert res == exp_res[i]


def test_operation_with_neg_num():
    res1 = calc_execute("6 - -9")
    res2 = calc_execute("-7 - 9")
    res3 = calc_execute("-7 + 8")
    res4 = calc_execute("7 + -8")

    assert res1 == 15
    assert res2 == -16
    assert res3 == 1
    assert res4 == -1


def test_priority_operation():
    res1 = calc_execute("7 + (8 * 9)")
    res2 = calc_execute("7 + (8 * 9) + 1")
    res3 = calc_execute("(7 + 9)")
    res4 = calc_execute("(7 + 8) / 2")

    assert res1 == 79
    assert res2 == 80
    assert res3 == 16
    assert res4 == 7.5


def test_without_space_expression():
    res1 = calc_execute("7+18-9")
    res2 = calc_execute("7.8+(8*9)+-1")
    res3 = calc_execute("(7+9)")
    res4 = calc_execute("(7+8)/2")
    res5 = calc_execute("7.8+-8+9")

    assert res1 == 16
    assert res2 == 78.8
    assert res3 == 16
    assert res4 == 7.5
    assert res5 == 8.8
