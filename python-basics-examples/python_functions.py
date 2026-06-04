def favorite_martial_art():
        return "bjj"


print(favorite_martial_art())
# This is the same output
my_variable = "bjj"
my_variable

def myfunc():pass

res = myfunc()
print(res)
#result = myfunc()
#print(result)

"""
**Documenting Functions**

It is a very good idea to document functions.  
In Jupyter Notebook and IPython docstrings can be viewed by referring to the function with a ?.  ie.

```
In [2]: favorite_martial_art_with_docstring?
Signature: favorite_martial_art_with_docstring()
Docstring: This function returns the name of my favorite martial art
File:      ~/src/functional_intro_to_python/<ipython-input-1-bef983c31735>
Type:      function
```
"""

def favorite_martial_art_with_docstring():
    """This function returns the name of my favorite martial art
    This is more
    This is even more
    return "string"
    """
    return "bjj"

#Docstrings of functions can be printed out by referring to __doc__

#favorite_martial_art_with_docstring.__doc__
# favorite_martial_art_with_docstring?

#Function arguments: positional, keyword

def practice(times):
    print(f"I like to practice {times} times a day")

practice(2)

# Positional Arguments are processed in order

def practice(times, technique, duration):
    print(f"I like to practice {technique}, {times} times a day, for {duration} minutes")

practice(3, "piano", 45)

#Keyword Arguments are processed by key, value and can have default values

def practice(times=2, technique="python", duration=60):
    print(f"I like to practice {technique}, {times} times a day, for {duration} minutes")

practice()
practice(duration=90, times=4)

# *****args and ****kwargs

# allow dynamic argument passing to functions
# Should be used with discretion because it can make code hard to understand

def attack_techniques(**kwargs):
    """This accepts any number of keyword arguments"""

    for name, attack in kwargs.items():
        print(f"This is an attack I would like to practice: {attack}")


attack_techniques(arm_attack="kimura",
                  leg_attack="straight_ankle_lock",
                  neck_attack="arm_triangle",
                 body_attack="charge")

# passing dictionary of keywords to function

attacks = {"arm_attack":"kimura",
           "leg_attack":"straight_ankle_lock",
           "neck_attach":"arm_triangle"}

attack_techniques(**attacks)

# Passing Around Functions

# Object-Oriented programming is a very popular way to program, but it isn't the only style available in Python. For concurrency and for Data Science, functional programming fits as a complementary style.

# In the example, below a function can be used inside of another function by being passed into the function itself as an argument.

def attack_location(technique):
    """Return the location of an attack"""

    attacks = {"kimura": "arm_attack",
           "straight_ankle_lock":"leg_attack",
           "arm_triangle":"neck_attach"}
    if technique in attacks:
        return attacks[technique]
    return "Unknown"

attack_location("kimura")


def multiple_attacks(attack_location_function):
    """Takes a function that categorizes attacks and returns location"""

    new_attacks_list = ["rear_naked_choke", "americana", "kimura"]
    for attack in new_attacks_list:
        attack_location = attack_location_function(attack)
        print(f"The location of attack {attack} is {attack_location}")

multiple_attacks(attack_location)

# Closures and Functional Currying

# Closures are functions that contain other nested functions with state from outer function.
# In Python, a common way to use them is to keep track of the state. In the example below, the outer function, attack_counter keeps track of counts of attacks. The inner fuction attack_filter uses the "nonlocal" keyword in Python3, to modify the variable in the outer function.
# This approach is called "functional currying". It allows for a specialized function to be created from general functions. As shown below, this style of function could be the basis of a simple video game or maybe for the statistics crew of a mma match.

#nonlocal cannot modify this variable
#lower_body_counter=5
def attack_counter():
    """Counts number of attacks on part of body"""
    lower_body_counter = 0
    upper_body_counter = 0
    #print(lower_body_counter)
    def attack_filter(attack):
        nonlocal lower_body_counter
        nonlocal upper_body_counter
        attacks = {"kimura": "upper_body",
           "straight_ankle_lock":"lower_body",
           "arm_triangle":"upper_body",
            "keylock": "upper_body",
            "knee_bar": "lower_body"}
        if attack in attacks:
            if attacks[attack] == "upper_body":
                upper_body_counter +=1
            if attacks[attack] == "lower_body":
                lower_body_counter +=1
        print(f"Upper Body Attacks {upper_body_counter}, Lower Body Attacks {lower_body_counter}")
    return attack_filter

fight = attack_counter()

fight("kimura")
fight("knee_bar")
fight("keylock")

#### Partial Functions

# Useful to partial assign default values to functions

from functools import partial

def multiple_attacks(attack_one, attack_two):
  """Performs two attacks"""

  print(f"First Attack {attack_one}")
  print(f"Second Attack {attack_two}")

attack_this = partial(multiple_attacks, "kimura")
type(attack_this)
attack_this("knee-bar")

# Alternately, the original function can also be called with a different two attacks

multiple_attacks("Darce Choke", "Bicep Slicer")

#### Lazy Evaluated Functions (Generators)

# A very useful style of programming is "lazy evaluation". A generator is an example of that. Generators yield an items at a time.

# The example below return an "infinite" random sequence of attacks. The lazy portion comes into play in that while there is an infinite amount of values, they are only returned when the function is called.

def lazy_return_random_attacks():
    """Yield attacks each time"""
    import random
    attacks = {"kimura": "upper_body",
           "straight_ankle_lock":"lower_body",
           "arm_triangle":"upper_body",
            "keylock": "upper_body",
            "knee_bar": "lower_body"}
    while True:
        random_attack = random.choices(list(attacks.keys()))
        yield random_attack

attack = lazy_return_random_attacks()
type(attack)

for _ in range(6):
    print(next(attack))

#### Decorators:   Functions that wrap other functions

#### Randomized Sleep Decorator

# Another useful technique in Python is to use the decorator syntax to wrap one function with another function. In the example below, a decorator is written that adds random sleep to each function call. When combined with the previous "infinite" attack generator, it generates random sleeps between each function call.

def randomized_speed_attack_decorator(function):
    """Randomizes the speed of attacks"""

    import time
    import random

    def wrapper_func(*args, **kwargs):
        sleep_time = random.randint(0,3)
        print(f"Attacking after {sleep_time} seconds")
        time.sleep(sleep_time)
        return function(*args, **kwargs)
    return wrapper_func

@randomized_speed_attack_decorator
def lazy_return_random_attacks():
    """Yield attacks each time"""
    import random
    attacks = {"kimura": "upper_body",
           "straight_ankle_lock":"lower_body",
           "arm_triangle":"upper_body",
            "keylock": "upper_body",
            "knee_bar": "lower_body"}
    while True:
        random_attack = random.choices(list(attacks.keys()))
        yield random_attack

for _ in range(5):
    print(next(lazy_return_random_attacks()))


##### Timing Decorator

# Using a decorator to time code is very common

from functools import wraps
from time import time

def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print(f"fun: {f.__name__}, args: [{args}, {kw}] took: {te-ts} sec")
        return result
    return wrap

@timing
def some_attacks():
  attack = lazy_return_random_attacks()
  for _ in range(5):
    print(next(attack))

some_attacks()

##### Making Classes Behave Like Functions

class AttackFinder:
  """Finds the attack location"""


  def __init__(self, attack):
    self.attack = attack

  def __call__(self):
    attacks = {"kimura": "upper_body",
           "straight_ankle_lock":"lower_body",
           "arm_triangle":"upper_body",
            "keylock": "upper_body",
            "knee_bar": "lower_body"}
    if not self.attack in attacks:
      return "unknown location"
    return attacks[self.attack]