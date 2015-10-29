---
layout     : post
title      : "How I made a DOS Attack at school"
categories : website
tags       : blog
author     : Ambrose
comments   : true
---

So, today I was feeling particularly mischievous. I enjoy making fun codes which usually serve no purpose,
and are only for show or have a funny outcome. Today was the day I accidentally decided to make a DOS Attack.
"A DOS attack is an exploit in which an attacker takes advantage of vulnerabilities in the domain name
system (DOS)", for more info [click here.][first]

At the end of my last lecture of the day, I had been playing tricks on friends by putting slips of paper
with my name on in people's bags. So the obvious thought came to mind: "What about doing this in code?".
I moved swiftly to the computer labs to set to work on my most evil idea yet. I started by looking at
Vince's tutorials to find out how to write a file from python (Something I think is pretty awesome thing to
be able to do!) and set up it to make it for one file. Clearly one wasn't enough if I was to "troll"
my friends so I put it in to a `for` loop ranging from 1 to 50. 50 files sounds awesome to me! But what
if I want more? So, next I decided to make a function to run this code with an argument `n`, which was
the upper bound of my range. But the thought came that my friends might try to outsmart me and put `n` to
be 1?!?!?! We can't have this, so I changed the `for e in range(1, n)` to `for e in range(1, 50 * n)`.
Now minimally there are 50 docs! Thats more like it!

I then thought that to be annoying, I would make the file say "You are not the best. Ambrose is." (which made me
chuckle), but what seemed more annoying is if the code talked about them. So I set up a raw input to ask them
their name, and sub it in to the file instead of 'you'.

This was nearly what I wanted. The last step in my master-plan was to make multiple copies of this. So I
put all the code I had written up to this point in yet another for statement, and let it rip! And it worked!!
Contempt with my creation I was about to let it rest, but an intrigued friend came up with the idea of "make
the code open all the files too". In my eyes, this was pure genius! So at code club, I asked Vince to
help me find hot to do such a thing. Considering how amazing and big python is, I was sure it would
be possible. And after a few google searches, my day long dream had become a reality. Vince input the code
on a seemingly appropriate line and I was happy. All that was left was to do was to run it... And that
was where the issue began...

I stress. DO NOT RUN THIS CODE. Turns out the code line to open the file was put within the for
statement within the for statement... And so, with n = 1, it opened up 2500 notepad files...


Here is a video of my computer visually combusting, enjoy!

<div class="video">
    <figure>
        <iframe width="560" height="315" src="https://www.youtube.com/embed/w3TW9G9Fark" frameborder="0" allowfullscreen></iframe>
    </figure>
</div>


Draining up to 97% of the Physical Memory, up to 8GB of Notepad and peaking the CPU at near 100%, this was the easily
the greatest code I have ever written.


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
