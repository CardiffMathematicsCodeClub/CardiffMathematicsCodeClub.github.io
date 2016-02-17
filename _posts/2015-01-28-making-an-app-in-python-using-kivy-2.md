---
layout     : post
title      : "Making an App in python using Kivy - Part 2 - Widgets"
categories : tutorial
tags       : blog python kivy
author     : Timothy
comments   : true
---

In the [first part]({% post_url 2015-01-16-making-an-app-in-python-using-kivy-1 %})
I talked about how to create an app. Now I'm going to talk about the some of
different widgets that can be used in Kivy, that I found helpful.

## Widgets

In Kivy widgets are the building blocks of the GUI interface, which we created
for our app. The main app takes 1 widget, as the root widget, when built.

Kivy includes examples of how to use each of the widgets. I would recommend
looking through these to identify the best widget to use for each element of the
app.

In the [Hello World example][gist] from part 1 we see that on line 5 I imported
the label widget, so that it can be used in line 11 to create an label. For each
widget you want to use it is needed to be imported

### Screen Manager

In most apps you will require a different layout for each type of page.
For this I would recommend using the [screen manager][smanager],
although there are other options such as [carousel][carouselopt] depending on
your needs.

Below is a sample of the different screens we used in our group last year.

![Screen Manager](/res/blog_pics/kivy-screen-manager.png)

Note that the screen manager doesn't need to be the root widget leading to the
whole screen changing. For example you can have a vertical boxlayout (layouts
are explained next), with an header as the first widget and the screen manager
as the second.

```python
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty
from kivy.lang import Builder

Builder.load_file('screenmanager.kv')


class CustomScreen(Screen):
    hue = NumericProperty(0)


class ScreenManagerApp(App):

    def build(self):
        root = ScreenManager()
        for x in range(4):
            root.add_widget(CustomScreen(name='Screen %d' % x))
        return root

if __name__ == '__main__':
    ScreenManagerApp().run()
```

The KV code can be found [here][gist1]

Here we making the screen manager the root widget with there being 4 screens
added to the manager. Each of the screens are similar with a different
background colour and number.

If we take a look at the code for the next button in the KV we have

```
Button:
    text: 'Next screen'
    size_hint: None, None
    pos_hint: {'right': 1}
    size: 150, 50
    on_release: root.manager.current = root.manager.next()
```

- Text is the text that is displayed on the button
- size_hint is used by default to decide on how big a widget will be, it
defaults to (1, 1).
- pos_hint
- size is how big the button is, note that if size_hint isn't set to (None,
None) then this doesn't have an effect.
- on_release is the action that occurs once a user has click on and released the
button.

Lets take a closer look at what on_release is doing. Firstly root refers to the
custom screen as looking in the KV code it comes under _CustomScreen_. Next we
are referring to the [manager attribute][mattribute] of the screen which gives
us the screen manager it's attached to. We are then setting the [current
attribute][attribute] of the screen manager to change the screen.

Now to see what it's being set to we see that it follows the root.manager again.
But this time we are using the [next method][method] of the screen manager to
get the name of next screen. The next method looks at the
[screen_names][screennames], which is a list the screens added to the screen
manager. The order in which next() and similarly [previous()][previous] works is
based upon the order that the screens were added to the screen manager.

#### Transitions

We also see that in the above example there are multiple transitions.
The transitions are changed by changing the screen managers
[transition attribute][transition].

### Layouts

In order to have multiple widgets there are layout out widgets that allow
multiple widgets to be attached to it.

There are 6 different [layout widgets][laywidgets] in kivy.

- [BoxLayout][Box]
- [GridLayout][Grid]
- [StackLayout][Stack]
- [AnchorLayout][Anchor]
- [FloatLayout][Float]
- [RelativeLayout][Relative]

Of the different layouts in our we used boxlayout the most and grid for tables.

In the boxlayout example from part 1, [code can be found here][gist2]. We note
that size hinting was used here but what does it do?

In the screen manager example we see that just size_hint was used. This took 2
values the first for the x direction and then for the y direction. But in the
Boxlayout example they are changed separately.

So for the first block pictured below, it is a vertical boxlayout.

![Vertical Layout](/res/blog_pics/kivy-boxlayout-example-1.png)

We see that the size_hint_y hasn't been changed so virtually each button is
taking up a third of the available space. What has been changed is the
size_hint_x, so the first and the last buttons are only 40% of the available
width that they were given. The second button is given 20% of the width. Due to
the positioning of each button means that they don't overlap.

[gist]: https://gist.github.com/timothyf1/75b20064a50e51651efa
[smanager]: http://kivy.org/docs/api-kivy.uix.screenmanager.html
[carouselopt]: http://kivy.org/docs/api-kivy.uix.carousel.html
[gist1]: https://gist.github.com/timothyf1/1f51fc7cdcf9b7a12694#file-screenmanager-kv
[mattribute]: http://kivy.org/docs/api-kivy.uix.screenmanager.html#kivy.uix.screenmanager.Screen.manager
[attribute]: http://kivy.org/docs/api-kivy.uix.screenmanager.html#kivy.uix.screenmanager.ScreenManager.current
[method]: http://kivy.org/docs/api-kivy.uix.screenmanager.html#kivy.uix.screenmanager.ScreenManager.next
[screennames]: http://kivy.org/docs/api-kivy.uix.screenmanager.html#kivy.uix.screenmanager.ScreenManager.screen_names
[previous]: http://kivy.org/docs/api-kivy.uix.screenmanager.html#kivy.uix.screenmanager.ScreenManager.previous
[transition]: http://kivy.org/docs/api-kivy.uix.screenmanager.html#kivy.uix.screenmanager.ScreenManager.transition
[laywidgets]: http://kivy.org/docs/guide/widgets.html#organize-with-layouts
[Box]: http://kivy.org/docs/api-kivy.uix.boxlayout.html
[Grid]: http://kivy.org/docs/api-kivy.uix.gridlayout.html
[Stack]: http://kivy.org/docs/api-kivy.uix.scatterlayout.html
[Anchor]: http://kivy.org/docs/api-kivy.uix.anchorlayout.html
[Float]: http://kivy.org/docs/api-kivy.uix.floatlayout.html
[Relative]: http://kivy.org/docs/api-kivy.uix.relativelayout.html
[gist2]: https://gist.github.com/timothyf1/adeb2eaa141ac4314981
