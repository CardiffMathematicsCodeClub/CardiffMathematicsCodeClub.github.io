---
layout     : post
title      : "How I made a DNS Attack at school"
categories : website
tags       : blog
author     : Ambrose
comments   : true
---

So, today I was feeling particularly mischievous. I enjoy making fun codes which usually serve no purpose,
and only are for show or with a funny outcome. Today was the day accidentally decided to make a DNS Attack.
"A DNS attack is an exploit in which an attacker takes advantage of vulnerabilities in the domain name
system (DNS)", for more info [click here.][first]

At the end of my last lecture of the day, I had been playing ticks on friends by putting slips of paper
with my name on in people's bags. So the obvious thought came to mind: "What about doing this in code?".
I moved swiftly to the computer labs to set to work on my most evil idea yet. I started by looking at
Vince's tutorials to find out how to write a file from python (Something I think is pretty awesome thing to
be able to do!) and set up it to make it for one file. Clearly one wasn't enough if I wasn't to "troll" 
my friends so I put it in to a 'for' statement in range 1 to 50. 50 files sounds awesome to me! But what
if I want more? So, next I decided to make a function to run this code with an argument 'n', which was
the upper bound of my range. But the thought came that my friends might try to outsmart me and put n to
be 1?!?!?! We can't have this, so I changed the 'for e in range(1, n)' to 'for e in range(1, 50 * n)'.
Now minimally there is 50 docs! Thats more like it!

I then thought that to be annoying, I made the file say "You are not the best. Ambrose is." which made me
chuckle, but what seemed funnier is if the code talked about them. So I set up a raw input to ask them
their name, and sub it in to the file instad of 'you'. From this



{% highlight python %}

import os

def whosthebest(n):
    name = raw_input("What's your name? ")
    for e in range(1, 50 * n):
        for t in range(1, 50 * n):
            filename = 'whosthebest%s.txt' % (t)
            textfile = open(filename, 'w')
            for i in range(50 * n):
                textfile.write("%s is not the best. Ambrose is. \n" % (name))
            textfile.close()
            os.system("start " + filename)

{% endhighlight python %}




[first]: http://siliconangle.com/blog/2013/08/26/5-notorious-ddos-attacks-in-2013-big-problem-for-the-internet-of-things/
