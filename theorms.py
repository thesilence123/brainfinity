from theorm import Theorm, Clause, Given
import numbers

zero_axiom = Theorm('Zero Axiom', Given([Clause('a', '==', 0), Clause('b', 'isinstance()', 'numbers.Number')]),
                    'a * b == 0')

commutative_addition = Theorm('Addition Commutativity', Given([Clause('a', 'isinstance()', 'numbers.Number'),
                                                               Clause('b', 'isinstance()', 'numbers.Number')]),
                              'a + b == b + a')
