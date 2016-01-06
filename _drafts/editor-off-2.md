---
layout     : post
title      : "The Editor Off Episode II: The Revenge of Atom"
categories : website vim atom emacs
tags       : blog
author     : Vince, Alex, Sam, Adam, Hannah, Geraint
comments   : true
---

After being decimated in the first week the Atom editor came out swinging with live code
publishing, real time markdown preview and modifying many lines of code simultaneously.
But could it hold off the newcomer Sublime?

For this battle we had 6 participants with 4 weapons of choice:

- Adam: Atom
- Vince: Atom
- Sam: Vim
- Alex: Emacs
- Geraint: Sublime
- Hannah: Sublime


This post will briefly show/discuss what they showed:

## Adam

### Making & publishing your own theme

After nothing worked and subsequently getting decimated by both Vim and Emacs in episode I,
Adam knew that he would have to come out fighting if he was to even stand a chance of
matching/beating Vince.

Adam therefore decided to showcase and perform a live publish of the [syntax theme][The Matrix]
he had been working on for the past year for his 1<sup>st</sup> 'trick'.
 
Despite a few teething problems, the pictures not loading correctly and not being able to find
it at first on the atom website, it went well.

### Using git-control

The 2<sup>nd</sup> trick Adam showed was a package called git-control which provides a GUI
interface to manage all commonly-used git commands.

Using the command `Ctrl`+`Alt`+`O` Adam opened up the GUI and having
connected it to the codeclub 'Project Folder', he committed and pushed up the quote of the
session live.

## Vince

Vince decided to throw a curve ball and chose a different weapon: he used atom.

### Using the built in markdown preview functionality

Markdown is an excellent language for quickly writing documents. Take a look at this video that
more or less shows the entirety of the markdown syntax in about 12 minutes:


<div class="video">
    <figure>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/6A5EpqqDOdk" frameborder="0" allowfullscreen></iframe>
    </figure>
</div>

In atom you can simply press `ctrl+shift+M` and it automatically opens a preview pane that
updates as you type. Here's a screenshot (showing me write the current blog post using Adam's
cool new theme):

![markdown-preview]({{site.baseurl}}/img/markdown-preview.png)

This is a nice example of some of the built in capabilities of atom.

### Movement and multiple cursors

Atom has some great built in functionality to help you type faster. **If your editor is not
helping you type less you are not using it right**. I've heard some people say that really with
you editor you should only ever type a given word once, I'm not quite there yet with my
favourite editor but am getting closer :)

For this trick Vince showed how you could select multiple lines and then have multiple cursors
which helped him fix some docstrings quickly. Here's a screenshot:

![multiple-cursors]({{site.baseurl}}/img/atom-multiple-cursors.png)

I also shared various other little tricks, such as typing `ctrl+F2` to set a bookmark and then
using `F2` to cycle between bookmarks to move back and forth between specific spots you're
working on.

To find out some of the cool things markdown can do out of the box, take a look at the
[documentation pages][documentation].

## Sam

### Use of panes in VIM.
Sam first demonstrated how it is possible in VIM to have the same file open twice, pointing to
different locations in the file. To do this type `:split` in normal mode. To change between the
two panes press `Ctrl`+`w` and then your desired directional key (hjkl).

Additionally, the panes can show different files. For example `:split hello.txt` would create a
new pane with `hello.txt` open inside it.

__Bonus Trick:__ VIM can open the code of websites directly, this is done by simply
substituting the URL in place of a file name when opening VIM (e.g.
`vim http://cardiffmathematicscodeclub.github.io/`).

### Automatic indentation
Any good editor has smart rules governing how text is indented on new lines.
In VIM, we can also apply this indentation after the text has already been written; Sam showed
an example of this for his second trick.

To apply the indentation, select the code the you wish to auto-indent, and then press
`=`.


## Alex

Continuing on from last week, Alex showed a few more tricks related to emacs' org-babel.

### Running embedded source code blocks

As seen in the first editor off org-mode provides a "supercharged" markdown like syntax and
allows you to embed source code blocks into your documents and then shuffle them around and
then write them out to separate files.

Well this week Alex showed us that org-babel also supports running these source code blocks and
then automatically pasting the results results into the current document, in a similar fashion
to tools like [IPython][ipython] but with a much larger number of
[supported languages][supported].

### Exporting org document to LaTeX

Org mode itself supports supporting its documents to a wide number of formats including HTML
and PDF (via LaTeX), this means using the features included by org-babel you could in theory
write up your entire project as an org file, source code, results and analysis in a single
place. Then quickly an (relatively) painlessly export it to LaTeX and compile to PDF ready for
sharing with others.

Alex quickly gave us small taste of this workflow by writing a small bit of python code
implementing pythagoras' theorem and the formula along with some filler text and exporting live
to PDF.

## Geraint

### Multi panes and multi cursors

Sublime come with many great features 'out-of-the-box'. The ability to split the screen and
work on up to four different files side by side was shown. This feature allows users to arrange
these files in rows, columns and grid format, great for working on large projects.

I then showed how to get as many cursors as you like simultaneously! In Sublime copies of the
same string can be highlighted at once (creating a new cursor for every instance) simply by
highlighting a string and repeatedly pressing `cmd+d`. Holding `cmd` and clicking a line number
highlights the whole line, but repeating this on other lines adds that line to what you have
highlighted, also creating many cursors!

### css Prediction

css is Sublime's specialty. Can't remember the exact name of a css property? No more worries,
in a .css file Sublime provides a drop-down menu of properties to choose from as you type,
makes creating beautiful HTML a breeze!


## Hannah



[The Matrix]: https://atom.io/themes/the-matrix-syntax
[documentation]: https://atom.io/docs/v1.0.19/using-atom-moving-in-atom
[ipython]: http://ipython.org
[supported]: http://orgmode.org/worg/org-contrib/babel/languages.html
