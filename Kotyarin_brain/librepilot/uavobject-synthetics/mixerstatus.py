##
##############################################################################
#
# @file       mixerstatus.py
# @author     The LibrePilot Project, http://www.librepilot.org Copyright (C) 2017.
#             The OpenPilot Team, http://www.openpilot.org Copyright (C) 2010.
# @brief      Implementation of the MixerStatus object. This file has been
#             automatically generated by the UAVObjectGenerator. For use with
#             the PyMite VM of the FlightPlan module.
#
# @note       Object definition file: mixerstatus.xml.
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

# Field Mixer1 definition
class Mixer1Field(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 6, 1)

# Field Mixer2 definition
class Mixer2Field(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 6, 1)

# Field Mixer3 definition
class Mixer3Field(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 6, 1)

# Field Mixer4 definition
class Mixer4Field(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 6, 1)

# Field Mixer5 definition
class Mixer5Field(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 6, 1)

# Field Mixer6 definition
class Mixer6Field(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 6, 1)

# Field Mixer7 definition
class Mixer7Field(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 6, 1)

# Field Mixer8 definition
class Mixer8Field(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 6, 1)

# Field Mixer9 definition
class Mixer9Field(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 6, 1)

# Field Mixer10 definition
class Mixer10Field(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 6, 1)

# Field Mixer11 definition
class Mixer11Field(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 6, 1)

# Field Mixer12 definition
class Mixer12Field(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 6, 1)



# Object MixerStatus definition
class MixerStatus(UAVObject):
    # Object constants
    OBJID = 0x354C0F40

    # Constructor
    def __init__(self):
        UAVObject.__init__(self, MixerStatus.OBJID)

        # Create object fields
        self.Mixer1 = Mixer1Field()
        self.addField(self.Mixer1)
        self.Mixer2 = Mixer2Field()
        self.addField(self.Mixer2)
        self.Mixer3 = Mixer3Field()
        self.addField(self.Mixer3)
        self.Mixer4 = Mixer4Field()
        self.addField(self.Mixer4)
        self.Mixer5 = Mixer5Field()
        self.addField(self.Mixer5)
        self.Mixer6 = Mixer6Field()
        self.addField(self.Mixer6)
        self.Mixer7 = Mixer7Field()
        self.addField(self.Mixer7)
        self.Mixer8 = Mixer8Field()
        self.addField(self.Mixer8)
        self.Mixer9 = Mixer9Field()
        self.addField(self.Mixer9)
        self.Mixer10 = Mixer10Field()
        self.addField(self.Mixer10)
        self.Mixer11 = Mixer11Field()
        self.addField(self.Mixer11)
        self.Mixer12 = Mixer12Field()
        self.addField(self.Mixer12)

        # Read field data
        self.read()
        self.metadata.read()
