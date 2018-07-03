# coding=utf-8
import GUI
import Math
import BigWorld
import game
import types
import Keys
import os
import ResMgr
import time
import math
from VehicleGunRotator import VehicleGunRotator
import AvatarInputHandler
import inspect
from gambiter.utils import *
from AvatarInputHandler.AimingSystems.ArcadeAimingSystem import ArcadeAimingSystem
from AvatarInputHandler.AimingSystems.SniperAimingSystem import SniperAimingSystem
from AvatarInputHandler.AimingSystems.StrategicAimingSystem import StrategicAimingSystem
from AvatarInputHandler.commands.siege_mode_control import SiegeModeControl
import gui.Scaleform.daapi.view.battle.shared.crosshair.plugins as plug
from gui.Scaleform.Flash import Flash
from gui.Scaleform import SCALEFORM_SWF_PATH_V3
from gui.Scaleform.daapi.view.meta.CrosshairPanelContainerMeta import CrosshairPanelContainerMeta
from Avatar import PlayerAvatar
from Vehicle import Vehicle
from gui import InputHandler
from gui.app_loader import g_appLoader
from gui.Scaleform.framework import ViewTypes

isNotEvent = False

WoTpath = os.getcwd()
WoTroot = os.getcwd()
pathxml = ResMgr.openSection('../paths.xml/Paths')
xPaths = filter(os.path.isdir, pathxml.readWideStrings('Path'))
WoTmod = xPaths[0]
res_modPath = WoTroot + WoTmod

# dictionary to easily convert keys from config to keycodes
keyDict = {"MODIFIER_SHIFT": 1, "MODIFIER_CTRL": 2, "MODIFIER_ALT": 4, "KEY_NOT_FOUND": 0, "KEY_NONE": 0, "KEY_NULL": 0, "KEY_ESCAPE": 1, "KEY_1": 2, "KEY_2": 3, "KEY_3": 4, "KEY_4": 5, "KEY_5": 6, "KEY_6": 7, "KEY_7": 8, "KEY_8": 9, "KEY_9": 10, "KEY_0": 11, "KEY_MINUS": 12, "KEY_EQUALS": 13, "KEY_BACKSPACE": 14, "KEY_TAB": 15, "KEY_Q": 16, "KEY_W": 17, "KEY_E": 18, "KEY_R": 19, "KEY_T": 20, "KEY_Y": 21, "KEY_U": 22, "KEY_I": 23, "KEY_O": 24, "KEY_P": 25, "KEY_LBRACKET": 26, "KEY_RBRACKET": 27, "KEY_RETURN": 28, "KEY_LCONTROL": 29, "KEY_A": 30, "KEY_S": 31, "KEY_D": 32, "KEY_F": 33, "KEY_G": 34, "KEY_H": 35, "KEY_J": 36, "KEY_K": 37, "KEY_L": 38, "KEY_SEMICOLON": 39, "KEY_APOSTROPHE": 40, "KEY_GRAVE": 41, "KEY_LSHIFT": 42, "KEY_BACKSLASH": 43, "KEY_Z": 44, "KEY_X": 45, "KEY_C": 46, "KEY_V": 47, "KEY_B": 48, "KEY_N": 49, "KEY_M": 50, "KEY_COMMA": 51, "KEY_PERIOD": 52, "KEY_SLASH": 53, "KEY_RSHIFT": 54, "KEY_NUMPADSTAR": 55, "KEY_LALT": 56, "KEY_SPACE": 57, "KEY_CAPSLOCK": 58, "KEY_F1": 59, "KEY_F2": 60, "KEY_F3": 61, "KEY_F4": 62, "KEY_F5": 63, "KEY_F6": 64, "KEY_F7": 65, "KEY_F8": 66, "KEY_F9": 67, "KEY_F10": 68, "KEY_NUMLOCK": 69, "KEY_SCROLL": 70, "KEY_NUMPAD7": 71, "KEY_NUMPAD8": 72, "KEY_NUMPAD9": 73, "KEY_NUMPADMINUS": 74, "KEY_NUMPAD4": 75, "KEY_NUMPAD5": 76, "KEY_NUMPAD6": 77, "KEY_ADD": 78, "KEY_NUMPAD1": 79, "KEY_NUMPAD2": 80, "KEY_NUMPAD3": 81, "KEY_NUMPAD0": 82, "KEY_NUMPADPERIOD": 83, "KEY_OEM_102": 86, "KEY_F11": 87, "KEY_F12": 88, "KEY_F13": 100, "KEY_F14": 101, "KEY_F15": 102, "KEY_KANA": 112, "KEY_ABNT_C1": 115, "KEY_CONVERT": 121, "KEY_NOCONVERT": 123, "KEY_YEN": 125, "KEY_ABNT_C2": 126, "KEY_NUMPADEQUALS": 141, "KEY_PREVTRACK": 144, "KEY_AT": 145, "KEY_COLON": 146, "KEY_UNDERLINE": 147, "KEY_KANJI": 148, "KEY_STOP": 149, "KEY_AX": 150, "KEY_UNLABELED": 151, "KEY_NEXTTRACK": 153, "KEY_NUMPADENTER": 156, "KEY_RCONTROL": 157, "KEY_MUTE": 160, "KEY_CALCULATOR": 161, "KEY_PLAYPAUSE": 162, "KEY_MEDIASTOP": 164, "KEY_VOLUMEDOWN": 174, "KEY_VOLUMEUP": 176, "KEY_WEBHOME": 178, "KEY_NUMPADCOMMA": 179, "KEY_NUMPADSLASH": 181, "KEY_SYSRQ": 183, "KEY_RALT": 184, "KEY_PAUSE": 197, "KEY_HOME": 199, "KEY_UPARROW": 200, "KEY_PGUP": 201, "KEY_LEFTARROW": 203, "KEY_RIGHTARROW": 205, "KEY_END": 207, "KEY_DOWNARROW": 208, "KEY_PGDN": 209, "KEY_INSERT": 210, "KEY_DELETE": 211, "KEY_LWIN": 219, "KEY_RWIN": 220, "KEY_APPS": 221, "KEY_POWER": 222, "KEY_SLEEP": 223, "KEY_WAKE": 227, "KEY_WEBSEARCH": 229, "KEY_WEBFAVORITES": 230, "KEY_WEBREFRESH": 231, "KEY_WEBSTOP": 232, "KEY_WEBFORWARD": 233, "KEY_WEBBACK": 234, "KEY_MYCOMPUTER": 235, "KEY_MAIL": 236, "KEY_MEDIASELECT": 237, "KEY_IME_CHAR": 255, "KEY_MOUSE0": 256, "KEY_LEFTMOUSE": 256, "KEY_MOUSE1": 257, "KEY_RIGHTMOUSE": 257, "KEY_MOUSE2": 258, "KEY_MIDDLEMOUSE": 258, "KEY_MOUSE3": 259, "KEY_MOUSE4": 260, "KEY_MOUSE5": 261, "KEY_MOUSE6": 262, "KEY_MOUSE7": 263, "KEY_JOY0": 272, "KEY_JOY1": 273, "KEY_JOY2": 274, "KEY_JOY3": 275, "KEY_JOY4": 276, "KEY_JOY5": 277, "KEY_JOY6": 278, "KEY_JOY7": 279, "KEY_JOY8": 280, "KEY_JOY9": 281, "KEY_JOY10": 282, "KEY_JOY11": 283, "KEY_JOY12": 284, "KEY_JOY13": 285, "KEY_JOY14": 286, "KEY_JOY15": 287, "KEY_JOY16": 288, "KEY_JOY17": 289, "KEY_JOY18": 290, "KEY_JOY19": 291, "KEY_JOY20": 292, "KEY_JOY21": 293, "KEY_JOY22": 294, "KEY_JOY23": 295, "KEY_JOY24": 296, "KEY_JOY25": 297, "KEY_JOY26": 298, "KEY_JOY27": 299, "KEY_JOY28": 300, "KEY_JOY29": 301, "KEY_JOY30": 302, "KEY_JOY31": 303, "KEY_JOYDUP": 272, "KEY_JOYDDOWN": 273, "KEY_JOYDLEFT": 274, "KEY_JOYDRIGHT": 275, "KEY_JOYSTART": 276, "KEY_JOYSELECT": 277, "KEY_JOYBACK": 277, "KEY_JOYALPUSH": 278, "KEY_JOYARPUSH": 279, "KEY_JOYCROSS": 280, "KEY_JOYA": 280, "KEY_JOYCIRCLE": 281, "KEY_JOYB": 281, "KEY_JOYSQUARE": 282, "KEY_JOYX": 282, "KEY_JOYTRIANGLE": 283, "KEY_JOYY": 283, "KEY_JOYL1": 284, "KEY_JOYBLACK": 284, "KEY_JOYR1": 285, "KEY_JOYWHITE": 285, "KEY_JOYL2": 286, "KEY_JOYLTRIGGER": 286, "KEY_JOYR2": 287, "KEY_JOYRTRIGGER": 287, "KEY_JOYAHARD": 288, "KEY_JOYBHARD": 289, "KEY_JOYXHARD": 290, "KEY_JOYYHARD": 291, "KEY_JOYBLACKHARD": 292, "KEY_JOYWHITEHARD": 293, "KEY_JOYLTRIGGERHARD": 294, "KEY_JOYRTRIGGERHARD": 295, "KEY_JOYALUP": 304, "KEY_JOYALDOWN": 305, "KEY_JOYALLEFT": 306, "KEY_JOYALRIGHT": 307, "KEY_JOYARUP": 308, "KEY_JOYARDOWN": 309, "KEY_JOYARLEFT": 310, "KEY_JOYARRIGHT": 311, "KEY_DEBUG": 312, "KEY_LCDKB_LEFT": 320, "KEY_LCDKB_RIGHT": 321, "KEY_LCDKB_OK": 322, "KEY_LCDKB_CANCEL": 323, "KEY_LCDKB_UP": 324, "KEY_LCDKB_DOWN": 325, "KEY_LCDKB_MENU": 326, "AXIS_LX": 0, "AXIS_LY": 1, "AXIS_RX": 2, "AXIS_RY": 3}


