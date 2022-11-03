# About [lambdaInPython.py](https://github.com/C0DER11101/PYTHONFOR5ThSem/blob/DaaPY/lambdaInPython.py)

Lambda keyword is used to make inline returning functions with no statements allowed internally.

Example:

```python
g=lambda x: x*x*x
```

Here `g` is actually a function, an inline function.

It takes an argument `x` for which it returns its cube!!

We would call `g` like this:

```python
g(6)
```

This is similar to this C++ snippet:

```c++
inline int g(int x)
{
	return x*x*x;
}
```

This is how an inline function looks like in C++, only a single statement(i.e. the return statement).

This is how we would call `g` in C++:

```c++
g(4);
```

So, in simple words, a lambda function in Python is just an inline function in C++!!!
