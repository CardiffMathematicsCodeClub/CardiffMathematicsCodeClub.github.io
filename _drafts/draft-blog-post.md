---
layout     : post  #NEVER CHANGE THIS
title      : "Draft Blog Post"  #WHat do you want your blog post to be called
categories : website How To
tags       : blog
author     : Adam  #Write your name here
comments   : true  #This allows people to comment on your post
---

**!!!DO NOT DELETE THIS THIS IS FOR REFERENCE ONLY!!!!**

We write blog posts for the website in markdown, this means that we can also use HTML tags such as <kbd></kbd>
when needed.

**Name of blog post**  
This should be in the form: ```year-month-day-title-of-blog-post.md```.  
So for this blog post it would be: ```2015-11-10-draft-blog-post.md```

**How to insert a picture**
First save the picture that you want to insert into the res/blog_pics folder.
Then go to the point in your poat that you want the picture to be and use the following code:  
![Add Alt-text here](/res/blog_pics/name-of-your-pic.jpg)  
So for example if I wanted to put in my picture called WHERE-IS-EVERYONE-pic4 with the Alt-text being
`Maybe they are behind the screen?` then all I do is type:  
![Maybe they are behind the screen?](/res/blog_pics/WHERE-IS-EVERYONE-pic4.jpg)

**How to insert a video from youtube**

Go to the video you want to insert on youtube and click on the share button.
Click on the embed button and copy the link.
then using the code below:

<div class="video">
    <figure>
        paste the link here
    </figure>
</div>

You can embed the video into your post. For example, if I wanted to embed the video of Vince's talk
on Axledrod below then I would type:

<div class="video">
    <figure>
        <iframe width="560" height="315" src="https://www.youtube.com/embed/gbxv3pn9YB4" frameborder="0" allowfullscreen></iframe>
    </figure>
</div>


**Highlighting code in a post**
If you want to highlight just one line of code then you can use either the HTML tag <kbd>type code here</kbd>
or using back-ticks `type code here`.

If you wanted to highlight several lines of code and also have syntax highlighting then
you need to use the following code:

{% highlight NAME OF LANGUAGE %}

	put the code here.

{% endhighlight NAME OF LANGUAGE %}

For example, if I wanted to input the code from Q1 of the 2015/16 Computing for Mathematics class test,
I would type:

{% highlight python %}  

	def mysqrt(K, epsilon=.001):
	    X = K / 4.0
	    while abs(X ** 2 - K) > epsilon:
	        X = (X + K / X) / 2
	    return X

	for n in range(1, 10001):  # A loop to test a bunch of values
	    approx = mysqrt(n)
	    true = n ** .5
	    print approx, true, approx - true  # Printing the 3 results

{% endhighlight python %}

**How to add a hyper link to your blog**
If I wanted to put a hyper link into my blog at a certain point and link it to the phrase <kbd>yes we code</kbd>,
then I would simply write:  

[yes we code][example]  

instead of just 'yes we code'.

And at the bottom of the page you would write:  
[example]: link to website/article you want to look at

So for example if I wanted to attach a link to an article about notoruious DDOS attacks [here][first] then I would do this.


[first]: http://siliconangle.com/blog/2013/08/26/5-notorious-ddos-attacks-in-2013-big-problem-for-the-internet-of-things/
