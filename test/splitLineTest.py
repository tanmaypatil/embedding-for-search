
from store import *

def test_find_sched():
    line = '[test-id]         Test009BlocksAndModels'
    tokens = processLine(line)
    assert tokens[0] == 'test-id'
    
