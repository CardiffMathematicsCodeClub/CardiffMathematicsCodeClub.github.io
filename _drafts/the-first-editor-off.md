---
layout     : post
title      : "The first editor off"
categories : website vim atom emacs
tags       : blog
author     : Vince, Alex, Sam, Adam
comments   : false
---

During the second week of code club we held an editor off. Like a dance off or
lip syn battle but cooler:


<div class="video">
    <figure>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/HvRypx1lbR4" frameborder="0" allowfullscreen></iframe>
    </figure>
</div>

For this first battle we had 4 participants with 3 weapons of choice:

- Vince: Vim
- Adam: Atom
- Alex: Emacs
- Sam: Vim

This post will briefly show/discuss what they showed:

## Vince

### Visual mode and using `.`

The first 'trick' Vince showed was how to repeat actions using the `.`

Combining this with visual mode allows you to quickly and easily make modifications across a file.

### Using the jedi-vim package to change Python

The second 'trick' Vince showed was using the
[jedi-vim](https://github.com/davidhalter/jedi-vim) plugin to quickly get the
docstring for a function:

Simply hit `<leader> + d` and the docstring appears in a buffer.

The second thing was `<leader> + K` which take you directly to the source code
for any given function. So Vince did this on the `random.choice` function to
directly access the python source code. He then quickly modified the way that
function worked so that he would always win at the simple game he programmed.

Note that the `<leader>` key is just any key that you can set up in Vim, Vince
has this set up as the default which is `\`.


## Sam

### Writing output of shell commands to current buffer

First, Sam showed how it is possible to run shell commands from within VIM using `:! <commands>`.
Additionally, he showed how you can write the output from these commands into the current buffer using `:.! <commands>`.

### Use of macros

Secondly, Sam showed how you can record macros in VIM to speed up repetitive tasks.

* To start recording a macro press <kbd>q</kbd><kbd>a</kbd>, <kbd>a</kbd> can be replaced by any other key you want to bind the macro to.
* Carry out the commands you wish to record; aim to navigate using keys such as <kbd>w</kbd>, <kbd>e</kbd>, and <kbd>b</kbd> (navigating by words) rather that <kbd>h</kbd>, <kbd>j</kbd>, <kbd>k</kbd>, and <kbd>;</kbd> (navigating by letters) so the macro is more general and will be robust when applied to different lines.
* To finish recording your macro press <kbd>q</kbd>.

* To run your macro press <kbd>@</kbd><kbd>a</kbd> (or whatever key binding you used).

* To run your macro on multiple lines either:
  * End your macro by moving down a line (<kbd>j</kbd>) and then run the macro the for the desired number of times (e.g. <kbd>5</kbd><kbd>@</kbd><kbd>a</kbd>).
  * Select the lines in visual mode (<kbd>V</kbd>), and then run `:norm @a` (replacing 'a' for your key binding).
