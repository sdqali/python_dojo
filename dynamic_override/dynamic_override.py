#!/usr/bin/env python

# Override an attribute of a class to take a dynamic value using property()

import datetime

class Foo(object):
    bar = datetime.datetime.now()

instance = Foo()

# Compare the value assigned when the Foo object is initialised.
first_value = instance.bar
second_value = instance.bar
assert(first_value == second_value)

# Override
Foo.bar = property(lambda self: datetime.datetime.now())

# Compare the value assigned after the override
third_value = instance.bar
fourth_value = instance.bar
assert(third_value != fourth_value)
