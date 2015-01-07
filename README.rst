WiringPy
========

WiringPy is a wrapper around the excellent WiringPi_ C library for
using the GPIO pins on `Raspberry Pis`_. It is intended to replace
`WiringPi2-Python`_ which has a few issues and limitations as it is
only a thin wrapper using SWIG_ and contains very limited
documentation.

One of the goals of WiringPy is to be a more Pythonic wrapper, and so
function names are often different from the base WiringPi C function
names. In most cases, this just involves replacing camel case with
underscores, so for example, ``pinMode`` in the C version is
``pin_mode`` here.

.. _WiringPi: http://wiringpi.com/
.. _Raspberry Pis: http://www.raspberrypi.org/
.. _WiringPi2-Python: https://github.com/WiringPi/WiringPi2-Python
.. _SWIG: http://www.swig.org/

TODO
----

This is very much a work in progress. Things still to do (in no
particular order):

* Implement additional libraries (e.g., I2C, SPI, etc.)
* Full Sphinx documentation
* Unit testing

License
-------

This software is distributed under the terms of the `GNU
LGPLv3`__. Note that the header files in the ``include`` directory are
directly copied from the original WiringPi repository for ease of code
generation.

__ http://www.gnu.org/copyleft/lesser.html
