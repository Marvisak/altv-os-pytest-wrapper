import alt


def test_hash() -> None:
    """Very basic test example"""
    assert alt.hash("test") == alt.hash("test")
    assert alt.hash("test") != alt.hash("tset")
