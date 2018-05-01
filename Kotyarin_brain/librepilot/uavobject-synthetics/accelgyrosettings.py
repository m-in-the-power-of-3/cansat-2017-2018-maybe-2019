##
##############################################################################
#
# @file       accelgyrosettings.py
# @author     The LibrePilot Project, http://www.librepilot.org Copyright (C) 2017.
#             The OpenPilot Team, http://www.openpilot.org Copyright (C) 2010.
# @brief      Implementation of the AccelGyroSettings object. This file has been
#             automatically generated by the UAVObjectGenerator. For use with
#             the PyMite VM of the FlightPlan module.
#
# @note       Object definition file: accelgyrosettings.xml.
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

# Field accel_bias definition
class accel_biasField(UAVObjectField):
    # Array element names
    X = 0
    Y = 1
    Z = 2
    def __init__(self):
        UAVObjectField.__init__(self, 6, 3)

# Field accel_scale definition
class accel_scaleField(UAVObjectField):
    # Array element names
    X = 0
    Y = 1
    Z = 2
    def __init__(self):
        UAVObjectField.__init__(self, 6, 3)

# Field accel_temp_coeff definition
class accel_temp_coeffField(UAVObjectField):
    # Array element names
    X = 0
    Y = 1
    Z = 2
    def __init__(self):
        UAVObjectField.__init__(self, 6, 3)

# Field gyro_bias definition
class gyro_biasField(UAVObjectField):
    # Array element names
    X = 0
    Y = 1
    Z = 2
    def __init__(self):
        UAVObjectField.__init__(self, 6, 3)

# Field gyro_scale definition
class gyro_scaleField(UAVObjectField):
    # Array element names
    X = 0
    Y = 1
    Z = 2
    def __init__(self):
        UAVObjectField.__init__(self, 6, 3)

# Field gyro_temp_coeff definition
class gyro_temp_coeffField(UAVObjectField):
    # Array element names
    X = 0
    X2 = 1
    Y = 2
    Y2 = 3
    Z = 4
    Z2 = 5
    def __init__(self):
        UAVObjectField.__init__(self, 6, 6)

# Field temp_calibrated_extent definition
class temp_calibrated_extentField(UAVObjectField):
    # Array element names
    MIN = 0
    MAX = 1
    def __init__(self):
        UAVObjectField.__init__(self, 6, 2)



# Object AccelGyroSettings definition
class AccelGyroSettings(UAVObject):
    # Object constants
    OBJID = 0x1262B2D0

    # Constructor
    def __init__(self):
        UAVObject.__init__(self, AccelGyroSettings.OBJID)

        # Create object fields
        self.accel_bias = accel_biasField()
        self.addField(self.accel_bias)
        self.accel_scale = accel_scaleField()
        self.addField(self.accel_scale)
        self.accel_temp_coeff = accel_temp_coeffField()
        self.addField(self.accel_temp_coeff)
        self.gyro_bias = gyro_biasField()
        self.addField(self.gyro_bias)
        self.gyro_scale = gyro_scaleField()
        self.addField(self.gyro_scale)
        self.gyro_temp_coeff = gyro_temp_coeffField()
        self.addField(self.gyro_temp_coeff)
        self.temp_calibrated_extent = temp_calibrated_extentField()
        self.addField(self.temp_calibrated_extent)

        # Read field data
        self.read()
        self.metadata.read()
