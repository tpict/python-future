"""
Backport of Python 3's int, based on Py2's long.

They are very similar. The most notable difference is:

- representation: trailing L in Python 2 removed in Python 3

"""

from future.utils import PY3, is_int


class newint(long):
    """
    A backport of the Python 3 int object to Py2
    """
    def __new__(cls, *args, **kwargs):
        """
        From the Py3 int docstring:

        |  int(x=0) -> integer
        |  int(x, base=10) -> integer
        |  
        |  Convert a number or string to an integer, or return 0 if no arguments
        |  are given.  If x is a number, return x.__int__().  For floating point
        |  numbers, this truncates towards zero.
        |  
        |  If x is not a number or if base is given, then x must be a string,
        |  bytes, or bytearray instance representing an integer literal in the
        |  given base.  The literal can be preceded by '+' or '-' and be surrounded
        |  by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
        |  Base 0 means to interpret the base from the string as an integer literal.
        |  >>> int('0b100', base=0)
        |  4

        """
        if len(args) == 0:
            return super(newint, cls).__new__(cls, **kwargs)
        elif is_int(args[0]):
            return args[0]
        return super(newint, cls).__new__(cls, *args, **kwargs)
        
    def __repr__(self):
        """
        Without the L suffix
        """
        value = super(newint, self).__repr__()
        assert value[-1] == 'L'
        return value[:-1]

    def __add__(self, other):
        return newint(super(newint, self).__add__(other))

    def __radd__(self, other):
        return newint(super(newint, self).__radd__(other))

    def __sub__(self, other):
        return newint(super(newint, self).__sub__(other))

    def __rsub__(self, other):
        return newint(super(newint, self).__rsub__(other))

    def __mul__(self, other):
        return newint(super(newint, self).__mul__(other))

    def __rmul__(self, other):
        return newint(super(newint, self).__rmul__(other))

    def __div__(self, other):
        return newint(super(newint, self).__div__(other))

    def __rdiv__(self, other):
        return newint(super(newint, self).__rdiv__(other))

    def __floordiv__(self, other):
        return newint(super(newint, self).__floordiv__(other))

    def __rfloordiv__(self, other):
        return newint(super(newint, self).__rfloordiv__(other))

    def __mod__(self, other):
        return newint(super(newint, self).__mod__(other))

    def __rmod__(self, other):
        return newint(super(newint, self).__rmod__(other))

    def __divmod__(self, other):
        result = super(newint, self).__divmod__(other)
        return (newsuper(result[0]), newsuper(result[1]))

    def __rdivmod__(self, other):
        result = super(newint, self).__rdivmod__(other)
        return (newsuper(result[0]), newsuper(result[1]))

    def __pow__(self, other):
        return newint(super(newint, self).__pow__(other))

    def __rpow__(self, other):
        return newint(super(newint, self).__rpow__(other))

    def __lshift__(self, other):
        return newint(super(newint, self).__lshift__(other))

    def __rlshift__(self, other):
        return newint(super(newint, self).__lshift__(other))

    def __rshift__(self, other):
        return newint(super(newint, self).__rshift__(other))

    def __rrshift__(self, other):
        return newint(super(newint, self).__rshift__(other))

    def __and__(self, other):
        return newint(super(newint, self).__and__(other))

    def __rand__(self, other):
        return newint(super(newint, self).__rand__(other))

    def __or__(self, other):
        return newint(super(newint, self).__or__(other))

    def __ror__(self, other):
        return newint(super(newint, self).__ror__(other))

    def __xor__(self, other):
        return newint(super(newint, self).__xor__(other))

    def __rxor__(self, other):
        return newint(super(newint, self).__rxor__(other))

    # __radd__(self, other) __rsub__(self, other) __rmul__(self, other) __rdiv__(self, other) __rtruediv__(self, other) __rfloordiv__(self, other) __rmod__(self, other) __rdivmod__(self, other) __rpow__(self, other) __rlshift__(self, other) __rrshift__(self, other) __rand__(self, other) __rxor__(self, other) __ror__(self, other) 

    # __iadd__(self, other) __isub__(self, other) __imul__(self, other) __idiv__(self, other) __itruediv__(self, other) __ifloordiv__(self, other) __imod__(self, other) __ipow__(self, other, [modulo]) __ilshift__(self, other) __irshift__(self, other) __iand__(self, other) __ixor__(self, other) __ior__(self, other)

    def __neg__(self):
        return newint(super(newint, self).__neg__())
        
    def __pos__(self):
        return newint(super(newint, self).__pos__())
    
    def __abs__(self):
        return newint(super(newint, self).__abs__())
    
    def __invert__(self):
        return newint(super(newint, self).__invert__())


__all__ = ['newint']