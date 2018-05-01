##
##############################################################################
#
# @file       gpspositionsensor.py
# @author     The LibrePilot Project, http://www.librepilot.org Copyright (C) 2017.
#             The OpenPilot Team, http://www.openpilot.org Copyright (C) 2010.
# @brief      Implementation of the GPSPositionSensor object. This file has been
#             automatically generated by the UAVObjectGenerator. For use with
#             the PyMite VM of the FlightPlan module.
#
# @note       Object definition file: gpspositionsensor.xml.
#             This is an automatically generated file.
#             DO NOT modify manually.
#
# @see        The GNU Public License (GPL) Version 3
#
#############################################################################/
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License
# for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
#

from librepilot.uavtalk.uavobject import *

# Field Latitude definition
class LatitudeField(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 2, 1)

# Field Longitude definition
class LongitudeField(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 2, 1)

# Field Altitude definition
class AltitudeField(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 6, 1)

# Field GeoidSeparation definition
class GeoidSeparationField(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 6, 1)

# Field Heading definition
class HeadingField(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 6, 1)

# Field Groundspeed definition
class GroundspeedField(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 6, 1)

# Field PDOP definition
class PDOPField(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 6, 1)

# Field HDOP definition
class HDOPField(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 6, 1)

# Field VDOP definition
class VDOPField(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 6, 1)

# Field Status definition
class StatusField(UAVObjectField):
    # Enumeration options
    NOGPS = 0
    NOFIX = 1
    FIX2D = 2
    FIX3D = 3
    def __init__(self):
        UAVObjectField.__init__(self, 7, 1)

# Field Satellites definition
class SatellitesField(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 0, 1)

# Field SensorType definition
class SensorTypeField(UAVObjectField):
    # Enumeration options
    UNKNOWN = 0
    NMEA = 1
    UBX = 2
    UBX7 = 3
    UBX8 = 4
    DJI = 5
    def __init__(self):
        UAVObjectField.__init__(self, 7, 1)

# Field AutoConfigStatus definition
class AutoConfigStatusField(UAVObjectField):
    # Enumeration options
    DISABLED = 0
    RUNNING = 1
    DONE = 2
    ERROR = 3
    def __init__(self):
        UAVObjectField.__init__(self, 7, 1)

# Field BaudRate definition
class BaudRateField(UAVObjectField):
    # Enumeration options
    N2400 = 0
    N4800 = 1
    N9600 = 2
    N19200 = 3
    N38400 = 4
    N57600 = 5
    N115200 = 6
    N230400 = 7
    UNKNOWN = 8
    def __init__(self):
        UAVObjectField.__init__(self, 7, 1)



# Object GPSPositionSensor definition
class GPSPositionSensor(UAVObject):
    # Object constants
    OBJID = 0x9DF1F67A

    # Constructor
    def __init__(self):
        UAVObject.__init__(self, GPSPositionSensor.OBJID)

        # Create object fields
        self.Latitude = LatitudeField()
        self.addField(self.Latitude)
        self.Longitude = LongitudeField()
        self.addField(self.Longitude)
        self.Altitude = AltitudeField()
        self.addField(self.Altitude)
        self.GeoidSeparation = GeoidSeparationField()
        self.addField(self.GeoidSeparation)
        self.Heading = HeadingField()
        self.addField(self.Heading)
        self.Groundspeed = GroundspeedField()
        self.addField(self.Groundspeed)
        self.PDOP = PDOPField()
        self.addField(self.PDOP)
        self.HDOP = HDOPField()
        self.addField(self.HDOP)
        self.VDOP = VDOPField()
        self.addField(self.VDOP)
        self.Status = StatusField()
        self.addField(self.Status)
        self.Satellites = SatellitesField()
        self.addField(self.Satellites)
        self.SensorType = SensorTypeField()
        self.addField(self.SensorType)
        self.AutoConfigStatus = AutoConfigStatusField()
        self.addField(self.AutoConfigStatus)
        self.BaudRate = BaudRateField()
        self.addField(self.BaudRate)

        # Read field data
        self.read()
        self.metadata.read()
