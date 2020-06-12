"""Test for my functions."""

from my_module.Animal_crossing_functions import fish_lst, opening, end_chat

def test_opening():
    """Tests opening function"""
    x = opening("ss")
    return x

def test_fish_lst():
    """Tests fish_lst function"""
    assert fish_lst('Yes') == True
    assert isinstance(fish_lst('Yes'), bool)
    assert callable(fish_lst)
    
def test_end_chat():
    """Tests end_chat function"""
    assert end_chat('quit') == True
    assert isinstance(end_chat('quit'), bool)
    assert callable(end_chat)
    