class base:
    modify = '06.03.2018'
    version = 'MeltyElement: Beta v0.1'
    xmlpath = ""


class MeltyElement():
    def __init__(self):
        ####
        self.aimtime = True
        self.flighttime = True
        self.targetspeed = True
        self.targetspeedMPH = False
        self.targetspeedKMH = False
        self.targetspeedMPS = False
        self.KMH = 3.6
        self.targetreload = True
        self.showPiercingPower = True
        self.showAdvancedPiercingPower = True
        self.showPenValues = False
        self.showHitAngle = False
        self.useXRay = True
        self.useBBox = True
        self.scalar = 2.0
        self.removeBinocs = True
        self.degree2pix = 16.0
        self.arcadeReticle = 36.0  # 72.0
        self.sniperReticle = 36.0  # 72.0
        self.relativeMode = True
        self.relOffset = 0.5
        self.timeout = 3.0
        self.m2pix = 8.5  # m2pix = 8.2
        self.circle0 = 24.0
        self.circle1 = 48.0
        ###########
        self.aimMode = 'None'
        self.reloadTime = 0
        self.currentTank = 0
        self.targetTankID = 0
        self.autoTargetID = 0
        self.name = ""
        self.type = ""
        # 3.6 kmh, 2.23694 mph, 0 meters per sec
        self.speedmulti = 3.6
        self.curTarget = None
        self.elementdebug = False
        self.debugE = False
        self.argslist = []
        self.illuminateKey = 666
        self.illuminateModifier = 666
        self.illuminatedSight = True
        self.illuminatedSightTogglearcade = False
        self.illuminatedSightTogglesniper = False
        self.illumSightVars = {'illuminatedSightTogglearcade': False, 'illuminatedSightTogglesniper': False}
        self.illuminateColor = None

        fp = open(base.xmlpath + "/gui/flash/ElementCrosshairSettings.xml")
        s = fp.read()
        decodeXML = s.decode('utf-8-sig').encode().encode("utf-8")
        fp.close()
        dataSectionXML = ResMgr.DataSection()
        dataSectionXML.createSectionFromString(decodeXML)
        config = dataSectionXML['mmms']
        xmlRoot = config['config']
        common = xmlRoot['common']
        arcade = xmlRoot['arcade']
        sniper = xmlRoot['sniper']
        strategic = xmlRoot['strategic']
        if config is not None:
            try:
                print "[MeltyElement] gui/flash/MeltyMapModSetting.xml parsing"
                if common.has_key('illuminatedSight'):
                    self.illuminatedSight = common.readBool('illuminatedSight')
                if common.has_key('illuminateKey'):
                    self.illuminateKey = keyDict[common.readString('illuminateKey')]
                if common.has_key('illuminateModifier'):
                    self.illuminateModifier = keyDict[common.readString('illuminateModifier')]
                if common.has_key('illuminateColor'):
                    self.illuminateColor = common.readVector3('illuminateColor')
                if common.has_key('aimtime'):
                    self.aimtime = common.readBool('aimtime')
                # print "[MeltyElement] MeltyElement.aimtime", MeltyElement.aimtime
                if common.has_key('flighttime'):
                    self.flighttime = common.readBool('flighttime')
                # print "[MeltyElement] MeltyElement.flighttime", MeltyElement.flighttime, common.readBool('flighttime')
                if common.has_key('targetspeed'):
                    self.targetspeed = common.readBool('targetspeed')
                # print "[MeltyElement] MeltyElement.targetspeed", MeltyElement.targetspeed, common.readBool('targetspeed')
                if common.has_key('targetspeedKMH'):
                    self.targetspeedKMH = common.readBool('targetspeedKMH')
                # print "[MeltyElement] MeltyElement.targetspeedKMH", MeltyElement.targetspeedKMH, common.readBool('targetspeedKMH')
                if common.has_key('targetspeedMPH'):
                    self.targetspeedMPH = common.readBool('targetspeedMPH')
                # print "[MeltyElement] MeltyElement.targetspeedMPH", MeltyElement.targetspeedMPH, common.readBool('targetspeedMPH')
                if common.has_key('targetspeedMPS'):
                    self.targetspeedMPS = common.readBool('targetspeedMPS')
                # print "[MeltyElement] MeltyElement.targetspeedMPS", MeltyElement.targetspeedMPS, common.readBool('targetspeedMPS')
                if common.has_key('targetreload'):
                    self.targetreload = common.readBool('targetreload')
                if common.has_key('showPiercingPower'):
                    self.showPiercingPower = common.readBool('showPiercingPower')
                # print "[MeltyElement] MeltyElement.showPiercingPower", MeltyElement.showPiercingPower, common.readBool('showPiercingPower')
                if common.has_key('showAdvancedPiercingPower'):
                    self.showAdvancedPiercingPower = common.readBool('showAdvancedPiercingPower')
                # print "[MeltyElement] MeltyElement.showAdvancedPiercingPower", MeltyElement.showAdvancedPiercingPower, common.readBool('showAdvancedPiercingPower')
                if common.has_key('showPenValues'):
                    self.showPenValues = common.readBool('showPenValues')
                # print "[MeltyElement] MeltyElement.showPenValues", MeltyElement.showPenValues, common.readBool('showPenValues')
                if common.has_key('showHitAngle'):
                    self.showHitAngle = common.readBool('showHitAngle')
                # print "[MeltyElement] MeltyElement.showHitAngle", MeltyElement.showHitAngle, common.readBool('showHitAngle')
                if common.has_key('useXRay'):
                    self.useXRay = common.readBool('useXRay')
                # print "[MeltyElement] MeltyElement.useXRay", MeltyElement.useXRay, common.readBool('useXRay')
                if common.has_key('useBBox'):
                    self.useBBox = common.readBool('useBBox')
                # print "[MeltyElement] MeltyElement.useBBox", MeltyElement.useBBox, common.readBool('useBBox')
                if common.has_key('scalar'):
                    self.scalar = common.readFloat('scalar')
                # print "[MeltyElement] MeltyElement.scalar", MeltyElement.scalar, common.readFloat('scalar')
                if common.has_key('debug'):
                    self.debugE = common.readBool('debug')
                # print "[MeltyElement] MeltyElement.debugE", MeltyElement.debugE, common.readBool('debug')
                if arcade.has_key('reticle'):
                    self.arcadeReticle = arcade.readFloat('reticle')
                # print "[MeltyElement] MeltyElement.arcadeReticle", MeltyElement.arcadeReticle, arcade.readFloat('reticle')
                if arcade.has_key('degree2pix'):
                    self.degree2pix = arcade.readFloat('degree2pix')
                # print "[MeltyElement] MeltyElement.degree2pix", MeltyElement.degree2pix, arcade.readFloat('degree2pix')
                if sniper.has_key('reticle'):
                    self.sniperReticle = sniper.readFloat('reticle')
                # print "[MeltyElement] MeltyElement.sniperReticle", MeltyElement.sniperReticle, sniper.readFloat('reticle')
                if sniper.has_key('removeBinocs'):
                    self.removeBinocs = sniper.readBool('removeBinocs')
                # print "[MeltyElement] MeltyElement.removeBinocs", MeltyElement.removeBinocs, sniper.readBool('removeBinocs')
                if strategic.has_key('relativeMode'):  # relOffset
                    self.relativeMode = strategic.readBool('relativeMode')
                # print "[MeltyElement] MeltyElement.relativeMode", MeltyElement.relativeMode, strategic.readBool('relativeMode')
                if strategic.has_key('relOffset'):  # relOffset
                    self.relOffset = strategic.readFloat('relOffset')
                # print "[MeltyElement] MeltyElement.relativeMode", MeltyElement.relOffset, strategic.readFloat('relOffset')
                if strategic.has_key('timeout'):
                    self.timeout = strategic.readFloat('timeout')
                # print "[MeltyElement] MeltyElement.timeout", MeltyElement.timeout, strategic.readFloat('timeout')
                if strategic.has_key('m2pix'):
                    self.m2pix = strategic.readFloat('m2pix')
                # print "[MeltyElement] MeltyElement.m2pix", self.m2pix, strategic.readFloat('m2pix')
                if strategic.has_key('circle'):
                    self.circle0 = strategic.readFloat('circle')
                # print "[MeltyElement] MeltyElement.circle0", MeltyElement.circle0, strategic.readFloat('m2pix')
                if strategic.has_key('circle'):
                    self.circle1 = strategic.readFloat('circle')  # print "[MeltyElement] MeltyElement.circle1", MeltyElement.circle1, strategic.readFloat('circle')
            except:
                print "[MeltyElement] config found but error occurred. Check values and file is encoded UTF-8 NO BOM "
        else:
            print res_modPath, "[MeltyElement] config not found"


