

	

from development.main_portless import find_ips

def func(x):
    return x + 1



def test_IP():
    find_ips("555.555.555.555")

def test_answer():
    assert func(3) == 4, "Should be 4"