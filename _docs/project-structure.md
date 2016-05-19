---
layout: page
title: Project Structure 
---

This page simply outlines how this project is structured so you can use it as a
road map to help you find what you are looking for and where you can find out
more information.

## Jekyll Collections

The main bulk of the content of the website is made up of various
[Jekyll Collections][collections] they allow us to focusing on writing our
content in [Markdown][markdown] without having to worry about HTML, CSS or
anything else that usually goes with making a website.

### Folders

- `_docs` This contains all the documentation for the website (which you are
  currently reading).
  
- `_drafts` In this folder you can put draft blog posts that you are working on
  but don't want to have published yet, they will show up on your machine but not
  the live version of the site.

- `_languages` This contains all the reference pages for programming languages
  such as C, Python, Haskell etc. 
  
- `_posts` In this folder we put all of our blog posts which are published, on
  the live version of the site.
  
- `_projects` Here we specify all the projects that Code Club has worked on,
  both past and present. 
  
- `_tools` This is where we put the reference pages for tools, libraries and
  other utilies which makes working with languages easier. 
  
- `_workshops` Here is where we schedule any workshops that are upcoming.
  
## Other Content

The rest of the content for the website can be found in a few other locations.

### Folders

- `blog` This is a folder with a few HTML files, if you look at them there isn't
  much in there. They are there just to get Jekyll to generate a page for each
  of the categories in our blog.

- `res` This folder contains all the images that we have on the site, as well as
  the source files for the logo. (`.xcf` - Like `.psd` files for Photoshop but
  for the open source alternative [GIMP][gimp])

### Files
- `404.html` This is the page that gets displayed if users happen to try and
  load a page which doesn't exist.

- `archive.md` This is the Archive page, with links to past workshops, blog
  posts and session quotes.

- `coc.md` This is the code of conduct for while at code club

- `getinvolved.md` This is the Getting involved page, with links to ongoing
  projects, programming challenges and contributors to the site.

- `index.html` This is the home page of the website

- `projects.md` This is the list of all projects, including ones which are no
  longer active.

- `reference.md` This is the main reference page with links to all of the
  language and tool pages.

- `sessions.html` Here is the list of all the past session quotes.

- `workshops.md` This is the main workshops page, it lists all the workshops,
  both past and upcoming.
  
- `favicon.png` This is a small version of the code club logo, it is used for
  example by browsers when they display our logo on the current tab.
 
## Website Internals

This section contains all the folders and files which go into taking the content
above and turning it into a website with the help of [Jekyll][jekyll]

### Folders

- `_data` This folder contains a number of YAML (`.yml`) files which contains
  information that we use with Jekyll to build to website. We have the list of
  contributors, session quotes as well as the website's menu and themes defined
  here.
  
- `_includes` This folder contains various snippets of HTML which can be
  imported into templates and webpages. Here things like the twiiter feed and the
  website footer are defined here.
  
- `_layouts` Here we define the HTML templates that Jekyll uses to compile the
  website with. This is a good place to define things that are needed for large
  groups of pages on the website, e.g. we have a `blog` template which
  automatically adds the category menu to all pages on the blog to let users
  filter which sort of posts show up easily. 
  
- `_sass` This folder contains the bulk of the CSS for our site, written using a
  preprocessor SASS (`.scss` files), here we have all the themes and a default
  layout for the site that theme creators can use so they can concentrate on
  making the site look good. Think of this folder as the `_includes` folder we
  mentioned above, but for CSS.
  
- `_site` Jekyll takes our project and compiles it into a website, after
  finishing this process it stores the result here - can be useful when
  debugging issues to look at the generated HTML.
  
- `css` Here the main theme files are stored, they are also written in SASS like
  those in the `_sass` directory. The main files mostly contain variables and
  import statements while the bulk of the themes are defined in the `_sass`
  folder.
  
- `js` This folder contains all the Javascript that we have on the site it's
  here where we implement things like the theme changer and the showing and
  hiding of the twitter feed. Anything interactive on the site tends to be done
  using Javascript
  
### Files

- `_config.yml` Here we specify all of our options to Jekyll such as what
  collections we use, any extra gems we want Jekyll to use etc.

## Other 

This final section contains items which aren't directly used to make the site,
but often make life much easier for us by being there.

### Folders

- `script` This folder contains scripts which do things like calculating the new
  version number for the site, or defining particular tests to run.

### Files

- `.gitignore` To keep track of changes and help streamline the process of
  having multiple people work on the site at the same time we use a tool called
  [Git][git]. This file lists certain filetypes and folders which we don't want
  git to keep track of - like the `_site` folder created by Jekyll.
- `README.md` This is the project's README file. It is the first thing people
  see when they visit the project on [github][github] it contains instructions
  on how people can get started with contributing to the site along with some
  introductory documentation.
- `Gemfile` This is a list of Ruby dependencies that are needed to be able to
  run the site on your machine, it also helps us to keep the versions of the
  dependencies up to date with those on [github pages][gh-pages] where our site
  is hosted.
- `Rakefile` This defines a number of commands that you can run which help
  automate particular jobs when working on the site, everything from running the
  tests to publishing draft blog posts and adding new themes.
- `.travis.yml` We have a number of tests that we run on the site to make sure
  everything is working ok (such as making sure all our links point somewhere).
  We use a service called [Travis][travis] to make sure that whenever we make
  changes to the website our tests are automatically run and we can tell quickly
  if something has broken. This file contains instructions for Travis on how to
  run our tests.
- `Dockerfile` [Docker][docker] allows you to run lightweight "containers" on
  your machine (containers are like virtualbox but for single applications
  rather than entire operating systems). We give people the option of using
  docker to build and run the site, this file contains the instructions required
  for docker to build the image that you can build the site with.
- `.dockerignore` This tells which files docker can safely ignore when building
  its image for the site.

[collections]: https://jekyllrb.com/docs/collections/
[docker]:      https://www.docker.com/
[gh-pages]:    https://pages.github.com/versions/
[gimp]:        https://www.gimp.org/
[git]:         https://git-scm.com/
[github]:      https://github.com/CardiffMathematicsCodeClub/CardiffMathematicsCodeClub.github.io
[jekyll]:      https://jekyllrb.com/
[markdown]:    https://daringfireball.net/projects/markdown/
[travis]:      https://travis-ci.org/