def check():
    import ResMgr
    import os
    res = ResMgr.openSection('../paths.xml')
    sb = res['Paths']
    conp = None
    for folder in sb.values():
        filename = os.getcwd() + folder.asString + '/gui/flash/ElementCrosshairSettings.xml'
        print "filename", filename
        if os.path.exists(filename):
            conp = filename
            base.xmlpath = os.getcwd() + folder.asString
            break
    if conp is not None:
        print "--------------------------------------------------------------------------------------"
        print "[MeltyElement]: Loading Element Crosshairs Mod " + time.strftime("%H:%M:%S")
        print base.version + ' Built' + str(base.modify)
        print "--------------------------------------------------------------------------------------"
    else:
        print "--------------------------------------------------------------------------------------"
        print "[MeltyElement]: Loading Element Crosshairs Mod " + time.strftime("%H:%M:%S")
        print base.version + ' Built' + str(base.modify)
        print '[MeltyElement]: MeltyElementCrosshairs Settings: ElementCrosshairSettings.xml not found!'
        print "--------------------------------------------------------------------------------------"
    return


def getPlayerAimingInfo():
    """
    PlayerVehicleTypeDescriptor parameters:
    * staticDispersionAngle - constant dispersion of full aimed not damaged gun (passport gun dispersion).
    PlayerAvatarAimingInfo parameters:
    * aimingStartTime - time when aiming was started, since this moment player stopped bothering his vehicle.
    * aimingStartFactor - dispersion factor at time when aiming was started.
    * dispersionFactor - gun dispersion angle factor (depends on gun condition).
    * dispersionFactorTurretRotation - <NotImplemented> (used by WG scripts to calculate other aiming parameters on client side).
    * dispersionFactorChassisMovement - <NotImplemented> (used by WG scripts to calculate other aiming parameters on client side).
    * dispersionFactorChassisRotation - <NotImplemented> (used by WG scripts to calculate other aiming parameters on client side).
    * expAimingTime - aiming exp time (<aimingFactor> decreases exp times every <expAimingTime> seconds).
    """
    aimingInfo = getattr(BigWorld.player(), '_PlayerAvatar__aimingInfo', None)
    if aimingInfo is None or aimingInfo[0] == 0.0:
        return None
    aimingStartTime, aimingStartFactor, dispersionFactor, dispersionFactorTurretRotation, dispersionFactorChassisMovement, dispersionFactorChassisRotation, expAimingTime = aimingInfo
    staticDispersionAngle = BigWorld.player().vehicleTypeDescriptor.gun.shotDispersionAngle
    return staticDispersionAngle, aimingStartTime, aimingStartFactor, dispersionFactor, expAimingTime


def getAimingFactor(aimingStartTime, aimingStartFactor, dispersionFactor, expAimingTime, aimingThreshold=1.05):
    # Calculates current aiming factor.
    negElapsedTime = aimingStartTime - BigWorld.time()
    if aimingStartFactor / dispersionFactor >= aimingThreshold:
        return aimingStartFactor * math.exp(negElapsedTime / expAimingTime)
    return dispersionFactor


def getFullAimingTime(aimingStartFactor, dispersionFactor, expAimingTime):
    # Calculates time required for dispersion decreasing <aimingStartFactor>/<gunDispersionFactor> times.
    return expAimingTime * math.log(aimingStartFactor / dispersionFactor)


def getRemainingAimingTime(aimingStartTime, fullAimingTime):
    return max(0.0, aimingStartTime + fullAimingTime - BigWorld.time())


def getDispersionAngle(dispersionAngle, aimingFactor):
    return dispersionAngle * aimingFactor


def getDeviation(dispersionAngle, aimingDistance):
    return dispersionAngle * aimingDistance


def getShotAngles(vehicleTypeDescriptor, vehicleMP, targetPosition, adjust=True):
    hullPosition = vehicleTypeDescriptor.chassis.hullPosition
    turretPosition = vehicleTypeDescriptor.hull.turretPositions[0]
    gunPosition = vehicleTypeDescriptor.turret.gunPosition
    shotSpeed = vehicleTypeDescriptor.shot.speed
    shotGravity = vehicleTypeDescriptor.shot.gravity
    return BigWorld.wg_getShotAngles(hullPosition + turretPosition, gunPosition, vehicleMP, shotSpeed, shotGravity, 0, 0, targetPosition, adjust)


def getTurretMatrix(vehicleTypeDescriptor, vehicleMatrix, turretYaw):
    hullPosition = vehicleTypeDescriptor.chassis.hullPosition
    turretPosition = vehicleTypeDescriptor.hull.turretPositions[0]
    turretMatrix = Math.Matrix()
    turretMatrix.setRotateY(turretYaw)
    turretMatrix.translation = hullPosition + turretPosition
    turretMatrix.postMultiply(vehicleMatrix)
    return turretMatrix


