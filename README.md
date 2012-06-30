What's this?
------------

I wanted some simple way to send commands to the iBuddy device but seems that
the project [pybuddy](https://github.com/ewall/pybuddy) was abandoned and no
longer working (at least, no at Ubuntu 12.04).

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

- red
- green
- blue
- beat
- fly
- dance


Thanks
------

Thanks a lot to the guys that created pybuddy, and to the guy that wrote [this
excellent article](http://www.gadgets.co.uk/mas_assets/full/IBUDDY.gif).
