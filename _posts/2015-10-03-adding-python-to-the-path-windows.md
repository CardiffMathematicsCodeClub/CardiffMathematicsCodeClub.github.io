---
layout     : post
title      : "Adding Python to the PATH on windows"
categories : blog 
tags       : blog python windows path
author     : Timothy
comments   : true
---

There have been a few of you trying to run a python script within atom on windows and are getting the following error message.

`'python' is not recognized as an internal or external command, operable program or batch file.`

The reason for this meassage is as Python isn't part of the PATH means that Atom can't find python to run the script.

To add Python to the script, the following is one option.

Locate the installation file used to install python which is called python-2.7.*.msi an run it.

When it loads you will get the screen show below and select Change Python 2.7.*

![Select Change Installation]({{site.baseurl}}/res/blog_pics/pythonpath1.png)

On the customize Python screen click on the red cross next to `Add python.exe to PATH` and select `Will be installed on local hard drive`.
Then click next.

![Select Path to be installed]({{site.baseurl}}/res/blog_pics/pythonpath2.png)

This will also take into account if you have changed the default installation folder. 

Once you have done this **RESTART WINDOWS** then python should be working within Atom. 
