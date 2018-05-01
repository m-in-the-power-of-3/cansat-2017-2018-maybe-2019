##
##############################################################################
#
# @file       stabilizationstatus.py
# @author     The LibrePilot Project, http://www.librepilot.org Copyright (C) 2017.
#             The OpenPilot Team, http://www.openpilot.org Copyright (C) 2010.
# @brief      Implementation of the StabilizationStatus object. This file has been
#             automatically generated by the UAVObjectGenerator. For use with
#             the PyMite VM of the FlightPlan module.
#
# @note       Object definition file: stabilizationstatus.xml.
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

# Field OuterLoop definition
class OuterLoopField(UAVObjectField):
    # Enumeration options
    DIRECT = 0
    DIRECTWITHLIMITS = 1
    ATTITUDE = 2
    RATTITUDE = 3
    WEAKLEVELING = 4
    ALTITUDE = 5
    ALTITUDEVARIO = 6
    SYSTEMIDENT = 7
    # Array element names
    ROLL = 0
    PITCH = 1
    YAW = 2
    THRUST = 3
    def __init__(self):
        UAVObjectField.__init__(self, 7, 4)

# Field InnerLoop definition
class InnerLoopField(UAVObjectField):
    # Enumeration options
    DIRECT = 0
    VIRTUALFLYBAR = 1
    ACRO = 2
    AXISLOCK = 3
    RATE = 4
    CRUISECONTROL = 5
    SYSTEMIDENT = 6
    # Array element names
    ROLL = 0
    PITCH = 1
    YAW = 2
    THRUST = 3
    def __init__(self):
        UAVObjectField.__init__(self, 7, 4)



# Object StabilizationStatus definition
class StabilizationStatus(UAVObject):
    # Object constants
    OBJID = 0x2632C56

    # Constructor
    def __init__(self):
        UAVObject.__init__(self, StabilizationStatus.OBJID)

        # Create object fields
        self.OuterLoop = OuterLoopField()
        self.addField(self.OuterLoop)
        self.InnerLoop = InnerLoopField()
        self.addField(self.InnerLoop)

        # Read field data
        self.read()
        self.metadata.read()
