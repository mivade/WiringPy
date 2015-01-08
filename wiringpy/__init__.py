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

# Internal utility functions
# -----------------------------------------------------------------------------

def _chk(cmd):
    """Simple checking of a command that should return 0."""
    if cmd == 0:
        return
    else:
        raise WiringPyError("Error executing command. Return code: " + cmd)

def _check_pin(pin):
    """Check that a pin number is valid."""
    # TODO: proper checking
    assert isinstance(pin, int)

def _check_mode(mode):
    """Check that a mode number is valid."""
    # TODO: proper checking
    assert isinstance(mode, int)

# Basic setup
# -----------------------------------------------------------------------------
    
try:
    _dll = ctypes.CDLL('libwiringPi.so.2.0')
except OSError:
    raise RuntimeError('WiringPi not found. Please install it.')

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
    _check_pin(pin)
    _check_mode(mode)
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
    _check_pin(pin)
    assert isinstance(pud, int)
    _dll.pullUpDnControl(pin, pud)

def digital_read(pin):
    """This function returns the value read at the given pin. It will
    be HIGH or LOW (1 or 0) depending on the logic level at the
    pin.

    Parameters
    ----------
    pin : int
        Pin number to read.

    """
    _check_pin(pin)
    return _dll.digitalRead(pin)

def digital_write(pin, value):
    """Writes the value HIGH or LOW (1 or 0) to the given pin which
    must have been previously set as an output.

    Parameters
    ----------
    pin : int
        Pin number to write to.
    value : int or bool
        Digital value to write.

    Notes
    -----
    WiringPi treats any non-zero number as HIGH, however 0 is the only
    representation of LOW.

    """
    _check_pin(pin)
    assert isinstance(value, (int, bool))
    _dll.digitalWrite(pin, value)

def pwm_write(pin, value):
    """Writes the value to the PWM register for the given pin.

    Parameters
    ----------
    pin : int
        Pin number to write to.
    value : int or bool
        PWM value to write.

    Notes
    -----
    The Raspberry Pi has one on-board PWM pin, WiringPi pin 1
    (BMC_GPIO 18, Phys 12) and the range is 0-1024. Other PWM devices
    may have other PWM ranges.

    This function is not able to control the Pi’s on-board PWM when in
    Sys mode.

    """
    _check_pin(pin)
    assert isinstance(value, int)
    assert 0 <= value <= 1024
    _dll.pwmWrite(pin, value)

def analog_read(pin):
    """Read the supplied analog input pin.

    Parameters
    ----------
    pin : int
        Pin number to read from.

    Notes
    -----
    You will need to register additional analog modules to enable this
    function for devices such as the Gertboard, quick2Wire analog
    board, etc.

    """
    _check_pin(pin)
    return _dll.analogRead(pin)

def analog_write(pin, value):
    """Write the given value to the supplied analog pin.

    Parameters
    ----------
    pin : int
        Pin number to write to.
    value : int or bool
        Analog value to write.    

    Notes
    -----
    You will need to register additional analog modules to enable this
    function for devices such as the Gertboard.

    """
    _check_pin(pin)
    assert isinstance(value, int)
    _dll.analogWrite(pin, value)