def getGunMatrix(vehicleTypeDescriptor, turretMatrix, gunPitch):
    gunPosition = vehicleTypeDescriptor.turret.gunPosition
    gunMatrix = Math.Matrix()
    gunMatrix.setRotateX(gunPitch)
    gunMatrix.translation = gunPosition
    gunMatrix.postMultiply(turretMatrix)
    return gunMatrix


def getShotRayAndPoint(vehicleTypeDescriptor, vehicleMatrix, turretYaw, gunPitch):
    turretMatrix = getTurretMatrix(vehicleTypeDescriptor, vehicleMatrix, turretYaw)
    gunMatrix = getGunMatrix(vehicleTypeDescriptor, turretMatrix, gunPitch)
    return gunMatrix.applyToAxis(2), gunMatrix.applyToOrigin()


def getVehicleShotParams(vehicleTypeDescriptor, vehicleMatrix, turretYaw, gunPitch):
    shotSpeed = vehicleTypeDescriptor.shot.speed
    shotGravity = vehicleTypeDescriptor.shot.gravity
    shotMaxDistance = vehicleTypeDescriptor.shot.maxDistance
    shotRay, shotPoint = getShotRayAndPoint(vehicleTypeDescriptor, vehicleMatrix, turretYaw, gunPitch)
    shotVector = shotRay.scale(shotSpeed)
    shotGravity = Math.Vector3(0.0, -shotGravity, 0.0)
    return shotPoint, shotVector, shotGravity, shotMaxDistance


def getBallisticsInfo(vehicleTypeDescriptor, vehicleMP, targetPoint):
    turretYaw, gunPitch = getShotAngles(vehicleTypeDescriptor, vehicleMP, targetPoint)
    shotPoint, shotVector, shotGravity, shotMaxDistance = getVehicleShotParams(vehicleTypeDescriptor, Math.Matrix(vehicleMP), turretYaw, gunPitch)
    flyTime = targetPoint.flatDistTo(shotPoint) / shotVector.flatDistTo(Math.Vector3(0.0, 0.0, 0.0))
    return targetPoint.distTo(shotPoint), flyTime, shotVector.pitch, (shotVector + shotGravity * flyTime).pitch


def getPlayerBallisticsInfo():
    player = BigWorld.player()
    return getBallisticsInfo(player.vehicleTypeDescriptor, player.getOwnVehicleMatrix(), player.gunRotator.markerInfo[0])


# ------------------------ #
#    AimingInfo Classes    #
# ------------------------ #
class AimingInfo(object):
    __slots__ = ('__weakref__', 'aimingThreshold')

    def __init__(self, aimingThreshold=1.05):
        super(AimingInfo, self).__init__()
        self.aimingThreshold = aimingThreshold
        return

    def getMacroData(self):
        playerAimingInfo = getPlayerAimingInfo()
        if playerAimingInfo is not None:
            staticDispersionAngle, aimingStartTime, aimingStartFactor, dispersionFactor, expAimingTime = playerAimingInfo
            aimingFactor = getAimingFactor(aimingStartTime, aimingStartFactor, dispersionFactor, expAimingTime, aimingThreshold=self.aimingThreshold)
            fullAimingTime = getFullAimingTime(aimingStartFactor, dispersionFactor, expAimingTime)
            remainingAimingTime = getRemainingAimingTime(aimingStartTime, fullAimingTime)
            realDispersionAngle = getDispersionAngle(staticDispersionAngle, aimingFactor)
            aimingDistance, flyTime, shotAngleRad, hitAngleRad = getPlayerBallisticsInfo()
            deviation = getDeviation(realDispersionAngle, aimingDistance)
            shotAngleDeg = math.degrees(shotAngleRad)
            hitAngleDeg = math.degrees(hitAngleRad)
            return {'expAimingTime': expAimingTime, 'fullAimingTime': fullAimingTime, 'remainingAimingTime': remainingAimingTime, 'staticDispersionAngle': staticDispersionAngle, 'realDispersionAngle': realDispersionAngle, 'dispersionFactor': dispersionFactor, 'aimingDistance': aimingDistance, 'aimingFactor': aimingFactor, 'shotAngleRad': shotAngleRad, 'shotAngleDeg': shotAngleDeg, 'hitAngleRad': hitAngleRad, 'hitAngleDeg': hitAngleDeg, 'deviation': deviation, 'flyTime': flyTime}
        return None

    @staticmethod
    def enable():
        # nothing
        return

    @staticmethod
    def disable():
        # nothing
        return

    def __repr__(self):
        return '{!s}(aimingThreshold={!r})'.format(self.__class__.__name__, self.aimingThreshold)

    def __del__(self):
        return


def getSpeed(vehicle):
    if not isinstance(vehicle, (BigWorld.Entity, types.NoneType)):
        vehicle = BigWorld.entity(vehicle)
    return vehicle and vehicle.getSpeed()


def getGunInfo():
    vTypeDesc = BigWorld.player().vehicleTypeDescriptor
    gun_Name = vTypeDesc.gun.name
    shell_Speed = vTypeDesc.shot.speed
    shellGravity = vTypeDesc.shot.gravity
    shell_Name = vTypeDesc.shot.shell.name
    return gun_Name, shell_Speed, shellGravity, shell_Name  # ownVehicle = BigWorld.entity(BigWorld.player().playerVehicleID)  # shellSpeed = 500.0  # if ownVehicle is not None:  #     vTypeDesc = ownVehicle.typeDescriptor  #     if vTypeDesc is not None:  #         shellSpeed = BigWorld.player().vehicleTypeDescriptor.shot.speed  # return BigWorld.player().vehicleTypeDescriptor.shot.speed if BigWorld.player().vehicleTypeDescriptor.shot.speed is not None else 800


# def getTankData():
#     eDebug("getTankData")
#     ownVehicle = BigWorld.entity(BigWorld.player().playerVehicleID)
#     ownAvatar = BigWorld.player()
#     if ownVehicle is not None:
#         playerVehTypeDesc = ownAvatar.vehicleTypeDescriptor
#         vTypeDesc = ownVehicle.typeDescriptor
#         if vTypeDesc is not None:
#             hullArmor = [vTypeDesc.hull['primaryArmor'][0], vTypeDesc.hull['primaryArmor'][1], vTypeDesc.hull['primaryArmor'][2]]
#             gunName = vTypeDesc.gun['shortUserString']
#             shellSpeed = vTypeDesc.shot['speed']
#             shellGravity = vTypeDesc.shot['gravity']
#             shellName = vTypeDesc.shot['shell']['userString']
#             if vTypeDesc.shot['shell']['kind'] == 'ARMOR_PIERCING':
#                 shellType = vTypeDesc.shot['shell']['kind'].replace('ARMOR_PIERCING', 'AP')
#             elif vTypeDesc.shot['shell']['kind'] == 'HIGH_EXPLOSIVE':
#                 shellType = vTypeDesc.shot['shell']['kind'].replace('HIGH_EXPLOSIVE', 'HE')
#             elif vTypeDesc.shot['shell']['kind'] == 'ARMOR_PIERCING_CR':
#                 shellType = vTypeDesc.shot['shell']['kind'].replace('ARMOR_PIERCING_CR', 'CR')
#             else:
#                 shellType = vTypeDesc.shot['shell']['kind'].replace('HOLLOW_CHARGE', 'HC')
#             vehicleName = vTypeDesc.type.userString
#             shellPower = vTypeDesc.shot['piercingPower'][0]
#             shellDamage = vTypeDesc.shot['shell']['damage'][0]
#             try:
#                 shellSplash = vTypeDesc.shot['shell']['explosionRadius']
#             except:
#                 shellSplash = 0
#             dispersionAngle, aimingStartTime, aimingStartFactor, dispersionFactor, aimingTime = BallisticsMath.getPlayerAimingInfo()
#             aimingFactor = BallisticsMath.getAimingFactor(aimingStartTime, aimingStartFactor, dispersionFactor, aimingTime)
#             try:
#                 fullAimingTime = BallisticsMath.getFullAimingTime(aimingStartFactor, dispersionFactor, aimingTime)
#             except ValueError:
#                 fullAimingTime = 0
#             remainingAimingTime = BallisticsMath.getRemainingAimingTime(aimingStartTime, fullAimingTime)
#             realDispersionAngle = BallisticsMath.getDispersionAngle(dispersionAngle, aimingFactor)
#             try:
#                 aimingDistance, hitAngleRad, flyTime = BallisticsMath.getPlayerBallisticsInfo()
#             except:
#                 aimingDistance = 0
#                 flyTime = 9999
#             # deviation = BallisticsMath.getDeviation(aimingDistance, realDispersionAngle)
#             # aimingDistance, hitAngleRad, flyTime = BallisticsMath.getPlayerBallisticsInfo()
#             realDispersionAngle = '%.1f' % (realDispersionAngle * 100)
#             remainingAimingTime = '%.1f' % remainingAimingTime if MeltyElement.aimtime else 9999
#             flightTime = '%.1f' % flyTime if MeltyElement.flighttime else 9999
#             return (gunName, shellSpeed, shellGravity, shellName, shellSplash, vehicleName, shellType, shellPower, shellDamage, aimingDistance, flightTime, remainingAimingTime, realDispersionAngle)
#     return (None, None, None, None, None, None, None, None, None, None, None, None, None)

