# Cardiff School of Mathematics Code Club  
[![Build Status](https://travis-ci.org/CardiffMathematicsCodeClub/CardiffMathematicsCodeClub.github.io.svg?branch=master)](https://travis-ci.org/CardiffMathematicsCodeClub/CardiffMathematicsCodeClub.github.io)

A repository for the Cardiff School of Mathematics Code Club: an extra curricular club open to all.

The website for code club is located here - http://cardiffmathematicscodeclub.github.io/

Meeting time: Thursday's 16:00-18:00 in room M/0.33.

## Runing the website locally
In order to run the website locally you need to have jeykll installed.

Once you have jekyll installed, then ```cd``` into the directory where the website is located and from the terminal run the following.

```
$ jekyll serve --watch
```

Then open the url given in a web browser to view the site.

Any changes you make to a page should automatically updated when viewing locally. If nothing changes, check the terminal from where jekyll has been run to see if there are any errors.

If you are making a draft post and want to preview it locally you can run the following.

```
$ jekyll serve --w --drafts
```

The draft blog post will appear as the latest post.


## Contributing

You are welcome to contribute to the code club website, we need as much
help as possible in making this the best site on the internet! Below is
a short list of tasks that need completing:

- Pages that give a short introduction to most of the popular programming languages
  would be good. These pages should give a should give a short piece on the history
  of the language, what it is used for giving well known programs as examples where possible.
  Also include a "Hello world!" snippet (see below) and some links to further resources, tutorials etc.

- We should think about maintaining a list of past and current projects that have been worked
  on at code club. Linking to source code and/or demos when possible

- We will always need help making the site looking as good as possible

- Maybe we could go for a terminal theme? Making the text boxes look like output from
  terminal commands, e.g. the menu could be the output from a "$ ls" command. We could
  also look at experimenting with CSS animations to add blinking cursors, typing commands etc.
  Or of anyone has other ideas then I'm open to discussion :)

### Code snippets

To embed code snippets into a page it's best to create a [Gist](https://gist.github.com) containing
the code, and since we are using Jekyll you can simply add the following to the markdown for that particular
page

```
{% gist <username>/<gist-id> %}
```
so for example if the URL for a particular gist was ```https://gist.github.com/johnsmith/57fd5d7s8fd6``` then
in your webpage you would put ```{% gist johnsmith/57fd5d7s8fd6 %} ```


### Testing Framework

#### Running tests:

Functional tests have been written using [selenium](http://www.seleniumhq.org/).
To run these you will need the selenium python package:

    $ pip install selenium

To run the tests set the dev server running:

    $ jekyll serve

then run the `functional_tests.py` file:

    $ python functional_tests.py

The output should look something like this:

```
.....
----------------------------------------------------------------------
Ran 5 tests in 13.083s

OK
```

Note that the testing framework requires [Firefox](https://www.mozilla.org/en-GB/firefox/new/) (it is possible to run other browsers but Firefox works out of the box).
When running these functional tests the browser will open up and navigate as dictated by the tests.

**Tests should be run after every pull and before every push (as well as throughout any other development).**

#### Writing tests

The functional tests are class based and all classes include a 'User Story'.
Whenever a new feature/page is added to the site a corresponding test should be written (note that at present not all tests that are needed are written).
In fact 'Test Driven Development' is the correct way to write any code:

1. Write a test
2. Check that tests fails
3. Write feature that stops test from failing

> Obey the Testing Goat! Do Nothing Until You Have a Test

![](http://orm-chimera-prod.s3.amazonaws.com/1234000000754/images/twdp_0101.png)

A great explanation of this process is given in [this book](http://chimera.labs.oreilly.com/books/1234000000754/ch01.html) (free to read online and where the goat image is taken from).
