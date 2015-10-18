---
layout : post
title: "An Introduction to Functional Programming with Python - Part 1"
categories : functional python tutorial
tags: blog
author: Alex
comments: true
---

This is the first part of a tutorial series meant to introduce the functional programming paradigm
using features built into Python. Most of what I will talk about will be available in both
Python 2.7.x and Python 3.x however in this series I will be using Python 3.x and will point out any
differences when needed.

I suppose I had better start by answering...

## What is a Paradigm?

It's a way of doing things and as you can see [here][paradigm-list] - there are a lot of them!

If you have completed Vince's [Computing for Maths][cfm] class then you will have been taught the Python
programming language but using the [imperative][imperative-wiki] and [object oriented][oop-wiki] paradaigms.

Ok that's the fancy stuff out of the way, in plain English this means that you tell the computer what
to do step-by-step for example consider the following bit of Python:

{% highlight py3 %}

def calc_average(nums):
    """
    This function calculates the average of a list of numbers, it assumes the
    list conatins only numbers and is non-empty

    Arguments:
                - nums: A list of numbers

    Outputs:
                - The average, a floating point number
    """

    sum = 0

    for n in nums:
        sum += n

    return sum/len(nums)
{% endhighlight %}

Here we have to tell Python exactly what it needs to do verbaitum

    1. Create a variable called sum, assign it the value zero.
    2. Go through each item in the list in turn and add it's value to the variable sum.
    3. Divide that by the number of items there were in the list.

Whereas the functional paradigm is part of a family of [declarative programming][declarative-wiki]
paradgims, where instead of detailing all the steps you simply 'declare' what something is or how to
transform it into another form. In the case of [functional programming][functional-wiki] this is done
(suprisingly) using functions, for example we can rewrite the above as the following.

{% highlight py3 %}

from functools import reduce

def f_average(nums):
    """
    The same as the calc_averaage function, just in a functional style
    """
    sum = reduce(lambda x, y: x + y, nums, 0)

    return list(sum/len(nums))
{% endhighlight %}

> Python 2.7.x Differences
>
> The ```reduce``` function was only moved into ```functools``` in Python > 3.0 so
> it doesn't need to be imported. Also the result doesn't require being cast to
> a list.

Don't worry too much if you don't understand the code above we will get around to how exactly
this works in later posts, the important point is to note that this style is slightly more
abstract and we let python handle some more of the details for us.

## Pure vs Impure Functions

There are two types of functions in the world _pure_ and _impure_. Below are two functions - can
you spot the pure function from the impure function?

{% highlight py3 %}

def f(x):
    return x + 1

def g(x):
    if isTuesday():
        return x + 1
    else:
        return x
{% endhighlight %}

The function ```g``` is the impure function since it depends on the state of the system it is run on.
Depending on if it is Tuesday or not this function may or may not do something, one of the main features
of the functional paradigm and the functional programming langauges (such as Haskell) is that
they deal in pure functions as far as possible.

The function ```f``` is pure, which means given the same arguments will return the same result come rain, come
shine, sleet or snow. If the world is on fire and the socks have declared war on the bananas this function
will behave exactly the same.

The more that you restrict the number of places where the current state of the system affects the behavoir of
your code the easier it will be to maintain and extend your program over time.

Well I think that's it for now, that's a brief overview of functional programming next time we will
take a look at _lambdas_ and _higher order functions_.


[cfm]: http://vknight.org/Computing_for_mathematics/
[declarative-wiki]: https://en.wikipedia.org/wiki/Declarative_programming
[functional-wiki]: https://en.wikipedia.org/wiki/Functional_programming
[imperative-wiki]: https://en.wikipedia.org/wiki/Imperative_programming
[oop-wiki]: https://en.wikipedia.org/wiki/Object-oriented_programming
[paradigm-list]: https://en.wikipedia.org/wiki/Programming_paradigm
