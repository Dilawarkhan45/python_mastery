import pytest
from grades import grade


@pytest.mark.parametrize(
    "marks, expected",
    [
        (32, "Fail"),
        (33, "D"),
        (59, "D"),
        (60, "C"),
        (69, "C"),
        (70, "B"),
        (79, "B"),
        (80, "A")
    ]
)
def test_grade_boundaries(marks, expected):
    assert grade(marks) == expected


def test_marks_above_100():
    with pytest.raises(ValueError):
        grade(101)


def test_negative_marks():
    with pytest.raises(ValueError):
        grade(-1)