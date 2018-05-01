##
##############################################################################
#
# @file       stabilizationbank.py
# @author     The LibrePilot Project, http://www.librepilot.org Copyright (C) 2017.
#             The OpenPilot Team, http://www.openpilot.org Copyright (C) 2010.
# @brief      Implementation of the StabilizationBank object. This file has been
#             automatically generated by the UAVObjectGenerator. For use with
#             the PyMite VM of the FlightPlan module.
#
# @note       Object definition file: stabilizationbank.xml.
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

# Field RollRatePID definition
class RollRatePIDField(UAVObjectField):
    # Array element names
    KP = 0
    KI = 1
    KD = 2
    ILIMIT = 3
    def __init__(self):
        UAVObjectField.__init__(self, 6, 4)

# Field PitchRatePID definition
class PitchRatePIDField(UAVObjectField):
    # Array element names
    KP = 0
    KI = 1
    KD = 2
    ILIMIT = 3
    def __init__(self):
        UAVObjectField.__init__(self, 6, 4)

# Field YawRatePID definition
class YawRatePIDField(UAVObjectField):
    # Array element names
    KP = 0
    KI = 1
    KD = 2
    ILIMIT = 3
    def __init__(self):
        UAVObjectField.__init__(self, 6, 4)

# Field RollPI definition
class RollPIField(UAVObjectField):
    # Array element names
    KP = 0
    KI = 1
    ILIMIT = 2
    def __init__(self):
        UAVObjectField.__init__(self, 6, 3)

# Field PitchPI definition
class PitchPIField(UAVObjectField):
    # Array element names
    KP = 0
    KI = 1
    ILIMIT = 2
    def __init__(self):
        UAVObjectField.__init__(self, 6, 3)

# Field YawPI definition
class YawPIField(UAVObjectField):
    # Array element names
    KP = 0
    KI = 1
    ILIMIT = 2
    def __init__(self):
        UAVObjectField.__init__(self, 6, 3)

# Field ManualRate definition
class ManualRateField(UAVObjectField):
    # Array element names
    ROLL = 0
    PITCH = 1
    YAW = 2
    def __init__(self):
        UAVObjectField.__init__(self, 4, 3)

# Field MaximumRate definition
class MaximumRateField(UAVObjectField):
    # Array element names
    ROLL = 0
    PITCH = 1
    YAW = 2
    def __init__(self):
        UAVObjectField.__init__(self, 4, 3)

# Field RollMax definition
class RollMaxField(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 3, 1)

# Field PitchMax definition
class PitchMaxField(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 3, 1)

# Field YawMax definition
class YawMaxField(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 3, 1)

# Field StickExpo definition
class StickExpoField(UAVObjectField):
    # Array element names
    ROLL = 0
    PITCH = 1
    YAW = 2
    def __init__(self):
        UAVObjectField.__init__(self, 0, 3)

# Field AcroInsanityFactor definition
class AcroInsanityFactorField(UAVObjectField):
    # Array element names
    ROLL = 0
    PITCH = 1
    YAW = 2
    def __init__(self):
        UAVObjectField.__init__(self, 3, 3)

# Field EnablePiroComp definition
class EnablePiroCompField(UAVObjectField):
    # Enumeration options
    FALSE = 0
    TRUE = 1
    def __init__(self):
        UAVObjectField.__init__(self, 7, 1)

# Field FpvCamTiltCompensation definition
class FpvCamTiltCompensationField(UAVObjectField):
    def __init__(self):
        UAVObjectField.__init__(self, 3, 1)

# Field EnableThrustPIDScaling definition
class EnableThrustPIDScalingField(UAVObjectField):
    # Enumeration options
    FALSE = 0
    TRUE = 1
    def __init__(self):
        UAVObjectField.__init__(self, 7, 1)

# Field ThrustPIDScaleCurve definition
class ThrustPIDScaleCurveField(UAVObjectField):
    # Array element names
    N0 = 0
    N25 = 1
    N50 = 2
    N75 = 3
    N100 = 4
    def __init__(self):
        UAVObjectField.__init__(self, 0, 5)

# Field ThrustPIDScaleSource definition
class ThrustPIDScaleSourceField(UAVObjectField):
    # Enumeration options
    MANUALCONTROLTHROTTLE = 0
    STABILIZATIONDESIREDTHRUST = 1
    ACTUATORDESIREDTHRUST = 2
    def __init__(self):
        UAVObjectField.__init__(self, 7, 1)

# Field ThrustPIDScaleTarget definition
class ThrustPIDScaleTargetField(UAVObjectField):
    # Enumeration options
    PID = 0
    PI = 1
    PD = 2
    ID = 3
    P = 4
    I = 5
    D = 6
    def __init__(self):
        UAVObjectField.__init__(self, 7, 1)

# Field ThrustPIDScaleAxes definition
class ThrustPIDScaleAxesField(UAVObjectField):
    # Enumeration options
    ROLLPITCHYAW = 0
    ROLLPITCH = 1
    ROLLYAW = 2
    ROLL = 3
    PITCHYAW = 4
    PITCH = 5
    YAW = 6
    def __init__(self):
        UAVObjectField.__init__(self, 7, 1)



# Object StabilizationBank definition
class StabilizationBank(UAVObject):
    # Object constants
    OBJID = 0x373871F0

    # Constructor
    def __init__(self):
        UAVObject.__init__(self, StabilizationBank.OBJID)

        # Create object fields
        self.RollRatePID = RollRatePIDField()
        self.addField(self.RollRatePID)
        self.PitchRatePID = PitchRatePIDField()
        self.addField(self.PitchRatePID)
        self.YawRatePID = YawRatePIDField()
        self.addField(self.YawRatePID)
        self.RollPI = RollPIField()
        self.addField(self.RollPI)
        self.PitchPI = PitchPIField()
        self.addField(self.PitchPI)
        self.YawPI = YawPIField()
        self.addField(self.YawPI)
        self.ManualRate = ManualRateField()
        self.addField(self.ManualRate)
        self.MaximumRate = MaximumRateField()
        self.addField(self.MaximumRate)
        self.RollMax = RollMaxField()
        self.addField(self.RollMax)
        self.PitchMax = PitchMaxField()
        self.addField(self.PitchMax)
        self.YawMax = YawMaxField()
        self.addField(self.YawMax)
        self.StickExpo = StickExpoField()
        self.addField(self.StickExpo)
        self.AcroInsanityFactor = AcroInsanityFactorField()
        self.addField(self.AcroInsanityFactor)
        self.EnablePiroComp = EnablePiroCompField()
        self.addField(self.EnablePiroComp)
        self.FpvCamTiltCompensation = FpvCamTiltCompensationField()
        self.addField(self.FpvCamTiltCompensation)
        self.EnableThrustPIDScaling = EnableThrustPIDScalingField()
        self.addField(self.EnableThrustPIDScaling)
        self.ThrustPIDScaleCurve = ThrustPIDScaleCurveField()
        self.addField(self.ThrustPIDScaleCurve)
        self.ThrustPIDScaleSource = ThrustPIDScaleSourceField()
        self.addField(self.ThrustPIDScaleSource)
        self.ThrustPIDScaleTarget = ThrustPIDScaleTargetField()
        self.addField(self.ThrustPIDScaleTarget)
        self.ThrustPIDScaleAxes = ThrustPIDScaleAxesField()
        self.addField(self.ThrustPIDScaleAxes)

        # Read field data
        self.read()
        self.metadata.read()
