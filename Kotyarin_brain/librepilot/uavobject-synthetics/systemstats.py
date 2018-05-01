##
##############################################################################
#
# @file       systemstats.py
# @author     The LibrePilot Project, http://www.librepilot.org Copyright (C) 2017.
#             The OpenPilot Team, http://www.openpilot.org Copyright (C) 2010.
# @brief      Implementation of the SystemStats object. This file has been
#             automatically generated by the UAVObjectGenerator. For use with
#             the PyMite VM of the FlightPlan module.
#
# @note       Object definition file: systemstats.xml.
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

# Field FlightTime definition
class FlightTimeField(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 5, 1)

# Field HeapRemaining definition
class HeapRemainingField(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 5, 1)

# Field CPUIdleTicks definition
class CPUIdleTicksField(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 5, 1)

# Field CPUZeroLoadTicks definition
class CPUZeroLoadTicksField(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 5, 1)

# Field EventSystemWarningID definition
class EventSystemWarningIDField(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 5, 1)

# Field ObjectManagerCallbackID definition
class ObjectManagerCallbackIDField(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 5, 1)

# Field ObjectManagerQueueID definition
class ObjectManagerQueueIDField(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 5, 1)

# Field IRQStackRemaining definition
class IRQStackRemainingField(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 4, 1)

# Field SystemModStackRemaining definition
class SystemModStackRemainingField(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 4, 1)

# Field SysSlotsFree definition
class SysSlotsFreeField(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 4, 1)

# Field SysSlotsActive definition
class SysSlotsActiveField(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 4, 1)

# Field UsrSlotsFree definition
class UsrSlotsFreeField(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 4, 1)

# Field UsrSlotsActive definition
class UsrSlotsActiveField(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 4, 1)

# Field CPULoad definition
class CPULoadField(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 3, 1)

# Field CPUTemp definition
class CPUTempField(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 0, 1)



# Object SystemStats definition
class SystemStats(UAVObject):
    # Object constants
    OBJID = 0xF1EC270E

    # Constructor
    def __init__(self):
        UAVObject.__init__(self, SystemStats.OBJID)

        # Create object fields
        self.FlightTime = FlightTimeField()
        self.addField(self.FlightTime)
        self.HeapRemaining = HeapRemainingField()
        self.addField(self.HeapRemaining)
        self.CPUIdleTicks = CPUIdleTicksField()
        self.addField(self.CPUIdleTicks)
        self.CPUZeroLoadTicks = CPUZeroLoadTicksField()
        self.addField(self.CPUZeroLoadTicks)
        self.EventSystemWarningID = EventSystemWarningIDField()
        self.addField(self.EventSystemWarningID)
        self.ObjectManagerCallbackID = ObjectManagerCallbackIDField()
        self.addField(self.ObjectManagerCallbackID)
        self.ObjectManagerQueueID = ObjectManagerQueueIDField()
        self.addField(self.ObjectManagerQueueID)
        self.IRQStackRemaining = IRQStackRemainingField()
        self.addField(self.IRQStackRemaining)
        self.SystemModStackRemaining = SystemModStackRemainingField()
        self.addField(self.SystemModStackRemaining)
        self.SysSlotsFree = SysSlotsFreeField()
        self.addField(self.SysSlotsFree)
        self.SysSlotsActive = SysSlotsActiveField()
        self.addField(self.SysSlotsActive)
        self.UsrSlotsFree = UsrSlotsFreeField()
        self.addField(self.UsrSlotsFree)
        self.UsrSlotsActive = UsrSlotsActiveField()
        self.addField(self.UsrSlotsActive)
        self.CPULoad = CPULoadField()
        self.addField(self.CPULoad)
        self.CPUTemp = CPUTempField()
        self.addField(self.CPUTemp)

        # Read field data
        self.read()
        self.metadata.read()