def new_update():
    # newDistance = saved_update(self)
    ownVehicle = BigWorld.entity(BigWorld.player().playerVehicleID)
    gunPitch = Math.Matrix(BigWorld.player().gunRotator.gunMatrix).pitch
    gunPitch = math.degrees(gunPitch)
    # ammoCtrl = g_sessionProvider.getAmmoCtrl()
    if ownVehicle is not None:
        elementAimInfo = AimingInfo.getMacroData(aimInfo)
        # {'expAimingTime': expAimingTime, 'fullAimingTime': fullAimingTime, 'remainingAimingTime': remainingAimingTime,
        #  'staticDispersionAngle': staticDispersionAngle, 'realDispersionAngle': realDispersionAngle,
        #  'dispersionFactor': dispersionFactor, 'aimingDistance': aimingDistance, 'aimingFactor': aimingFactor,
        #  'shotAngleRad': shotAngleRad, 'shotAngleDeg': shotAngleDeg, 'hitAngleRad': hitAngleRad, 'hitAngleDeg': hitAngleDeg,
        #  'deviation': deviation, 'flyTime': flyTime}
        aimingDistance = '%.0f' % elementAimInfo['aimingDistance']
        realDispersionAngle = '%.1f' % (elementAimInfo['realDispersionAngle'] * 100)
        remainingAimingTime = '%.1f' % elementAimInfo['remainingAimingTime'] if MeltyElement.aimtime else 9999
        flightTime = '%.1f' % elementAimInfo['flyTime'] if MeltyElement.flighttime else 9999
        # dispersionAngle, aimingStartTime, aimingStartFactor, dispersionFactor, aimingTime = BallisticsMath.getPlayerAimingInfo()
        # aimingFactor = BallisticsMath.getAimingFactor(aimingStartTime, aimingStartFactor, dispersionFactor, aimingTime)
        # try:
        #     fullAimingTime = BallisticsMath.getFullAimingTime(aimingStartFactor, dispersionFactor, aimingTime)
        # except ValueError:
        #     fullAimingTime = 0
        # remainingAimingTime = BallisticsMath.getRemainingAimingTime(aimingStartTime, fullAimingTime)
        # realDispersionAngle = BallisticsMath.getDispersionAngle(dispersionAngle, aimingFactor)
        # aimingDistance, hitAngleRad, flyTime = BallisticsMath.getPlayerBallisticsInfo()
        # realDispersionAngle = '%.1f' % (realDispersionAngle * 100)
        # remainingAimingTime = '%.1f' % remainingAimingTime if MeltyElement.aimtime else 9999
        # flightTime = '%.1f' % flyTime if MeltyElement.flighttime else 9999
        sniperBattleFlash.updateBallistics(aimingDistance, flightTime, remainingAimingTime, realDispersionAngle)  # self._flashCall('updateBallistics', [aimingDistance, flightTime, remainingAimingTime, realDispersionAngle])  # if BattleReplay.isPlaying() and MeltyElement.reloadTime != 0:  #     reloadTime = MeltyElement.reloadTime  #     percent = ammoCtrl.getGunReloadTime()  #     if percent != 100.0:  #         reloadTimer = abs(reloadTime * percent / 100.0 - reloadTime)  #     else:  #         reloadTimer = 0  #     self._flashCall('reloadTimer', [reloadTimer, gunPitch, reloadTime])  # else:  #     reloadingHndl = BigWorld.player().inputHandler.aim._reloadingHndl  #     if reloadingHndl.state['isReloading']:  #         reloadTimer = reloadingHndl.state['startTime'] + reloadingHndl.state['duration'] - BigWorld.time()  #     else:  #         reloadTimer = 0  #     self._flashCall('reloadTimer', [reloadTimer, gunPitch, MeltyElement.reloadTime])
    if BigWorld.target() is not None:
        # noinspection PyBroadException
        try:
            curTarget = BigWorld.target()
            curTargetSpeed = int(round(getSpeed(curTarget) * MeltyElement.speedmulti, 0))
        except:
            curTargetSpeed = 9999
        sniperBattleFlash.updateVehicleSpeed(curTargetSpeed)
        typeDescr = BigWorld.target().typeDescriptor
        # speed = [typeDescr.physics['speedLimits'][0], typeDescr.physics['speedLimits'][1]]
        # self._flashCall('updateVehicleSpeed', [curTargetSpeed])
        # self._flashCall('vehicleSpeed', [speed[0], speed[1]])
        # self._flashCall('setTargetSpeed', [speed[0], speed[1]])
        newDistance = int((BigWorld.target().position - BigWorld.player().getOwnVehiclePosition()).length)
        sniperBattleFlash.updateTarget(newDistance, BigWorld.entity(BigWorld.target().id).health)
        # reload = typeDescr.gun['reloadTime']
        # viewrange = typeDescr.turret['circularVisionRadius']
        # self._flashCall('setTargetParams', [reload, viewrange, newDistance])
        _gun = typeDescr.gun
        _miscAttrs = typeDescr.miscAttrs
        _turret = typeDescr.turret
        crewLevelIncrease = 0.0043 * _miscAttrs.get('crewLevelIncrease', 0)
        # targetVehicle = _type.shortUserString
        # targetName = entity.publicInfo.name
        targetReload = _gun.reloadTime * _miscAttrs.get('gunReloadTimeFactor', 1) / (1.0695 + crewLevelIncrease)
        targetReload = '%.1f' % targetReload
        targetVisionRadius = _turret.circularVisionRadius * _miscAttrs.get('circularVisionRadiusFactor', 1) / (1.0434 + crewLevelIncrease)
        sniperBattleFlash.setTargetParams(targetReload, targetVisionRadius, newDistance)
    else:
        curTargetSpeed = 9999
        sniperBattleFlash.updateVehicleSpeed(curTargetSpeed)  # sniperBattleFlash.clearTarget()
    aimMode = BigWorld.player().inputHandler.ctrlModeName
    if aimMode == 'arcade':
        sniperBattleFlash.component.visible = False
    if aimMode == 'sniper':
        sniperBattleFlash.component.visible = True
        # curCtrl = getattr(getattr(BigWorld.player(), 'inputHandler', None), 'ctrl', None)
        # if MeltyElement.removeBinocs:
        #     curCtrl._cam._SniperCamera__binoculars.enabled = False
        curZoom = BigWorld.player().inputHandler.ctrl.camera._SniperCamera__zoom
        # curzoom2 = int(curzoom)
        # self._flashCall('sniperZoom', [int(round(curzoom))])
        zoom2 = 1.047197580337524 / curZoom
        # self._flashCall('getZoomByMeltyMap', [zoom2])
        sniperBattleFlash.getZoom(zoom2)
    if aimMode == 'strategic':
        sniperBattleFlash.component.visible = False
        height = int(round(BigWorld.camera().position.y - AvatarInputHandler.control_modes.getFocalPoint()[1]))
        # self._flashCall('heightSight', [height])
        # self._flashCall('updateHeight', [height])
        # # self._flashCall('getZoomByMeltyMap', [height])
        sniperBattleFlash.getZoom(height)
        gunPitch = abs(math.degrees(Math.Matrix(BigWorld.player().gunRotator.gunMatrix).pitch))
        x, y, z = BigWorld.player().gunRotator.markerInfo[0]
        v = BigWorld.player().getOwnVehiclePosition() - Math.Vector3(x, y, z)  # self._flashCall('gunView', [gunPitch, v.length])  # if aimMode == 'arcade' or aimMode == 'sniper' or aimMode == 'strategic' or aimMode == 'postmortem':  # self._flashCall('markerDistance', [_getAimDistance()])  # self._flashCall('updateDistance', [_getAimDistance()])  # self._flashCall('updateDistanceMS', [_getAimDistance()])  # self._flashCall('aimingEnded', [BigWorld.player().complexSoundNotifications._ComplexSoundNotifications__isAimingEnded])  # return newDistance


