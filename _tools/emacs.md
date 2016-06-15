---
layout: reference
title: Emacs
---

### Overview

{% include image_caption.html 
           url="/res/reference_pics/emacs-no-conf.png" 
           caption="Emacs without any configuration" %}

To call [Emacs][emacs] a text editor would be like calling a smartphone a pocket
calculator. While Emacs can edit text but it can also do so much more, from
browsing the web to answering emails, from [playing tetris][Mxtetris] to
[offering counseling][Mxdoctor].

Emacs is often affectionately referred to as "an Operating System lacking a
decent text editor" due to all the different programs that have been written for
it. At its core Emacs is essentially an interpreter for a [Lisp][lisp] dialect
called [ELisp][elisp] and people over the years have written programs that just
happen to be good at manipulating text making Emacs suitable for text editing.

It has its drawbacks though Emacs users are often struck down with a case of
"[Emacs Pinky][emacs-pinky]" which is essentially RSI from having to use the
Control key so often to issue commands. Thankfully there are ways to remedy
this, if you are familiar with the [Vim][vim] editing style there is a fantastic
vim emulation package called [evil-mode][evil] which when combined with
[evil-leader][evil-leader] brings a workflow to Emacs where you can quite easily
forget about the Control key entirely.

### Starter Kits

{% include image_caption.html 
    url="/res/reference_pics/emacs-spacemacs.png"
    caption="Emacs with a custom configuration, using the Spacemacs starter kit"%}

With great power comes great responsibility and configuring Emacs to your liking
can be an entire project in itself. For example [here][init-el] is my old
settings file which weighs in at over 400 lines of code and even then many
features that I wanted weren't working properly or missing entirely. Thankfully
the community has created many starter kits or configuration frameworks which
allows you to crowd source your configuration leaving you to concentrate on
other things.

Some popular starter kits include:

- [Prelude][prelude]: A starter kit focused on bringing saner defaults and a
  large suite of popular Emacs packages to kickstart your editing experience.
  Focuses on the default editing style of Emacs
  
- [Spacemacs][spacemacs]: Mainly focused on the Vim editing style, Spacemacs
  brings you many of the popular Emacs packages packages wrapped with mnemonic,
  discoverable keybindings.
  
- [emacs24-starter-kit][starter-kit]: This starter kit is written in a literate
  style where all code is surrounded by the documentation explaining it. 
  

[elisp]: https://en.wikipedia.org/wiki/Emacs_Lisp
[emacs]: https://www.gnu.org/s/emacs/
[emacs-pinky]: http://ergoemacs.org/emacs/emacs_pinky.html
[evil]: http://www.emacswiki.org/emacs/Evil
[evil-leader]: https://github.com/cofi/evil-leader
[init-el]: https://github.com/alcarney/emacs.d/blob/master/init.el
[lisp]: https://en.wikipedia.org/wiki/Lisp_(programming_language)
[Mxdoctor]: https://vimeo.com/90228904
[Mxtetris]: https://www.youtube.com/watch?v=5A8knEALaIY
[prelude]: https://github.com/bbatsov/prelude
[spacemacs]: https://github.com/syl20bnr/spacemacs

[starter-kit]: http://eschulte.github.com/emacs24-starter-kit/

