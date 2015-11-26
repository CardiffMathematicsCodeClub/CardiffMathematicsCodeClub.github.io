---
layout     : post
title      : "The first editor off"
categories : website
tags       : blog vim atom emacs
author     : Vince, Alex, Sam, Adam
comments   : true
---

During the second week of code club we held an editor off. Like a dance off or
lip sync battle but cooler:


<div class="video">
    <figure>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/HvRypx1lbR4" frameborder="0" allowfullscreen></iframe>
    </figure>
</div>

For this first battle we had 4 participants with 3 weapons of choice:

- Vince: Vim
- Sam: Vim
- Alex: Emacs
- Adam: Atom (nothing worked for him)

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

The second thing was `<leader> + K` which takes you directly to the source code
for any given function. So Vince did this on the `random.choice` function to
directly access the python source code. He then quickly modified the way that
function worked so that he would always win at the simple game he programmed.

Note that the `<leader>` key is just any key that you can set up in Vim, Vince
has this set up as the default which is `\`.


## Sam

### Writing output of shell commands to current buffer

First, Sam showed how it is possible to run shell commands from within VIM using `:! <commands>`.
Additionally, he showed how you can write the output from these commands into the current buffer using `:.! <commands>`.

Vince added that a good use of this feature could be creating or adding to a .gitignore file by writing the output of an `git status` command (the output being all the files that are not being tracked by git).

### Use of macros

Secondly, Sam showed how you can record macros in VIM to speed up repetitive tasks.

* To start recording a macro press <kbd>q</kbd><kbd>a</kbd>, <kbd>a</kbd> can be replaced by any other key you want to bind the macro to.
* Carry out the commands you wish to record; aim to navigate using keys such as <kbd>w</kbd>, <kbd>e</kbd>, and <kbd>b</kbd> (navigating by words) rather that <kbd>h</kbd>, <kbd>j</kbd>, <kbd>k</kbd>, and <kbd>;</kbd> (navigating by letters) so the macro is more general and will be robust when applied to different lines.
* To finish recording your macro press <kbd>q</kbd>.

* To run your macro press <kbd>@</kbd><kbd>a</kbd> (or whatever key binding you used).

* To run your macro on multiple lines either:
  * End your macro by moving down a line (<kbd>j</kbd>) and then run the macro the for the desired number of times (e.g. <kbd>5</kbd><kbd>@</kbd><kbd>a</kbd>).
  * Select the lines in visual mode (<kbd>V</kbd>), and then run `:norm @a` (replacing 'a' for your key binding).

Sam demonstrated this by formatting a few lines of csv format data into Python dictionary format.

## Alex

### Butterfly Mode

This was more of a joke than anything useful by claiming that emacs is the ultimate editor and emac's
butterfly mode is a reference to the following [xkcd][xkcd] comic.

![Butterfly-Power](http://imgs.xkcd.com/comics/real_programmers.png)

Launching butterfly mode by typing ```M-x butterfly RET``` (M-x = Alt + x, RET = Enter) will see characters
fly on from the edges of the screen and print the sentence ```Amazing physics going on``` in the centre of the
screen.

### Org-Babel, Tangling and Weaving

On a more serious note Alex showed us Org-Babel, a facet or emac's Org-Mode which allows you to embed source code
in your documents. How is this different from other formats such as Markdown? Well this source code can be
"tangled" into other files.

This allows us to follow a paradaigm called
[Literate Programming][Literate]
where instead of writing the source code to a program in a format specified by the computer, you can write the
source code in a way that makes sense to humans and then use Org-Babel to compile all the files from code
snippets embedded in your document.

I don't feel like I'm explaining this very well so let me point you in the direction of a few such programs.
Alex's [Emacs Configuration][Emacs]
is in fact a literate program using Org-Babel. While it isn't written using Org-Babel Donald Knuth's
[TeX][Tex] is probably _the_ example of a literate program.


[xkcd]: https://xkcd.com/378/
[literate]: https://en.wikipedia.org/wiki/Literate_programming
[Emacs]: https://raw.githubusercontent.com/alcarney/emacs.d/master/README.org
[Tex]: http://mirrors.ctan.org/systems/knuth/dist/tex/texbook.tex
