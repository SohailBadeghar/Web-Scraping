from sample import add

def test_add_num():
    assert add(1,2) == 4

def test_add_str():
    assert add("a", "b") == "ab"


class TestSample:
    def test_add_num(self):
        assert add(2,2) == 4

    def test_add_str(self):
        assert add("a", "b") == "ab"