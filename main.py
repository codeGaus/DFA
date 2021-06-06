from DFA import *


DFA1 = DFA({'0', '1'}, ['q0', 'q1', 'q2'], 'q0', ['q0'], {
    'q0': {
        '0': 'q2',
        '1': 'q1'
    },
    'q1': {
        '0': 'q1',
        '1': 'q1'
    },
    'q2': {
        '0': 'q1',
        '1': 'q0'
    }
})

print(DFA1.test('010101'))

