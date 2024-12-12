from sequencegen import make_sequence, save_sequence, has_repetitions

def test_has_repetitions():
    trials = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert has_repetitions(trials, 1) == False
    trials = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    assert has_repetitions(trials, 1) == True
    # trials = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # assert has_repetitions(trials, 2) == False
    # trials = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    # assert has_repetitions(trials, 2) == False
    # trials = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    # assert has_repetitions(trials, 3) == True