from nose.tools import *

def setup():
    print "Setup!"

def teardown():
    print "Teardown"

def test_basic():
    assert_equals(2, 1 + 1)