# def getmems(obj):
#     print "\n ### " + str(obj) + " ###\n"
#     print "\n ### " + str(obj) + " ###\n"
#     i = 0
#     for property, value in inspect.getmembers(obj):
#         print "\tm" + str(i) + " ", property, ":  v ", value
#         i += 1


class SniperBattleFlash(Flash):
    def __init__(self):
        # Flash.__init__(self, 'SniperBattleFlash.swf')
        # # We should call parent __init__ first.
        # # If we want to use specific path, use path parameter, otherwise, skip it.
        # # In this example I will load flash from root directory (/res_bw, /res, /res_mods/<patch>).
        # # In my opinion, base Flash class (written by WG) was made by Indians for food. Paths sum did incorrect at least.
        # super(SniperBattleFlash, self).__init__('SniperBattleFlash.swf', path=SCALEFORM_SWF_PATH_V3)
        # Flash.__init__(self, 'SniperBattleFlash.swf')
        super(SniperBattleFlash, self).__init__('SniperBattleFlash.swf', path=SCALEFORM_SWF_PATH_V3)
        self.maxHP = 0.0

        # Here component is a BigWorld GUI container, and movie is a Scaleform movie object.

        # We don't want to see a background, we make it transparent.
        self.movie.backgroundAlpha = 0.0

        # WG undocumented parameter. Use it on your own risk.
        self.component.wg_inputKeyMode = 2

        # See BigWorld documentation for details.
        self.component.focus = False

        # See BigWorld documentation for details.
        self.component.heightMode = 'PIXEL'
        self.component.widthMode = 'PIXEL'

        # Setting size of our flash document.
        # See BigWorld documentation for details.
        self.component.size = (800, 800)
        self.component.size = GUI.screenResolution()

        self.component.visible = True

        # getmems(self.component.movie)

        # This method inits logging, and do some other things.
        self.afterCreate()

        return

    def populate(self):
        #   Getting access to our flash object
        #   By getting a _level0 we can access to first frame functions, but it is useless to set a flash script
        #       property - ActionScript 2.0 document have no document class. So we use an object instead. See basic
        #       info for details.
        self.__flashObject = self.getMember('_root._level0.g_modeMC')

        #   Setting a Python instance overloading ActionScript placeholders.
        #   Methods of this instance will overload ActionScript element (base class instance) methods (dummies).
        #   You can use any instance (object) here, that provides required DAAPI methods for overload.
        # self.__flashObject.script = self

        #   Populating a BigWorld GUI container.
        GUI.addRoot(self.component)

        return

    @property
    def flashObject(self):
        #   This property provides access to our flash object from outside. However, it is a private object.
        #   It's not good if code outside this class access this object directly. It would better to use wrapper methods.
        return self.__flashObject

    def destroy(self):
        #   This method should be called before you delete this class instance. Manually. Otherwise, it will cause
        #       an error. It contrasts populate method.
        #   Removing container from visible objects.
        GUI.delRoot(self.component)

        #   Resetting flash object script.
        self.__flashObject.script = None

        #   Finally, releasing flash object.
        self.__flashObject = None

        return

    def __del__(self):
        #   This method is called when object is actually deleted. See Python docs for details.
        #   Unloading logging and other things (see __init__).
        self.beforeDelete()

        #   Finally call a parent class method.
        super(SniperBattleFlash, self).__del__()

        return

    @staticmethod
    def py_daapiMethod(number, string, array):
        #   This DAAPI method will be used as an overload for ActionScript dummy with the same name.
        #   We can return something or nothing
        #   For example I will return a sum like
        import debug_utils
        debug_utils.LOG_WARNING("py_daapiMethod was called.")
        return number + len(string) + len(array)

    def as_daapiMethod_wrapper(self, number, string, array):
        #   This method is not strictly required, it may be used to wrap flashObject calls for external caller.
        return self.__flashObject.as_daapiMethod(number, string, array)

    def setOnLoad(self, var):
        print "onload"
        self.call("SniperBattleFlash.onLoad", [var])

    def getAimDist(self):
        elementAimInfo = AimingInfo.getMacroData(aimInfo)
        aimingDistance = '%.0f' % elementAimInfo['aimingDistance']
        self.call("SniperBattleFlash.updateTarget", [aimingDistance])

    def setReloading(self, duration, startTime, isReloading, correction):
        self.call("SniperBattleFlash.setReloading", [duration, startTime, isReloading, correction])

    # noinspection PyUnusedLocal
    def setReloadingAsPercent(self, percent, isReloading):
        self.call("SniperBattleFlash.setReloadingAsPercent", [percent])

    def setHealth(self, percent):
        curHP = self.maxHP * percent
        # print "MaxHP: ", self.maxHP, " curHP:", curHP, "percent:", percent
        self.call("SniperBattleFlash.setHealth", [percent, curHP, self.maxHP])

    def setAmmoStock(self, quantity, quantityInClip, isLow, state, clipReloaded):
        self.call("SniperBattleFlash.setAmmoStock", [quantity, quantityInClip, isLow, state, clipReloaded])

    # noinspection PyUnusedLocal
    def setClipParams(self, clipCapacity, burst, isAutoloader):
        self.call("SniperBattleFlash.setClipParams", [clipCapacity, burst])

    def setTarget(self, isFriend):
        if isFriend:
            isEnemy = 0
        else:
            isEnemy = 1
        self.call("SniperBattleFlash.setTarget", [isEnemy])

    def setTargetParams(self, TargetReload, TargetViewRange, newDist):
        self.call("SniperBattleFlash.setTargetParams", [TargetReload, TargetViewRange, newDist])

    def updateVehicleSpeed(self, curTargetSpeed):
        self.call("SniperBattleFlash.updateVehicleSpeed", [curTargetSpeed])

    def updateTarget(self, newDistance, health):
        self.call("SniperBattleFlash.updateTarget", [newDistance, health])

    def setCenterType(self, centerAlpha, centerType):
        # print "setCenterType:", centerType
        self.call("SniperBattleFlash.setCenterType", [centerAlpha, centerType])

    def setNetType(self, netAlpha, netType):
        # print "setNetType:", netType
        self.call("SniperBattleFlash.setNetType", [netAlpha, netType])

    def setReloaderType(self, reloadAlpha, reloadType):
        self.call("SniperBattleFlash.setReloaderType", [reloadAlpha, reloadType])

    def setConditionType(self, conditionAlpha, conditionType):
        self.call("SniperBattleFlash.setConditionType", [conditionAlpha, conditionType])

    def setCassetteType(self, cassetteAlpha, cassetteType):
        self.call("SniperBattleFlash.setCassetteType", [cassetteAlpha, cassetteType])

    def setGunParams(self, gun_Name, shell_Speed, shellGravity, shell_Name):
        self.call("SniperBattleFlash.setGunParams", [gun_Name, shell_Speed, shellGravity, shell_Name])

    def updateBallistics(self, aimingDistance, flightTime, remainingAimingTime, realDispersionAngle):
        self.call("SniperBattleFlash.updateBallistics", [aimingDistance, flightTime, remainingAimingTime, realDispersionAngle])

    def getZoom(self, zoom2):
        self.call("SniperBattleFlash.getZoomByMeltyMap", [zoom2])

    def onRecreateDevice(self, offsetX, offsetY):
        width, height = GUI.screenResolution()
        self.call("SniperBattleFlash.onRecreateDevice", [width, height, offsetX, offsetY])

    def clearTarget(self):
        startTime = BigWorld.serverTime()
        self.call("SniperBattleFlash.clearTarget", [startTime])

    def toggleIlluminateSight(self, illuminatedToggle, illuminateColor0, illuminateColor1, illuminateColor2):
        self.call("SniperBattleFlash.toggleIlluminateSight", [illuminatedToggle, illuminateColor0, illuminateColor1, illuminateColor2])


