import pytest

from ordinal import ordinal


@pytest.mark.parametrize(
    'number, suffix',
    [  # Single digits
        (0, 'th'),
        (1, 'st'),
        (2, 'nd'),
        (3, 'rd'),
        (4, 'th'),
        (5, 'th'),
        (6, 'th'),
        (7, 'th'),
        (8, 'th'),
        (9, 'th'),
        (10, 'th'),
        # Tweens/teens - all 'th'
        (11, 'th'),
        (12, 'th'),
        (13, 'th'),
        (14, 'th'),
        (15, 'th'),
        (16, 'th'),
        (17, 'th'),
        (18, 'th'),
        (19, 'th'),
        # Assorted
        (20, 'th'),
        (21, 'st'),
        (22, 'nd'),
        (23, 'rd'),
        (24, 'th'),
        (25, 'th'),
        (40, 'th'),
        (51, 'st'),
        (72, 'nd'),
        (93, 'rd'),
        # Larger numbers
        (200, 'th'),
        (251, 'st'),
        (372, 'nd'),
        (463, 'rd'),
        (889, 'th'),
        (910, 'th'),
        (4500, 'th'),
        (5671, 'st'),
        (6782, 'nd'),
        (7893, 'rd'),
        (8904, 'th'),
        (9108, 'th'),
    ])
def test_ordinal(number, suffix):
    assert ordinal(number) == suffix
