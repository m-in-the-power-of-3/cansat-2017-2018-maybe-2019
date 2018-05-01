##
##############################################################################
#
# @file       groundpathfollowersettings.py
# @author     The LibrePilot Project, http://www.librepilot.org Copyright (C) 2017.
#             The OpenPilot Team, http://www.openpilot.org Copyright (C) 2010.
# @brief      Implementation of the GroundPathFollowerSettings object. This file has been
#             automatically generated by the UAVObjectGenerator. For use with
#             the PyMite VM of the FlightPlan module.
#
# @note       Object definition file: groundpathfollowersettings.xml.
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

# Field HorizontalVelMax definition
class HorizontalVelMaxField(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 6, 1)

# Field HorizontalVelMin definition
class HorizontalVelMinField(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 6, 1)

# Field CourseFeedForward definition
class CourseFeedForwardField(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 6, 1)

# Field VelocityFeedForward definition
class VelocityFeedForwardField(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 6, 1)

# Field HorizontalPosP definition
class HorizontalPosPField(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 6, 1)

# Field SpeedPI definition
class SpeedPIField(UAVObjectField):
    # Array element names
    KP = 0
    KI = 1
    KD = 2
    BETA = 3
    def __init__(self):
        UAVObjectField.__init__(self, 6, 4)

# Field ThrustLimit definition
class ThrustLimitField(UAVObjectField):
    # Array element names
    MIN = 0
    SLOWFORWARD = 1
    MAX = 2
    def __init__(self):
        UAVObjectField.__init__(self, 6, 3)

# Field UpdatePeriod definition
class UpdatePeriodField(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 2, 1)



# Object GroundPathFollowerSettings definition
class GroundPathFollowerSettings(UAVObject):
    # Object constants
    OBJID = 0xCD54334C

    # Constructor
    def __init__(self):
        UAVObject.__init__(self, GroundPathFollowerSettings.OBJID)

        # Create object fields
        self.HorizontalVelMax = HorizontalVelMaxField()
        self.addField(self.HorizontalVelMax)
        self.HorizontalVelMin = HorizontalVelMinField()
        self.addField(self.HorizontalVelMin)
        self.CourseFeedForward = CourseFeedForwardField()
        self.addField(self.CourseFeedForward)
        self.VelocityFeedForward = VelocityFeedForwardField()
        self.addField(self.VelocityFeedForward)
        self.HorizontalPosP = HorizontalPosPField()
        self.addField(self.HorizontalPosP)
        self.SpeedPI = SpeedPIField()
        self.addField(self.SpeedPI)
        self.ThrustLimit = ThrustLimitField()
        self.addField(self.ThrustLimit)
        self.UpdatePeriod = UpdatePeriodField()
        self.addField(self.UpdatePeriod)

        # Read field data
        self.read()
        self.metadata.read()
