from guessing_game.game import check_guess


def test_guess_equal_to_target_is_correct():
    assert check_guess(target=50, guess=50) == "correct"


def test_guess_below_target_is_too_low():
    assert check_guess(target=50, guess=30) == "too low"


def test_guess_above_target_is_too_high():
    assert check_guess(target=50, guess=70) == "too high"


def test_boundary_just_below_target():
    assert check_guess(target=50, guess=49) == "too low"


def test_boundary_just_above_target():
    assert check_guess(target=50, guess=51) == "too high"