offsetXArcade = 960
offsetYSniper = 540
offsetYArcade = 458
aimInfo = AimingInfo()
sniperBattleFlash = SniperBattleFlash()


def isAlive(vehicle):
    if not isinstance(vehicle, (BigWorld.Entity, types.NoneType)):
        vehicle = BigWorld.entity(vehicle)
    return vehicle and vehicle.isAlive()


def inject_handle_key_event_sniper(event):
    is_down, key, mods, is_repeat = game.convertKeyEvent(event)
    if hasattr(BigWorld.player(), 'isOnArena') and BigWorld.player().isOnArena and isAlive(BigWorld.player().playerVehicleID) and BigWorld.player().inputHandler.ctrlModeName == 'sniper':
        try:
            if MeltyElement.illuminatedSight:
                # currAim = BigWorld.player().inputHandler.ctrl.getAim()
                aimMode = BigWorld.player().inputHandler.ctrlModeName
                currSight = MeltyElement.illumSightVars['illuminatedSightToggle%s' % aimMode]
                if BigWorld.isKeyDown(MeltyElement.illuminateKey) and is_down and mods == MeltyElement.illuminateModifier:
                    # AppLoader.getBattleApp().call('battle.' + panel + '.ShowMessage', [key, msgText, color])
                    if currSight:
                        snipermsg = 'Illuminated %s Sight Disabled' % aimMode
                        MeltyElement.illumSightVars['illuminatedSightToggle%s' % aimMode] = False
                        ctrl = g_appLoader.getDefBattleApp()
                        if ctrl is not None:
                            battle_page = ctrl.containerManager.getContainer(ViewTypes.VIEW).getView()
                            battle_page.components['battlePlayerMessages'].as_showRedMessageS(None, snipermsg)
                        # g_appLoader.getDefBattleApp().call('battle.PlayerMessagesPanel.ShowMessage', ['%s illuminateSightOn' % aimMode, 'Illuminated %s Sight Disabled' % aimMode, 'red'])
                    else:
                        snipermsg = 'Illuminated %s Sight Enabled' % aimMode
                        MeltyElement.illumSightVars['illuminatedSightToggle%s' % aimMode] = True
                        # g_appLoader.getDefBattleApp().call('battle.PlayerMessagesPanel.ShowMessage', ['%s illuminateSightOff' % aimMode, 'Illuminated %s Sight Enabled' % aimMode, 'green'])
                        ctrl = g_appLoader.getDefBattleApp()
                        if ctrl is not None:
                            battle_page = ctrl.containerManager.getContainer(ViewTypes.VIEW).getView()
                            battle_page.components['battlePlayerMessages'].as_showGreenMessageS(None, snipermsg)
                    illuminatedToggle = MeltyElement.illumSightVars['illuminatedSightToggle%s' % aimMode]
                    sniperBattleFlash.toggleIlluminateSight(illuminatedToggle, MeltyElement.illuminateColor[0], MeltyElement.illuminateColor[1], MeltyElement.illuminateColor[2])
                    # currAim._flashCall('toggleIlluminateSight', [illuminatedToggle, MeltyElement.illuminateColor[0], MeltyElement.illuminateColor[1], MeltyElement.illuminateColor[2]])
            if BigWorld.player().isOnArena is None and BigWorld.player().inputHandler.ctrlModeName != 'postmortem':
                if BigWorld.isKeyDown(Keys.KEY_F1) and is_down and mods == MeltyElement.illuminateModifier:
                    print "trying to reload cfg"
                    check()
        except Exception as e:
            print('%s inject_handle_key_event' % base.version, e)


# noinspection PyUnusedLocal
@registerEvent(Vehicle, 'onLeaveWorld')
def ME_AP_Vehicle_onLeaveWorld(self):
    global sniperBattleFlash
    if self.isPlayerVehicle:
        sniperBattleFlash.destroy()
        sniperBattleFlash = None
        InputHandler.g_instance.onKeyDown -= inject_handle_key_event_sniper
        InputHandler.g_instance.onKeyUp -= inject_handle_key_event_sniper


# noinspection PyUnusedLocal
@registerEvent(Vehicle, 'onEnterWorld')
def ME_AP_Vehicle_onEnterWorld(self, prereqs):
    global isNotEvent, sniperBattleFlash
    if self.isPlayerVehicle:
        isNotEvent = True
        if sniperBattleFlash is None:
            sniperBattleFlash = SniperBattleFlash()
        sniperBattleFlash.populate()
        #   Doing something...
        #   Changing properties.
        sniperBattleFlash.flashObject._x = offsetXArcade
        sniperBattleFlash.flashObject._y = offsetYArcade
        sniperBattleFlash.setOnLoad(1)
        # eDebug("Vehicle.onEnterWorld: " + datetime.datetime.now().strftime("%H:%M:%S.%f"))
        td = self.typeDescriptor
        sniperBattleFlash.maxHP = float(td.maxHealth)
        sniperBattleFlash.cameraMode = 'arcade'
        sniperBattleFlash.siegeMode = False
        InputHandler.g_instance.onKeyDown += inject_handle_key_event_sniper
        InputHandler.g_instance.onKeyUp += inject_handle_key_event_sniper


@overrideMethod(CrosshairPanelContainerMeta, 'as_recreateDeviceS')
def CrosshairPanelContainerMeta_as_recreateDeviceS(base, self, offsetX, offsetY):
    # print "offsetX:", offsetX, "offsetY: ", offsetY
    gun_Name, shell_Speed, shellGravity, shell_Name = getGunInfo()
    sniperBattleFlash.setGunParams(gun_Name, shell_Speed, shellGravity, shell_Name)
    # gunName, shellSpeed, shellGravity, shellName, shellSplash, vehicleName, shellType, shellPower, shellDamage, aimingDistance, flightTime, remainingAimingTime, realDispersionAngle = getTankData()
    # sendDataToFlash(self, gunName, shellSpeed, shellGravity, shellName, shellSplash, vehicleName, shellType, shellPower, shellDamage, aimingDistance, flightTime, remainingAimingTime, realDispersionAngle)
    sniperBattleFlash.flashObject._x = offsetX  # (1920 * 0.5) * (1 + offsetX)
    sniperBattleFlash.flashObject._y = offsetY  # (0.5 * 1080) * (1 - offsetY)
    # sniperBattleFlash.onRecreateDevice(offsetX, offsetY)
    return base(self, offsetX, offsetY)


# noinspection PyUnusedLocal
@registerEvent(VehicleGunRotator, '_VehicleGunRotator__getShotPosition')
def elementCross_getShotPosition(self, turretYaw, gunPitch):
    sniperBattleFlash.getAimDist()
    new_update()


# noinspection PyUnusedLocal
@registerEvent(CrosshairPanelContainerMeta, 'as_setReloadingS')
def CrosshairPanelContainerMeta_as_setReloadingS(self, duration, baseTime, startTime, isReloading):
    sniperBattleFlash.setReloading(duration, startTime, isReloading, 0)
    gun_Name, shell_Speed, shellGravity, shell_Name = getGunInfo()
    sniperBattleFlash.setGunParams(gun_Name, shell_Speed, shellGravity, shell_Name)


