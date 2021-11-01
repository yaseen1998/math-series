from math_series import __version__
from math_series.series import sum_series
from math_series.series import lucas
from math_series.series import fibonacci




def test_version():
    assert __version__ == '0.1.0'

def test_sum_series_fibonacci():
    expected=13
    actual=sum_series(7)
    assert expected == actual
    
def test_sum_series_lucas():
    expected=29
    actual=sum_series(7,2,1)
    assert expected == actual

def test_lucas():
    expected=29
    actual=lucas(7)
    assert expected == actual

def test_fibonacci():
    expected=13
    actual=fibonacci(7)
    assert expected == actual

