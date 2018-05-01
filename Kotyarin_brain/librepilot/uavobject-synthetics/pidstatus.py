##
##############################################################################
#
# @file       pidstatus.py
# @author     The LibrePilot Project, http://www.librepilot.org Copyright (C) 2017.
#             The OpenPilot Team, http://www.openpilot.org Copyright (C) 2010.
# @brief      Implementation of the PIDStatus object. This file has been
#             automatically generated by the UAVObjectGenerator. For use with
#             the PyMite VM of the FlightPlan module.
#
# @note       Object definition file: pidstatus.xml.
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

# Field setpoint definition
class setpointField(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 6, 1)

# Field actual definition
class actualField(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 6, 1)

# Field error definition
class errorField(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 6, 1)

# Field ulow definition
class ulowField(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 6, 1)

# Field uhigh definition
class uhighField(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 6, 1)

# Field command definition
class commandField(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 6, 1)

# Field P definition
class PField(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 6, 1)

# Field I definition
class IField(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 6, 1)

# Field D definition
class DField(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 6, 1)



# Object PIDStatus definition
class PIDStatus(UAVObject):
    # Object constants
    OBJID = 0x75CF70A6

    # Constructor
    def __init__(self):
        UAVObject.__init__(self, PIDStatus.OBJID)

        # Create object fields
        self.setpoint = setpointField()
        self.addField(self.setpoint)
        self.actual = actualField()
        self.addField(self.actual)
        self.error = errorField()
        self.addField(self.error)
        self.ulow = ulowField()
        self.addField(self.ulow)
        self.uhigh = uhighField()
        self.addField(self.uhigh)
        self.command = commandField()
        self.addField(self.command)
        self.P = PField()
        self.addField(self.P)
        self.I = IField()
        self.addField(self.I)
        self.D = DField()
        self.addField(self.D)

        # Read field data
        self.read()
        self.metadata.read()
