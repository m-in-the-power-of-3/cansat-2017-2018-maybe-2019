##
##############################################################################
#
# @file       attitudesimulated.py
# @author     The LibrePilot Project, http://www.librepilot.org Copyright (C) 2017.
#             The OpenPilot Team, http://www.openpilot.org Copyright (C) 2010.
# @brief      Implementation of the AttitudeSimulated object. This file has been
#             automatically generated by the UAVObjectGenerator. For use with
#             the PyMite VM of the FlightPlan module.
#
# @note       Object definition file: attitudesimulated.xml.
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

# Field q1 definition
class q1Field(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 6, 1)

# Field q2 definition
class q2Field(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 6, 1)

# Field q3 definition
class q3Field(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 6, 1)

# Field q4 definition
class q4Field(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 6, 1)

# Field Roll definition
class RollField(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 6, 1)

# Field Pitch definition
class PitchField(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 6, 1)

# Field Yaw definition
class YawField(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 6, 1)

# Field Velocity definition
class VelocityField(UAVObjectField):
    # Array element names
    NORTH = 0
    EAST = 1
    DOWN = 2
    def __init__(self):
        UAVObjectField.__init__(self, 6, 3)

# Field Position definition
class PositionField(UAVObjectField):
    # Array element names
    NORTH = 0
    EAST = 1
    DOWN = 2
    def __init__(self):
        UAVObjectField.__init__(self, 6, 3)



# Object AttitudeSimulated definition
class AttitudeSimulated(UAVObject):
    # Object constants
    OBJID = 0x9266CE74

    # Constructor
    def __init__(self):
        UAVObject.__init__(self, AttitudeSimulated.OBJID)

        # Create object fields
        self.q1 = q1Field()
        self.addField(self.q1)
        self.q2 = q2Field()
        self.addField(self.q2)
        self.q3 = q3Field()
        self.addField(self.q3)
        self.q4 = q4Field()
        self.addField(self.q4)
        self.Roll = RollField()
        self.addField(self.Roll)
        self.Pitch = PitchField()
        self.addField(self.Pitch)
        self.Yaw = YawField()
        self.addField(self.Yaw)
        self.Velocity = VelocityField()
        self.addField(self.Velocity)
        self.Position = PositionField()
        self.addField(self.Position)

        # Read field data
        self.read()
        self.metadata.read()
