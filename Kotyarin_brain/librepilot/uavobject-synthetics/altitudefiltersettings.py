##
##############################################################################
#
# @file       altitudefiltersettings.py
# @author     The LibrePilot Project, http://www.librepilot.org Copyright (C) 2017.
#             The OpenPilot Team, http://www.openpilot.org Copyright (C) 2010.
# @brief      Implementation of the AltitudeFilterSettings object. This file has been
#             automatically generated by the UAVObjectGenerator. For use with
#             the PyMite VM of the FlightPlan module.
#
# @note       Object definition file: altitudefiltersettings.xml.
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

# Field AccelLowPassKp definition
class AccelLowPassKpField(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 6, 1)

# Field AccelDriftKi definition
class AccelDriftKiField(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 6, 1)

# Field InitializationAccelDriftKi definition
class InitializationAccelDriftKiField(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 6, 1)

# Field BaroKp definition
class BaroKpField(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 6, 1)



# Object AltitudeFilterSettings definition
class AltitudeFilterSettings(UAVObject):
    # Object constants
    OBJID = 0xE611042C

    # Constructor
    def __init__(self):
        UAVObject.__init__(self, AltitudeFilterSettings.OBJID)

        # Create object fields
        self.AccelLowPassKp = AccelLowPassKpField()
        self.addField(self.AccelLowPassKp)
        self.AccelDriftKi = AccelDriftKiField()
        self.addField(self.AccelDriftKi)
        self.InitializationAccelDriftKi = InitializationAccelDriftKiField()
        self.addField(self.InitializationAccelDriftKi)
        self.BaroKp = BaroKpField()
        self.addField(self.BaroKp)

        # Read field data
        self.read()
        self.metadata.read()
