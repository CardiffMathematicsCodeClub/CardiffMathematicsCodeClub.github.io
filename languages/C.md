---
layout: language
title: C
categories: inspiration languages
---

### Overview

C is one the oldest languages still in active use today, first created 1972 by
Dennis Ritchie at [Bell Labs][bell-labs] and has gone through many revisions as the
years have progressed with the most recent edition [C11][c11] released early in 2011.

However due to the way C is developed, where a committee drafts a standard with C's rules
and features and it's up to the compiler developers to implement them. This mean that
many of the more recent features are still not available for certain compilers/platforms
so many people try to adhere to the [C99][c99]
or even [ANSI][ansi-c] (the original release) standards to increase portability.

C has been a hugely influential language and has inspired the design of many of newer languages
including C++, Java, Go, Python and many, many more. C has and still is so popular due
to the fact it is extremely portable, chances are a compiler exists for almost any processor
architecture out there and produces extremely fast executables.

But that speed comes at a cost, anything but the simplest of tasks are left to the programmer.
This means when programming in C you have to manage your own memory, perform bound checks on arrays
and more. If you forget to ensure you don't actually access memory you have to right to at best you
can introduce a bug that will crash your program, however a hacker can exploit this and inject malicious
code into your program and basically hi-jacking you or your clients' machine...

If you would like more information about the history or evolution of this language
then you can follow [this][cwiki] link

### Applications

C is heavily used for working with hardware, so many device drivers and operating systems such as
Linux are implemented in C. It's performance means it's a popular choice for real-time systems and
applications such as video games. Also languages such as Python, Perl and PHP all have their interpreters
written in C.

Below is a list of applications that use C:

- [Blender][blender]
- [GameBoy Games][gba]
- [The Linux Kernel][kernel]
- [Vim][vim]
- Pretty much any linux command line tool (ls, cd, wget, curl, grep, sed, etc.)
- And many more!

### Some Code

Hello World:
{% gist alcarney/249466469521937d78c8 %}

A little program that will count the number of lines in a file
{% gist alcarney/aae3b583a956d92861b1 %}

### Some Useful Libraries/Tools

Many tools and libraries have sprung up over the years to make working with C easier, so below we've compiled a
list that gives you an idea of what is available.

_Disclaimer:_ Since I have only ever developed on Linux for Linux, this list will have a heavy bias towards Linux,
not everything below will be available for Windows and/or Mac.

__Compilers__

C is what is known as a compiled language, where the code you write is translated into machine code and then stored
in a binary file ready to be run. So to be able to develop in C it is absolutely essential that you use a compiler.

- [GCC Compiler][gcc]
- [CLang Compiler][clang] also provides static analysis tools

__Debuggers and Profiliers__

Because C is so low level (by today's standards) there are many places where bugs can appear in your program, so tools
have been developed to help you find and fix many of the most common bugs and help you hunt down a few of the more obscure ones.
Profilers help you find out which parts of your code are slowing your program down and help you find ways to speed it up.

- [GDB Debugger][gdb]
- [Perf][perf] a Linux tool that profiles your code's performance with stats like cache usage and instruction throughput on the CPU
- [Valgrind][valgrind] a tool to help debug/optimise C code helps spot memory leaks, race conditions also includes heap, cache and branch prediction profilers

__Libraries__

A library is a collection of code written by a third party designed to make your life easier by performing certain tasks for you.
This could be anything from drawing graphics on screen to reading a certain type of file for you.

- [Check][check] a unit testing library for C

__Build Tools__

Compiling large C programs can be a pain, it often requires performing multiple commands over 10s to 1000s of source files,
not to mention including all the correct references to libraries etc. Fortanately there are tools out there that help to
automate this process for you:

- [CMake][cmake] a cross platform build system that writes build scripts for whichever platform it's currently being used on.

[ansi-c]: http://www.flash-gordon.me.uk/ansi.c.txt
[bell-labs]: http://en.wikipedia.org/wiki/Bell_Labs
[blender]: https://www.blender.org
[c99]: http://www.open-std.org/jtc1/sc22/WG14/www/docs/n1256.pdf
[c11]: http://www.open-std.org/JTC1/SC22/WG14/www/docs/n1570.pdf
[check]: http://check.sourceforge.net
[clang]: http://clang.llvm.org
[cmake]: http://cmake.org
[cwiki]: http://en.wikipedia.org/wiki/C_(programming_language)
[gba]: http://www.coranac.com/tonc/text/toc.htm
[gcc]: https://gcc.gnu.org
[gdb]: http://www.gnu.org/software/gdb
[kernel]: https://kernel.org
[perf]: http://www.brendangregg.com/perf.html
[valgrind]: http://valgrind.org
[vim]: http://www.vim.org
