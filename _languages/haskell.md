---
layout: language
language: haskell
---

### Overview 

Haskell is a lazy, purely functional, statically typed programming language
named after the logician Haskell Curry. Despite the recent popularity surge of
functional languages Haskell is not a recent development having its first
release in 1990.

It was influenced by a language called [Miranda][miranda] which saw its first
release in 1985 and spawned a wide array of other lazy functional languages.
Haskell grew out of a desire to move away from the proprietary language Miranda
and consolidate the advances made in language design into a single language.

Following Haskell 1.0, there were number of additional specifications until the
Haskell98 specification was released and is considered the first "stable"
release. Published in 2010 Haskell2010, is the most recent Haskell
specification.

Being a language designed by specification there are many different
implementations of Haskell, however by far the most popular and feature complete
is [The Glasgow Haskell Compiler (GHC)][ghc] which is widely considered _the_
implementation of Haskell.

While Haskell has mostly been used as an academic language especially in the
early days it is used in industry by companies such as Facebook and there are
libraries for almost use case from web servers to games.

For more information you can go [here][haskell-wiki]


### Applications

Here is a short list of applications that have been written using Haskell:

- [Pandoc][pandoc]: A document conversion tool
- [Darcs][darcs]: A version control system, like Git but with a different
  approach to tracking changes
- [Xmonad][xmonad]: A tiling window manager for Linux

### Some Code

Hello World:

``` haskell
main :: IO ()
main = putStrLn "Hello World"
```

A program that will print the first 100 Fibonacci numbers:

``` haskell
fibs :: [Int]
fibs = 0 : 1 : zipWith (+) fibs (tail fibs)

main :: IO ()
main = print $ take 100 fibs
```

### Useful Libraries and Tools

__Compilers and Interpreters__

Haskell is a compiled language, it first gets compiled to an intermediate
language which is then used to generate code for whatever the target platform
is.

- [GHC][ghc]: As mentioned above considered _the_ implementation of Haskell also
  comes with an interpreter `ghci` which lets you try out various Haskell
  expressions in a REPL like environment.
- [GHCJS][ghcjs]: Built using GHC allows you to compile Haskell code to
  Javascript.
- [Frege][frege]: Compiles most Haskell code to the JVM (Java) and allows for
  easy use of native Java libraries and integration with Java code.
- [Hugs][hugs]: Used to be one of the main "competitors" to GHC, implementing
  the Haskell98 standard. However it is no longer under development.
  
__Build Tools__

Build tools are there to automate the process of compiling and managing your
programs letting you focus on more important things like writing code.

- [Cabal][cabal]: Is the build tool which ships with GHC and can also be used to
  install Haskell programs from source. However it can lead to trouble when used
  accross multiple projects with a problem commonly referred to as
  ["Cabal Hell"][cabal-hell]
- [Stack][stack]: This is a relatively recent development in the Haskell
   community and builds on top of Cabal in an attempt to solve "Cabal Hell" by
   working with [Stackage][stackage] which maintains lists of packages and their
   versions which "play nice" with each other.
   
__Libraries__

Libraries are collections of code which are designed to make a particular task
easier to perform, reducing the number of things you have to build and maintain
yourself.

- [Hakyll][hakyll]: A library which helps you create a static site generator
  (like Jekyll) in very few lines of code.
- [Yesod][yesod]: A web framework for Haskell - like Python's Django
- [Diagrams][diagrams]: Used to create vector graphics
- [LambdaHack][lambdahack]: A game engine focused on creating rouge-like dungeon
  crawlers like NetHack.

You can find a list of many, many more Haskell packages [here][hackage] on
Hackage

[cabal]:        https://www.haskell.org/cabal/
[cabal-hell]:   https://en.wikipedia.org/wiki/Cabal_(software)#Criticism
[darcs]:        http://darcs.net/
[diagrams]:     http://projects.haskell.org/diagrams/
[frege]:        https://github.com/Frege/frege
[ghc]:          https://www.haskell.org/ghc/
[ghcjs]:        https://github.com/ghcjs/ghcjs
[hackage]:      https://hackage.haskell.org/packages
[hakyll]:       https://jaspervdj.be/hakyll/
[haskell-wiki]: https://en.wikipedia.org/wiki/Haskell_(programming_language)
[hugs]:         https://www.haskell.org/hugs/
[lambdahack]:   https://hackage.haskell.org/package/LambdaHack
[miranda]:      https://en.wikipedia.org/wiki/Miranda_(programming_language)
[pandoc]:       http://pandoc.org/
[stack]:        http://www.haskellstack.org/
[stackage]:     https://www.stackage.org/
[xmonad]:       http://xmonad.org/
[yesod]:        http://www.yesodweb.com/











 
