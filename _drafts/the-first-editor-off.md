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
