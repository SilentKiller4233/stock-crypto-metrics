from helpers import calculate_pe, calculate_pb, calculate_roe, safe_divide

def test_safe_divide():
    assert safe_divide(10, 2) == 5
    assert safe_divide(10, 0) is None
    assert safe_divide(None, 5) is None

def test_calculate_pe():
    assert calculate_pe(100, 10) == 10

def test_calculate_pb():
    assert calculate_pb(100, 25) == 4

def test_calculate_roe():
    assert calculate_roe(200, 400) == 0.5