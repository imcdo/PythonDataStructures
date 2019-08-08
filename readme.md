## Misc python datastructures and random stuff

## Here are some helpful tutorials

### good python coding practices:
    Python, as you know, is a loosly typed language (you do not have to specify a type).  
    There are many benifits to this.  One of the most inportant is the ability to make 
    modular, reusuable code.  

    This means that we can take advantange of consistant interfaces (how we access an object with
    its methods and fields).  This means if we write similar objects (like a linked list and a normal list)
    with the same interface (same methods and properties) then we can use them interchangably
    whenever we want.

    How do we acheave this?  Well we can simply use the same methods.  For certain things however, python helps 
    us out by giving us a list of magic methods.  (i.e. the methods with __ around their names).  These 
    methods are used for built in functions like `hash()` and `len()` but also for operators like `+ - * /`.

    here is a short list of useful magic methods:

    **`def __str__(self):`**
        called when using the str() method, should return the string representation of your object

    **`def __len__(self)`: **
        this method is called when you use the function `len()` on your object.  this is recomended over using
        a size method 

    **`def __getitem__(self, key)` and `def __setitem__(self, key, value)`:**
        This magic method allows you to use brackets on your object.  When you use brackets to access
        an object it calls __getitem__ with the key as the value in the brackets.
        ex: `v = l[1]` is equivelent to 'v = l.__getitem__(1)`

        set item works the same whay except it is called when an = follows the brackets.  

    **`def __iter__(self):` **
        responds to the iter() function.  is used to get the iterable representation of your object.  Allows 
        for things like the unary * operator, comma seperation asignment, and for loops to act upon your object.


**I'll be sure to post more, especially on things like generators, lambdas, and the unary * operator as I use them in my code
quite a bit**

