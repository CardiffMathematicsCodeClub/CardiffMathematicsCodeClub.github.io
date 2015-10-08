---
layout     : post
title      : "Adding Python to the PATH on windows"
categories : blog 
tags       : blog python windows path
author     : Timothy
comments   : true
---

There have been a few of you trying to run a [Python]({{site.baseurl}}/languages/Python.html) script within [Atom]({{site.baseurl}}/editors/Atom.html) on windows and are getting the following error message.

`'Python' is not recognized as an internal or external command, operable program or batch file.`

If you have installed Python, the reason for this message is as Python isn't part of the PATH means that Atom can't find Python to run the script.

To add Python to the PATH, the following is one option.
Other methods can be found online. 

Locate the installation file used to install Python which is called `Python-2.7.*.msi` an run it.

When it loads you will get the screen show below and select `Change Python 2.7.*` and click Finish.
Note: The finish button doesn't mean you finished as you will be taken to the next screen. 

![Select Change Installation]({{site.baseurl}}/res/blog_pics/pythonpath1.png)

Then on the customize Python screen click on the red cross next to `Add Python.exe to PATH` and select `Will be installed on local hard drive`.
Then click next.

![Select Path to be installed]({{site.baseurl}}/res/blog_pics/pythonpath2.png)

This will also take into account if you have changed the default installation folder. 

Once you have done this **RESTART WINDOWS** then Python should be working within Atom. 
