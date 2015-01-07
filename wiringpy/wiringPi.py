from ctypes import *



def PI_THREAD(X): return void *X (void *dummy) # macro
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
INT_EDGE_RISING = 2 # Variable c_int '2'
PWM_MODE_MS = 0 # Variable c_int '0'
WPI_MODE_GPIO = 1 # Variable c_int '1'
WPI_MODE_GPIO_SYS = 2 # Variable c_int '2'
SOFT_PWM_OUTPUT = 4 # Variable c_int '4'
LOW = 0 # Variable c_int '0'
PWM_OUTPUT = 2 # Variable c_int '2'
PI_MODEL_A = 1 # Variable c_int '1'
PI_MODEL_B = 2 # Variable c_int '2'
GPIO_CLOCK = 3 # Variable c_int '3'
PI_MODEL_AP = 5 # Variable c_int '5'
PI_VERSION_2 = 4 # Variable c_int '4'
PI_MAKER_EGOMAN = 1 # Variable c_int '1'
PWM_TONE_OUTPUT = 6 # Variable c_int '6'
INT_EDGE_FALLING = 1 # Variable c_int '1'
PWM_MODE_BAL = 1 # Variable c_int '1'
PI_MODEL_CM = 4 # Variable c_int '4'
PI_VERSION_1 = 1 # Variable c_int '1'
WPI_MODE_PINS = 0 # Variable c_int '0'
SOFT_TONE_OUTPUT = 5 # Variable c_int '5'
NUM_PINS = 17 # Variable c_int '17'
PI_VERSION_UNKNOWN = 0 # Variable c_int '0'
HIGH = 1 # Variable c_int '1'
PI_MAKER_SONY = 2 # Variable c_int '2'
WPI_MODE_UNINITIALISED = -1 # Variable c_int '-0x00000000000000001'
INPUT = 0 # Variable c_int '0'
WPI_MODE_PIFACE = 4 # Variable c_int '4'
PI_MAKER_QISDA = 3 # Variable c_int '3'
PUD_OFF = 0 # Variable c_int '0'
PI_MODEL_BP = 3 # Variable c_int '3'
PI_VERSION_1_2 = 3 # Variable c_int '3'
PI_VERSION_1_1 = 2 # Variable c_int '2'
PI_MODEL_UNKNOWN = 0 # Variable c_int '0'
WPI_MODE_PHYS = 3 # Variable c_int '3'
PI_MAKER_UNKNOWN = 0 # Variable c_int '0'
OUTPUT = 1 # Variable c_int '1'
PUD_UP = 2 # Variable c_int '2'
INT_EDGE_BOTH = 3 # Variable c_int '3'
PUD_DOWN = 1 # Variable c_int '1'
INT_EDGE_SETUP = 0 # Variable c_int '0'
__all__ = ['INT_EDGE_RISING', 'PWM_MODE_MS', 'WPI_MODE_GPIO',
           'WPI_MODE_GPIO_SYS', 'SOFT_PWM_OUTPUT', 'LOW',
           'PWM_OUTPUT', 'PI_MODEL_A', 'PI_MODEL_B', 'GPIO_CLOCK',
           'PI_MODEL_AP', 'PI_VERSION_2', 'PI_MAKER_EGOMAN',
           'PWM_TONE_OUTPUT', 'INT_EDGE_FALLING', 'PWM_MODE_BAL',
           'PI_MODEL_CM', 'PI_THREAD', 'PI_VERSION_1',
           'WPI_MODE_PINS', 'NUM_PINS', 'PI_VERSION_UNKNOWN', 'HIGH',
           'PI_MAKER_QISDA', 'WPI_MODE_UNINITIALISED', 'INPUT',
           'wiringPiNodeStruct', 'PI_MAKER_SONY', 'WPI_MODE_PIFACE',
           'OUTPUT', 'PUD_OFF', 'PI_MODEL_BP', 'PI_VERSION_1_2',
           'PI_VERSION_1_1', 'PI_MODEL_UNKNOWN', 'WPI_MODE_PHYS',
           'PI_MAKER_UNKNOWN', 'SOFT_TONE_OUTPUT', 'PUD_UP',
           'INT_EDGE_BOTH', 'PUD_DOWN', 'INT_EDGE_SETUP']
