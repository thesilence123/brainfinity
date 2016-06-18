import itertools


def ordered_pairses(member_signs, givens):
    for x in itertools.permutations(givens, len(member_signs)):
        yield zip(member_signs, x)
