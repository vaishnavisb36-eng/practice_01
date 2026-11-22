from simple_int import calculate_si

def test_SI():
    assert calculate_si(5000, 2, 2)==200

    def test_SIZero():
        assert calculate_si(7000, 3, 2)==420