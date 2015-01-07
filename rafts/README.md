# Cardiff School of Mathematics Code Club

A repository for the Cardiff School of Mathematics Code Club: an extra curricular club open to all.

The website for code club is located here - http://cardiffmathematicscodeclub.github.io/

Meeting time: Thursdays at 16:00 in room M/0.33.

## Runing the website locally
In order to run the website locally you need to have jeykll installed.

Once you have jekyll installed, then ```cd``` into the directory where the website is located and from the terminal run the following.

```
$ jekyll serve --watch
```

Then open the url given in a web browser to view the site. 

Any changes you make to a page should automatically updated when viewing locally. If nothing changes, check the terminal from where jekyll has been run to see if there are any errors. 

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
the code, and sice we are using Jekyll you can simply add the following to the markdown for that particular
page

```
{% gist <username>/<gist-id> %}
```
so for example if the URL for a particular gist was ```https://gist.github.com/johnsmith/57fd5d7s8fd6``` then
in your webpage you would put ```{% gist johnsmith/57fd5d7s8fd6 %} ```
