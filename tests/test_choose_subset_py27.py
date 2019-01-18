"""
Should be compatible within the abaqus python environment.

To test run:

activate <Python 2.7 environment name>
pytest tests/test_subset_np.py

"""
import pytest
import optimal_subrange.py2.choose_subset as cs

def test_subset_np_simple():
    assert cs.choose_subset([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3) == [1, 5, 10]

def test_choose_subset_unsorted():
    assert cs.choose_subset([10, 3, 7, 1, 6], 3, sorted=False) == [1, 6, 10]

def test_choose_subset_float():
    assert cs.choose_subset([5.1, 6.4, 21.9, 17.2, 13.0, 77, 56.1], 4, sorted=False) == [5.1, 21.9, 56.1, 77]