"""Pythonic access to the WiringPi Raspberry Pi GPIO library."""

import ctypes
from wiringPi import *

# Constants
# -----------------------------------------------------------------------------

__version__ = '0.1.0'

# Exception types
# -----------------------------------------------------------------------------

class WiringPyError(Exception):
    pass

# Basic setup
# -----------------------------------------------------------------------------
    
try:
    _dll = ctypes.CDLL('libwiringPi.so.2.0')
except OSError:
    raise RuntimeError('WiringPi not found. Please install it.')

def _chk(cmd):
    """Simple checking of a command that should return 0."""
    if cmd == 0:
        return
    else:
        raise WiringPyError("Error executing command. Return code: " + cmd)

def setup(scheme='wiringpi'):
    """Initialize GPIO access and set the pin numbering format.

    Parameters
    ----------
    scheme : str
        A string specifying the numbering scheme to use. Valid options
        are 'wiringpi' (default), 'gpio' (the Broadcom pin numbering
        scheme), 'physical' (counting pin numbers on the P1 connector
        the Raspberry Pi B(+), and 'sys' (uses the ``/sys/class/gpio``
        interface after proper setup with the ``gpio`` utility and
        uses the Broadcom nubmering scheme).

    Notes
    -----
    With the exception of the ``sys`` scheme, all schemes require
    running as root. It is therefore recommended that the ``sys``
    numbering scheme is used, and may be made the default option in
    future versions of WiringPy.

    """
    assert isinstance(scheme, (str, unicode))
    scheme = scheme.lower()
    if scheme == 'wiringpi':
        _chk(_dll.wiringPiSetup())
    elif scheme == 'gpio':
        _chk(_dll.wiringPiSetupGpio())
    elif scheme == 'phys':
        _chk(_dll.wiringPiSetupPhys())
    elif scheme == 'sys':
        _chk(_dll.wiringPiSetupSys())
    else:
        raise WiringPyError("Unknown pin numbering scheme: " + scheme)

def pin_mode(pin, mode):
    """Setup a pin's mode.

    Parameters
    ----------
    pin : int
        Pin number to setup.
    mode : int
        Pin mode to use.

    Notes
    -----
    The pin mode must be one of:

    * ``wiringpy.INPUT``
    * ``wiringpy.OUTPUT``
    * ``wiringpy.PWM_OUTPUT``
    * ``wiringpy.GPIO_CLOCK``
    * ``wiringpy.SOFT_PWM_OUTPUT``
    * ``wiringpy.SOFT_TONE_OUTPUT``
    * ``wiringpy.PWM_TONE_OUTPUT``

    """
    # TODO: proper pin number checking (depending on Pi model, etc.)
    assert isinstance(pin, int)
    assert isinstance(mode, int)
    if mode not in [
            'INPUT', 'OUTPUT', 'PWM_OUTPUT', 'GPIO_CLOCK',
            'SOFT_PWM_OUTPUT', 'SOFT_TONE_OUTPUT', 'PWM_TONE_OUTPUT']:
        raise WiringPyError("Invalid pin mode.")
    _dll.pinMode(pin, mode)

def pull_up_down_control(pin, pud):
    """Configure the pull-up or pull-down resistor mode.

    This sets the pull-up or pull-down resistor mode on the given pin,
    which should be set as an input. Unlike the Arduino, the BCM2835
    has both pull-up an down internal resistors. The parameter pud
    should be; PUD_OFF, (no pull up/down), PUD_DOWN (pull to ground)
    or PUD_UP (pull to 3.3v) The internal pull up/down resistors have
    a value of approximately 50 kohm on the Raspberry Pi.

    This function has no effect on the Raspberry Pi’s GPIO pins when
    in Sys mode. If you need to activate a pull-up/pull-down, then you
    can do it with the gpio program in a script before you start your
    program.

    """
    # TODO: proper pin number checking (depending on Pi model, etc.)
    assert isinstance(pin, int)
    assert isinstance(pud, int)
    _dll.pullUpDnControl(pin, pud)

def digital_write(pin, value):
    """Set a digital value."""

def digital_read(pin):
    """Read a digital pin."""

    