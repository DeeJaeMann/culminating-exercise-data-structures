import pytest
from tower_of_hanoi import tower_of_hanoi

"""
Tests for source disk "A", destination disk "C
"""
def test_tower_of_hanoi_with_0_disks():
    assert tower_of_hanoi(0, "A", "C", "B", []) == []

def test_tower_of_hanoi_with_1_disk():
    assert tower_of_hanoi(1, "A", "C", "B", []) == ["Move disk 1 from A to C"]

def test_tower_of_hanoi_with_2_disks():
    assert tower_of_hanoi(2, "A", "C", "B", []) == ["Move disk 1 from A to B", "Move disk 2 from A to C", "Move disk 1 from B to C"]

def test_tower_of_hanoi_with_3_disks():
    assert tower_of_hanoi(3, "A", "C", "B", []) == ["Move disk 1 from A to C", "Move disk 2 from A to B", "Move disk 1 from C to B", "Move disk 3 from A to C", "Move disk 1 from B to A", "Move disk 2 from B to C", "Move disk 1 from A to C"]

def test_tower_of_hanoi_with_4_disks():
    assert tower_of_hanoi(4, "A", "C", "B", []) == ["Move disk 1 from A to B", "Move disk 2 from A to C", "Move disk 1 from B to C", "Move disk 3 from A to B", "Move disk 1 from C to A", "Move disk 2 from C to B", "Move disk 1 from A to B", "Move disk 4 from A to C", "Move disk 1 from B to C", "Move disk 2 from B to A", "Move disk 1 from C to A", "Move disk 3 from B to C", "Move disk 1 from A to B", "Move disk 2 from A to C", "Move disk 1 from B to C"]

def test_tower_of_hanoi_with_5_disks():
    assert tower_of_hanoi(5, "A", "C", "B", []) == ["Move disk 1 from A to C", "Move disk 2 from A to B", "Move disk 1 from C to B", "Move disk 3 from A to C", "Move disk 1 from B to A", "Move disk 2 from B to C", "Move disk 1 from A to C", "Move disk 4 from A to B", "Move disk 1 from C to B", "Move disk 2 from C to A", "Move disk 1 from B to A", "Move disk 3 from C to B", "Move disk 1 from A to C", "Move disk 2 from A to B", "Move disk 1 from C to B", "Move disk 5 from A to C", "Move disk 1 from B to A", "Move disk 2 from B to C", "Move disk 1 from A to C", "Move disk 3 from B to A", "Move disk 1 from C to B", "Move disk 2 from C to A", "Move disk 1 from B to A", "Move disk 4 from B to C", "Move disk 1 from A to C", "Move disk 2 from A to B", "Move disk 1 from C to B", "Move disk 3 from A to C", "Move disk 1 from B to A", "Move disk 2 from B to C", "Move disk 1 from A to C"]

"""
Tests for source disk "A", destination disk "B
"""

def test_tower_of_hanoi_with_0_disks():
    assert tower_of_hanoi(0, "A", "B", "C", []) == []

def test_tower_of_hanoi_with_1_disk():
    assert tower_of_hanoi(1, "A", "B", "C", []) == ["Move disk 1 from A to B"]

def test_tower_of_hanoi_with_2_disks():
    assert tower_of_hanoi(2, "A", "B", "C", []) == ["Move disk 1 from A to C", "Move disk 2 from A to B", "Move disk 1 from C to B"]

def test_tower_of_hanoi_with_4_disks():
    assert tower_of_hanoi(4, "A", "B", "C", []) == ["Move disk 1 from A to C", "Move disk 2 from A to B", "Move disk 1 from C to B", "Move disk 3 from A to C", "Move disk 1 from B to A", "Move disk 2 from B to C", "Move disk 1 from A to C", "Move disk 4 from A to B", "Move disk 1 from C to B", "Move disk 2 from C to A", "Move disk 1 from B to A", "Move disk 3 from C to B", "Move disk 1 from A to C", "Move disk 2 from A to B", "Move disk 1 from C to B"]

"""
Source disk C destination disk A
"""

def test_tower_of_hanoi_with_0_disks():
    assert tower_of_hanoi(0, "C", "A", "B", []) == []

def test_tower_of_hanoi_with_1_disk():
    assert tower_of_hanoi(1, "C", "A", "B", []) == ["Move disk 1 from C to A"]

def test_tower_of_hanoi_with_2_disks():
    assert tower_of_hanoi(2, "C", "A", "B", []) == ["Move disk 1 from C to B", "Move disk 2 from C to A", "Move disk 1 from B to A"]

