# the next() method in python generators!!

_This method is used **parse** the values yielded by a generator._

**This method tells the generator only to return the next value of the iterable.**

When we do this:

```pytohon3
g=numberGenerator(10); # for some generator function numberGenerator()!!
```

we are basically instantiating a generator g. This g is like a variable that holds the generator state.

_When the function `next()` is called with the generator as its argument, the Python generator function is executed until it finds a `yield`_
_statement. Then, the yielded value is returned to the called and the state of the generator is saved for later use._
