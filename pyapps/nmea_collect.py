#!/usr/bin/env python
"""
.. module:: nmea_collect.py

.. moduleauthor:: dr. Zoltan Siki <siki@agt.bme.hu>
                  Mate Kecskemeti <kecskemeti.mate3@gmail.com>

GNSS NMEA data collector. It can collect NMEA data from the GNSS receiver and write to txt file.
Uses bluetooth or serial communication.

    :param argv[1] (port): serial port or bluetooth MAC address, default COM1
    :param argv[2] (output file): name of the output file (e.g. results.txt), default stdout

"""

import re
import sys

sys.path.append('../pyapi')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        cm = sys.argv[1]
    else:
        cm = 'COM1'
#    if re.search('COM[0-9]$', cm) or '/dev/ttyUSB0' == cm:
#        from serialiface import SerialIface
#        iface = SerialIface('test', cm)
#    else:
#        from bluetoothiface import BluetoothIface
#        iface = BluetoothIface('test', cm, 1)
    from localiface import LocalIface
    from nmeagnssunit import NmeaGnssUnit
    from filewriter import FileWriter
    from gnss import Gnss
    iface = LocalIface('test', 'output.nmea')
    if len(sys.argv) > 2:
        fn = sys.argv[2]
    else:
        fn = 'stdout'
    wrt = FileWriter('', 'DEG', '.3f', '%Y-%m-%d %H:%M:%S', None, fn)
    mu = NmeaGnssUnit()
    # instrument
    g = Gnss('test', mu, iface, wrt)
    while g.measureIface.state == g.measureIface.IF_OK:
        g.Measure()