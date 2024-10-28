from times import  time_range, compute_overlap_time
import pytest

def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(large, short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]

    assert result == expected

def test_time_range_no_overlap():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 10:30:00")
    short = time_range("2010-01-12 11:30:00", "2010-01-12 12:00:00", 2, 60)
    result = compute_overlap_time(large, short)
    expected = []

    assert result == expected

def test_time_range_with_time_intervals():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 3, 60)
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(large, short)
    expected = [('2010-01-12 10:00:00', '2010-01-12 10:39:20'), ('2010-01-12 10:40:20', '2010-01-12 11:19:40'), ('2010-01-12 11:20:40', '2010-01-12 12:00:00')], [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]

    assert result == expected

def test_times_ending_and_starting_same():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00")
    short = time_range("2010-01-12 11:00:00", "2010-01-12 12:00:00", 2, 60)
    result = compute_overlap_time(large, short)
    expected = [('2010-01-12 10:00:00', '2010-01-12 11:00:00')], [('2010-01-12 11:00:00', '2010-01-12 11:29:30'), ('2010-01-12 11:30:30', '2010-01-12 12:00:00')]

    assert result == expected

def test_time_backwards():
    with pytest.raises(ValueError):
        assert time_range("2010-01-12 12:00:00", "2010-01-12 10:00:00")
    

if __name__ == "__main__":
    test_times_ending_and_starting_same()
    print("Test passed!")


