import logging
import numbers
from mathematics_logic import ordered_pairses


class Theorm(object):
    def __init__(self, name, given, result):
        super(Theorm, self).__init__()
        self.name = name
        self.given = given
        self.result = result


class Given(object):
    """
    This is the given every theorm has.
    It has a list of clauses about members.
    A member could be a number or a wrapper.
    """
    def __init__(self, clauses):
        self.logger = logging.getLogger(__name__)
        self.clauses = [clause for clause in set(clauses)]
        self.members = dict()

    def is_match(self, givens):
        """
        Gets a list of givens. Returns if it satisfies all the clauses.
        It runs through all the clauses and tries to satisfy. If it succeeds, it assigns a member to what it succeeded to.
        :param givens: List of members to test againts the clause members.
        :return: True if satisfies. False otherwise.
        """
        givens_basket = givens[:]
        member_signs = [clause.member_sign for clause in self.clauses]

        members = {}
        found = True
        for ordered_pairs in ordered_pairses(member_signs, givens):
            for ordered_pair in ordered_pairs:
                self.logger.debug('Ordered pair: %s' % (ordered_pair,))
                members[ordered_pair[0]] = ordered_pair[1]
            for clause in self.clauses:
                if not self.evaluate(clause, members): found = False
            if found:
                self.logger.debug('Found! The members are: %s' % members)
                return True
            members = {}
        self.logger.debug('Not a match.')
        return False

    def evaluate(self, clause, members):
        if clause.op.startswith('.') and not clause.third:
            return eval('members[clause.member_sign]' + clause.op)
        if clause.op.startswith('.') and clause.third:
            return eval(members[clause.member_sign] + clause.op[:-1] + clause.third + clause.op[-1])
        if clause.op == 'isinstance()':
            return eval('isinstance(' + 'members[clause.member_sign]' + ',' + clause.third + ')')
        return eval(members[clause.member_sign] + clause.op + clause.third)




class Clause(object):
    """
    It can be true or false.
    """
    def __init__(self, member_sign, op, third = None):
        super(Clause, self).__init__()
        self.member_sign = member_sign
        self.op = op
        self.third = third
    def __repr__(self):
        return self.member_sign + self.op + self.third if self.third is not None else ''
