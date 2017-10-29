import pytest
from nose.tools import *
from ex47.game import Room, Human

def test_room():
    gold = Room("GoldRoom",
                """This room has gold in it you can grab. There's a
                door to the north.""")
    assert_equal(gold.name,  "GoldRoom")
    assert_equal(gold.paths, {})

def test_room_paths():
    # r for room variable
    center = Room("Center", "Test room called hall")
    north = Room("North", "Test room called kitchen")
    south = Room("South", "Test room called Dungeon")

    center.add_paths({'north': north, 'south': south})
    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)

def test_map():
    start = Room("Start", "You are in a hall you can go through a north door")
    north = Room("Kitchen", "You mum's kitchen nice! you can go West")
    west = Room("Dungeon", "It dark here almost like a dungeon you can go South" )
    south = Room("GoldRoom", "Oh yeah found my neXt box let's play a game")

    start.add_paths({'north': north, 'south': start})
    north.add_paths({'west': west, 'east': north})
    west.add_paths({'south': south, 'east': west})

    assert_equal(start.go('north'), north)
    assert_equal(start.go('south'), start)
    # do not understand this principle
    assert_equal(north.go('west'), west)
    assert_equal(north.go('east'), north)
    assert_equal(west.go('south'), south)



def test_player():
    NP1 = Human("jack", 50, 100)
    NP2 = Human("daniel", 40, 90)

    assert_equal(NP1.name, "jack")
    assert_equal(NP1.style, {})

def test_style():

    fighter = Human("bob", 50, 100)
    wizard = Human("jane", 40, 90)

    fighter.add_style({'fighter': fighter})
    wizard.add_style({'wizard': wizard})

    assert_equal(fighter.update_style('fighter'), fighter)
    assert_equal(wizard.update_style('wizard'), wizard)
