What's this?
------------

I wanted some simple way to send commands to the iBuddy device but seems that
the project [pybuddy](https://github.com/ewall/pybuddy) was abandoned and no
longer working (at least, not at Ubuntu 12.04).

It's called cibuddy because we want to use it as a Continuous Integration
alert.

BTW, this is an iBuddy:

![iBuddy device](http://www.gadgets.co.uk/mas_assets/full/IBUDDY.gif)


Usage
-----

This small class allows you to control the buddy easily:

    >>> buddy = Buddy()
    >>> buddy.beat()

Allowed commands:

- `.red()`: Turn the head on with color red.
- `.green()`: Turn the head on with color green.
- `.blue()`: Turn the head on with color blue.
- `.beat(time=.05)`: Beat the heart, the time var is the time between each beat.
- `.fly(time=.05)`: Move the winds.
- `.dance(time=.05)`: Make the buddy dance left-right-left-..-N!


Thanks
------

Thanks a lot to the guys that created pybuddy, to the guy that wrote [this
excellent article](http://imakethin.gs/blog/hacking-the-usb-i-buddy), and
to [this guy](http://www.youtube.com/watch?v=oHg5SJYRHA0).