# noinspection PyUnusedLocal
@registerEvent(CrosshairPanelContainerMeta, 'as_setReloadingAsPercentS')
def CrosshairPanelContainerMeta_as_setReloadingAsPercent(self, percent, isReloading):
    sniperBattleFlash.setReloadingAsPercent(percent, isReloading)


# noinspection PyUnusedLocal
@registerEvent(CrosshairPanelContainerMeta, 'as_setHealthS')
def CrosshairPanelContainerMeta_as_setHealthS(self, percent):
    # print "CrosshairPanelContainerMeta_as_setHealthS perc:", percent
    sniperBattleFlash.setHealth(percent)


@registerEvent(Vehicle, 'onHealthChanged')
def ElementCrosshaironHealthChanged(self, newHealth, attackerID, attackReasonID):
    if self.isPlayerVehicle:
        newPercent = float(newHealth) / float(sniperBattleFlash.maxHP)
        # print "onHealthChanged", newHealth, "perc:", newPercent
        sniperBattleFlash.setHealth(newPercent)


# noinspection PyUnusedLocal
@registerEvent(CrosshairPanelContainerMeta, 'as_setAmmoStockS')
def CrosshairPanelContainerMeta_as_setAmmoStockS(self, quantity, quantityInClip, isLow, clipState, clipReloaded=False):
    sniperBattleFlash.setAmmoStock(quantity, quantityInClip, isLow, clipState, clipReloaded)


# noinspection PyUnusedLocal
@registerEvent(CrosshairPanelContainerMeta, 'as_setClipParamsS')
def CrosshairPanelContainerMeta_as_setClipParamsS(self, clipCapacity, burst, isAutoloader=False):
    sniperBattleFlash.setClipParams(clipCapacity, burst, isAutoloader)


@registerEvent(PlayerAvatar, 'targetBlur')
def PlayerAvatar_targetBlur(self, prevEntity):
    global f_delayHideTarget
    # if config.get('sight/enabled', True):
    if prevEntity in self._PlayerAvatar__vehicles:
        sniperBattleFlash.clearTarget()


# noinspection PyBroadException
@registerEvent(PlayerAvatar, 'targetFocus')
def PlayerAvatar_targetFocus(self, entity):
    # global targetName, targetVehicle, targetVType, targetColorsVType, targetReload, targetVisionRadius, targetDistance
    if entity in self._PlayerAvatar__vehicles:
        if entity.publicInfo['team'] == 0:
            isFriend = True
        else:
            isFriend = False
        sniperBattleFlash.setTarget(isFriend)

        # if f_delayHideTarget is not None:
        #     BigWorld.cancelCallback(f_delayHideTarget)
        # _type = entity.typeDescriptor.type
        _gun = entity.typeDescriptor.gun
        _miscAttrs = entity.typeDescriptor.miscAttrs
        _turret = entity.typeDescriptor.turret
        crewLevelIncrease = 0.0043 * _miscAttrs.get('crewLevelIncrease', 0)
        # targetVehicle = _type.shortUserString
        # targetName = entity.publicInfo.name
        targetReload = _gun.reloadTime * _miscAttrs.get('gunReloadTimeFactor', 1) / (1.0695 + crewLevelIncrease)
        targetReload = '%.1f' % targetReload
        targetVisionRadius = _turret.circularVisionRadius * _miscAttrs.get('circularVisionRadiusFactor', 1) / (1.0434 + crewLevelIncrease)
        try:
            curTarget = BigWorld.target()
            curTargetSpeed = int(round(getSpeed(curTarget) * MeltyElement.speedmulti, 0))
        except:
            curTargetSpeed = 9999
        sniperBattleFlash.updateVehicleSpeed(curTargetSpeed)
        newDistance = int((BigWorld.target().position - BigWorld.player().getOwnVehiclePosition()).length)
        sniperBattleFlash.setTargetParams(targetReload, targetVisionRadius, newDistance)
        sniperBattleFlash.updateTarget(newDistance, BigWorld.entity(BigWorld.target().id).health)


@overrideMethod(plug, '_makeSettingsVO')
def plugins_makeSettingsVO(base, settingsCore, *keys):
    data = base(settingsCore, *keys)
    if isNotEvent:
        for mode in data:
            centerAlpha = data[mode]['centerAlphaValue']
            centerType = data[mode]['centerType']
            netType = data[mode]['netType']
            # netType = data[mode]['netType']
            # gunTagType = data[mode]['gunTagType']
            # gunTagAlpha = data[mode]['gunTagAlpha']
            # mixingType = data[mode]['mixingType']
            # mixingAlpha = data[mode]['mixingAlpha']
            reloadAlpha = data[mode]['reloaderTimerAlphaValue']
            conditionAlpha = data[mode]['conditionAlphaValue']
            cassetteAlpha = data[mode]['cassetteAlphaValue']

            # self._flashCall('setCenterType', [self._Aim__aimSettings['centralTag'], self._Aim__aimSettings['centralTagType']])
            sniperBattleFlash.setCenterType(100, centerType)
            # self._flashCall('setNetType', [self._Aim__aimSettings['net'], self._Aim__aimSettings['netType']])
            sniperBattleFlash.setNetType(100, netType)
            # self._flashCall('setReloaderType', [self._Aim__aimSettings['reloader'], 0])
            sniperBattleFlash.setReloaderType(100, 0)
            # self._flashCall('setConditionType', [self._Aim__aimSettings['condition'], 0])
            sniperBattleFlash.setConditionType(100, 0)
            # self._flashCall('setCassetteType', [self._Aim__aimSettings['cassette'], 0])
            sniperBattleFlash.setCassetteType(100, 0)
            # print "centerType:", centerType, "netType:", netType, "centerAlpha", centerAlpha, "reloadAlpha", reloadAlpha
            if 'centerAlphaValue' in data[mode]:
                data[mode]['centerAlphaValue'] = 0
            if 'netAlphaValue' in data[mode]:
                data[mode]['netAlphaValue'] = 0
            if 'reloaderAlphaValue' in data[mode]:
                data[mode]['reloaderAlphaValue'] = 0
            if 'conditionAlphaValue' in data[mode]:
                data[mode]['conditionAlphaValue'] = 0
            if 'cassetteAlphaValue' in data[mode]:
                data[mode]['cassetteAlphaValue'] = 0
            if 'reloaderTimerAlphaValue' in data[mode]:
                data[mode]['reloaderTimerAlphaValue'] = 0
            if 'zoomIndicatorAlphaValue' in data[mode]:
                data[mode]['zoomIndicatorAlphaValue'] = 0
    return data


@registerEvent(ArcadeAimingSystem, 'enable')
def ArcadeAimingSystem_enable(self, targetPos, turretYaw=None, gunPitch=None):
    global cameraMode
    cameraMode = 'arcade'
    sniperBattleFlash.component.visible = False


@registerEvent(SniperAimingSystem, 'enable')
def SniperAimingSystem_enable(self, targetPos, playerGunMatFunction):
    global cameraMode
    cameraMode = 'sniper'
    sniperBattleFlash.component.visible = True


@registerEvent(StrategicAimingSystem, 'enable')
def StrategicAimingSystem_enable(self, targetPos):
    global cameraMode
    cameraMode = 'strategic'
    sniperBattleFlash.component.visible = False


@registerEvent(SiegeModeControl, 'notifySiegeModeChanged')
def SiegeModeControl_notifySiegeModeChanged(self, vehicle, newState, timeToNextMode):
    global siegeMode
    if not vehicle.isPlayerVehicle:
        return
    prev_siegeMode = siegeMode
    siegeMode = 'siege' if newState == 2 else None
    if prev_siegeMode != siegeMode:
        print "rev_siegeMode != siegeMode"


check()
MeltyElement = MeltyElement()
