# Array of tests to run (in order)
# Each test contains
#   description - 
#   steps - A list of steps to perform, each step can have
#       inputs - A list of tuples for the inputs to apply at that step
#       *time - The time (in ms) to wait before continuing to the next step 
#           and before checking expected values for this step. The time should be a multiple of
#           the period of the system
#       *iterations - The number of clock ticks to wait (periods)
#       expected - The expected value at the end of this step (after the "time" has elapsed.) 
#           If this value is incorrect the test will fail early before completing.
#       * only one of these should be used
#   expected - The expected output (as a list of tuples) at the end of this test
# An example set of tests is shown below. It is important to note that these tests are not "unit tests" in 
# that they are not ran in isolation but in the order shown and the state of the device is not reset or 
# altered in between executions (unless preconditions are used).
tests = [ {'description': 'PINA: 15, PINB: 15, PINC: 15 => PORTD: 0b11010100',
    'steps': [ {'inputs': [('PINA',0x0F),('PINB',0x0F),('PINC',0x0F)], 'iterations': 5 } ],
    'expected': [('PORTD',0xB4)],
    },

    {'description': 'PINA: 20, PINB: 50, PINC: 110 => PORTD: 0b10110111',
    'steps': [ {'inputs': [('PINA',0x14),('PINB',0x32),('PINC',0x6E)], 'iterations': 5 } ],
    'expected': [('PORTD',0xB7)],
    },
    
    {'description': 'PINA: 10, PINB: 20, PINC: 91 => PORTD: 0b11110010',
    'steps': [ {'inputs': [('PINA',0x0A),('PINB',0x14),('PINC',0x5B)], 'iterations': 5 } ],
    'expected': [('PORTD',0xF2)],
    },

    {'description': 'PINA: 91, PINB: 20, PINC: 10 => PORTD: 0b11110010',
    'steps': [ {'inputs': [('PINA',0x0A),('PINB',0x14),('PINC',0x5B)], 'iterations': 5 } ],
    'expected': [('PORTD',0xF2)],
    },

    {'description': 'PINA: 40, PINB: 50, PINC: 60 => PORTD: 0b10010101',
    'steps': [ {'inputs': [('PINA',0x28),('PINB',0x32),('PINC',0x3C)], 'iterations': 5 } ],
    'expected': [('PORTD',0x95)],
    },

    {'description': 'PINA: 0, PINB: 0, PINC: 0 => PORTD: 0b00000000',
    'steps': [ {'inputs': [('PINA',0x00),('PINB',0x00),('PINC',0x00)], 'iterations': 5 } ],
    'expected': [('PORTD',0x00)],
    },    
]

# Optionally you can add a set of "watch" variables these need to be global or static and may need
# to be scoped at the function level (for static variables) if there are naming conflicts. The 
# variables listed here will display everytime you hit (and stop at) a breakpoint
watch = ['weight','tmpD']