def test_tower_of_hanoi_with_3_disks():
    assert tower_of_hanoi(3, "C", "A", "B", []) == ["Move disk 1 from C to A", "Move disk 2 from C to B", "Move disk 1 from A to B", "Move disk 3 from C to A", "Move disk 1 from B to C", "Move disk 2 from B to A", "Move disk 1 from C to A"]

def test_tower_of_hanoi_with_4_disks():
    assert tower_of_hanoi(4, "C", "A", "B", []) == ["Move disk 1 from C to B", "Move disk 2 from C to A", "Move disk 1 from B to A", "Move disk 3 from C to B", "Move disk 1 from A to C", "Move disk 2 from A to B", "Move disk 1 from C to B", "Move disk 4 from C to A", "Move disk 1 from B to A", "Move disk 2 from B to C", "Move disk 1 from A to C", "Move disk 3 from B to A", "Move disk 1 from C to B", "Move disk 2 from C to A", "Move disk 1 from B to A"]

def test_tower_of_hanoi_with_5_disks():
    assert tower_of_hanoi(5, "C", "A", "B", []) == ["Move disk 1 from C to A", "Move disk 2 from C to B", "Move disk 1 from A to B", "Move disk 3 from C to A", "Move disk 1 from B to C", "Move disk 2 from B to A", "Move disk 1 from C to A", "Move disk 4 from C to B", "Move disk 1 from A to B", "Move disk 2 from A to C", "Move disk 1 from B to C", "Move disk 3 from A to B", "Move disk 1 from C to A", "Move disk 2 from C to B", "Move disk 1 from A to B", "Move disk 5 from C to A", "Move disk 1 from B to C", "Move disk 2 from B to A", "Move disk 1 from C to A", "Move disk 3 from B to C", "Move disk 1 from A to B", "Move disk 2 from A to C", "Move disk 1 from B to C", "Move disk 4 from B to A", "Move disk 1 from C to A", "Move disk 2 from C to B", "Move disk 1 from A to B", "Move disk 3 from C to A", "Move disk 1 from B to C", "Move disk 2 from B to A", "Move disk 1 from C to A"]

"""
Source disk B destination disk C
"""

def test_tower_of_hanoi_with_0_disks():
    assert tower_of_hanoi(0, "B", "C", "A", []) == []

def test_tower_of_hanoi_with_1_disk():
    assert tower_of_hanoi(1, "B", "C", "A", []) == ["Move disk 1 from B to C"]

def test_tower_of_hanoi_with_2_disks():
    assert tower_of_hanoi(2, "B", "C", "A", []) == ["Move disk 1 from B to A", "Move disk 2 from B to C", "Move disk 1 from A to C"]

def test_tower_of_hanoi_with_3_disks():
    assert tower_of_hanoi(3, "B", "C", "A", []) == ["Move disk 1 from B to C", "Move disk 2 from B to A", "Move disk 1 from C to A", "Move disk 3 from B to C", "Move disk 1 from A to B", "Move disk 2 from A to C", "Move disk 1 from B to C"]

def test_tower_of_hanoi_with_4_disks():
    assert tower_of_hanoi(4, "B", "C", "A", []) == ["Move disk 1 from B to A", "Move disk 2 from B to C", "Move disk 1 from A to C", "Move disk 3 from B to A", "Move disk 1 from C to B", "Move disk 2 from C to A", "Move disk 1 from B to A", "Move disk 4 from B to C", "Move disk 1 from A to C", "Move disk 2 from A to B", "Move disk 1 from C to B", "Move disk 3 from A to C", "Move disk 1 from B to A", "Move disk 2 from B to C", "Move disk 1 from A to C"]

def test_tower_of_hanoi_with_5_disks():
    assert tower_of_hanoi(5, "B", "C", "A", []) == ["Move disk 1 from B to C", "Move disk 2 from B to A", "Move disk 1 from C to A", "Move disk 3 from B to C", "Move disk 1 from A to B", "Move disk 2 from A to C", "Move disk 1 from B to C", "Move disk 4 from B to A", "Move disk 1 from C to A", "Move disk 2 from C to B", "Move disk 1 from A to B", "Move disk 3 from C to A", "Move disk 1 from B to C", "Move disk 2 from B to A", "Move disk 1 from C to A", "Move disk 5 from B to C", "Move disk 1 from A to B", "Move disk 2 from A to C", "Move disk 1 from B to C", "Move disk 3 from A to B", "Move disk 1 from C to A", "Move disk 2 from C to B", "Move disk 1 from A to B", "Move disk 4 from A to C", "Move disk 1 from B to C", "Move disk 2 from B to A", "Move disk 1 from C to A", "Move disk 3 from B to C", "Move disk 1 from A to B", "Move disk 2 from A to C", "Move disk 1 from B to C"]

if __name__ == "__main__":
    pytest.main()