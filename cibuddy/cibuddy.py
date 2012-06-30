'''
Simple module to control the iBuddy device.

Commands explanation:

XBGRUDLR
  X = heart LED (1=on, 0=off)
  BGR are the bits for the 3 leds in the head (0=on, 1=off)
  UD are the wing positions, toggle between them to flap
  LR are used to twitch it left and right, only enable 1 at a time
'''

import usb
from time import sleep
from inspect import isfunction


def wait(arg):
    def inner_wait(function):
        def wrapper(*args, **kwargs):
            function(*args, **kwargs)
            sleep(arg)
        return wrapper
    if isfunction(arg):
        f = arg
        arg = 1  # Default sleep time
        return inner_wait(f)
    return inner_wait


def repeat(arg):
    def inner_repeat(function):
        def wrapper(*args, **kwargs):
            for _ in xrange(arg):
                function(*args, **kwargs)
        return wrapper
    if isfunction(arg):
        f = arg
        arg = 10  # Default repeat times
        return inner_repeat(f)
    return inner_repeat


class NoBuddyFound(Exception):
    pass


class Buddy(object):
    SETUP = (0x22, 0x09, 0x00, 0x02, 0x01, 0x00, 0x00, 0x00)
    HEADER = (0x55, 0x53, 0x42, 0x43, 0x00, 0x40, 0x02)
    VENDOR_ID = 0x1130
    POSSIBLE_PRODUCTS = (0x001, )

    def __init__(self):
        self.device = self.get_device()
        self.configuration = self.device.configurations[0]
        self.interface = self.configuration.interfaces[0][0]
        self.handler = self.get_handler()
        self.handler.reset()
        self._send(0xF0)  # Clean state

    def get_handler(self):
        if not hasattr(self, 'handler'):
            self.handler = self.device.open()
            try:
                self.handler.detachKernelDriver(0)
                self.handler.detachKernelDriver(1)
            except:
                pass
            self.handler.setConfiguration(self.configuration)
            self.handler.claimInterface(self.interface)
            self.handler.setAltInterface(self.interface)
        return self.handler

    def get_device(self):
        for bus in usb.busses():
            for device in bus.devices:
                if (device.idVendor == self.VENDOR_ID and
                    device.idProduct in self.POSSIBLE_PRODUCTS):
                    return device
        raise NoBuddyFound

    def _send(self, command):
        self.handler.controlMsg(0x21, 0x09, self.SETUP, 0x02, 0x01)
        message = self.HEADER + (command, )
        self.handler.controlMsg(0x21, 0x09, message, 0x02, 0x01)

    @repeat
    def beat(self, time=.5):
        for m in (0x70, 0xf0):
            self._send(m)
            sleep(time)

    @repeat
    def fly(self, time=.05):
        for m in (0xf0, 0xf8, 0xf4, 0xfC):
            self._send(m)
            sleep(time)

    @repeat
    def dance(self, time=.5):
        # Doesn't seem to work, but probably the problem is with my buddy hw
        self._send(0xF0)
        self._send(0xF3)
        sleep(time)
        self._send(0xF1)
        self._send(0xF2)

    @wait
    def red(self):
        self._send(0xe0)

    @wait
    def green(self, time):
        self._send(0xd0)

    @wait
    def blue(self):
        self._send(0xb0)

    @wait
    def off(self):
        self._send(0xf0)

if __name__ == '__main__':
    buddy = Buddy()
    try:
        # Example call
        buddy.dance()
    finally:
        buddy.off()
