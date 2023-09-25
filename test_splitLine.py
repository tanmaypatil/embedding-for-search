
from store import *

def test_find_id():
    line = '[test-id]         Test009BlocksAndModels'
    tokens = processLine(line,None)
    assert tokens[0] == 'test-id'
    assert tokens[1] == 'Test009BlocksAndModels'

def test_find_id2():
    line = '[test-severity]   1 - critical'
    tokens = processLine(line,None)
    assert tokens[0] == 'test-severity'
    assert tokens[1] == '1 - critical'

def test_find_actions():
    line = '[test-actions]'
    tokens = processLine(line,None)
    assert tokens[0] == 'test-actions'
    assert tokens[1] == ''

def test_find_actions1():
    line = '1. go to url {open-project application}'
    tokens = processLine(line,'test-actions')
    assert tokens[0] == 'test-actions-1'
    assert tokens[1] == 'go to url {open-project application}'

def test_find_actions6():
    line = '6. close browser'
    tokens = processLine(line,'test-actions')
    assert tokens[0] == 'test-actions-6'
    assert tokens[1] == 'close browser'
    
    
