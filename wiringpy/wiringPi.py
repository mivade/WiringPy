from ctypes import *



class wiringPiNodeStruct(Structure):
    pass
wiringPiNodeStruct._fields_ = [
    ('pinBase', c_int),
    ('pinMax', c_int),
    ('fd', c_int),
    ('data0', c_uint),
    ('data1', c_uint),
    ('data2', c_uint),
    ('data3', c_uint),
    ('pinMode', CFUNCTYPE(None, POINTER(wiringPiNodeStruct), c_int, c_int)),
    ('pullUpDnControl', CFUNCTYPE(None, POINTER(wiringPiNodeStruct), c_int, c_int)),
    ('digitalRead', CFUNCTYPE(c_int, POINTER(wiringPiNodeStruct), c_int)),
    ('digitalWrite', CFUNCTYPE(None, POINTER(wiringPiNodeStruct), c_int, c_int)),
    ('pwmWrite', CFUNCTYPE(None, POINTER(wiringPiNodeStruct), c_int, c_int)),
    ('analogRead', CFUNCTYPE(c_int, POINTER(wiringPiNodeStruct), c_int)),
    ('analogWrite', CFUNCTYPE(None, POINTER(wiringPiNodeStruct), c_int, c_int)),
    ('next', POINTER(wiringPiNodeStruct)),
]
__all__ = ['wiringPiNodeStruct']
