#!/usr/bin/python
__author__="cooke"
__date__ ="$02-Feb-2012 15:26:23$"

"""
Initialize a basic broadcast slave channel for listening to
an ANT+ Bicycle cadence and speed senser, using raw messages
and event handlers.

"""
import sys
import time

from ant.core import driver
from ant.core import event
from ant.core.constants import RESPONSE_NO_ERROR
from ant.core.message import ChannelAssignMessage
from ant.core.message import ChannelFrequencyMessage
from ant.core.message import ChannelIDMessage
from ant.core.message import ChannelOpenMessage
from ant.core.message import ChannelPeriodMessage
from ant.core.message import ChannelSearchTimeoutMessage
from ant.core.message import NetworkKeyMessage
from ant.core.message import SystemResetMessage
from antpluslistener.core import SofieHdfFormatLogWriter
# USB1 ANT stick interface. Running `dmesg | tail -n 25` after plugging the
# stick on a USB port should tell you the exact interface.
SERIAL = '/dev/ttyUSB0'

# If set to True, the stick's driver will dump everything it reads/writes
# from/to the stick.
# Some demos depend on this setting being True, so unless you know what you
# are doing, leave it as is.
DEBUG = True

# Set to None to disable logging
#LOG = None
LOG = SofieHdfFormatLogWriter.LogWriter()

# ========== DO NOT CHANGE ANYTHING BELOW THIS LINE ==========
print "Using log file:", LOG.filename
print ""

 # Event callback
class MyCallback(event.EventCallback):
    def process(self, msg):
        print msg

if __name__ == '__main__':
    NETKEY = '\xB9\xA5\x21\xFB\xBD\x72\xC3\x45'
    # Initialize driver
    stick = driver.USB1Driver(SERIAL, log=LOG, debug=DEBUG,baud_rate=4800)
    stick.open()

    # Initialize event machine
    evm = event.EventMachine(stick)
    evm.registerCallback(MyCallback())
    evm.start()

    # Reset
    msg = SystemResetMessage()
    stick.write(msg.encode())
    time.sleep(1)

    # Set network key
    msg = NetworkKeyMessage(key=NETKEY)
    stick.write(msg.encode())
    if evm.waitForAck(msg) != RESPONSE_NO_ERROR:
        sys.exit()

    # Initialize it as a receiving channel using our network key
    msg = ChannelAssignMessage()
    stick.write(msg.encode())
    if evm.waitForAck(msg) != RESPONSE_NO_ERROR:
        sys.exit()

    # Now set the channel id for pairing with an ANT+ bike cadence/speed sensor
    msg = ChannelIDMessage(device_type=121)
    stick.write(msg.encode())
    if evm.waitForAck(msg) != RESPONSE_NO_ERROR:
        sys.exit()

    # Listen forever and ever (not really, but for a long time)
    msg = ChannelSearchTimeoutMessage(timeout=255)
    stick.write(msg.encode())
    if evm.waitForAck(msg) != RESPONSE_NO_ERROR:
        sys.exit()

    # We want a ~4.05 Hz transmission period
    msg = ChannelPeriodMessage(period=8085)
    stick.write(msg.encode())
    if evm.waitForAck(msg) != RESPONSE_NO_ERROR:
        sys.exit()

    # And ANT frequency 57, of course
    msg = ChannelFrequencyMessage(frequency=57)
    stick.write(msg.encode())
    if evm.waitForAck(msg) != RESPONSE_NO_ERROR:
        sys.exit()

    # Time to go live
    msg = ChannelOpenMessage()
    stick.write(msg.encode())
    if evm.waitForAck(msg) != RESPONSE_NO_ERROR:
        sys.exit()

    print "Listening for ANT events (120 seconds)..."
    time.sleep(120)

    # Shutdown
    msg = SystemResetMessage()
    stick.write(msg.encode())
    time.sleep(1)

    evm.stop()
    stick.close()