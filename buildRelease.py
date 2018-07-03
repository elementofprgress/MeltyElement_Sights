import py_compile, zipfile, os
import subprocess

import shutil


def move(src, dest):
    shutil.copy(src, dest)

def prepareDir(targetPath):
    if os.path.exists(targetPath):
        return True
    dirName = os.path.dirname(targetPath)
    if not os.path.exists(dirName): os.makedirs(dirName)


WOTVersion = "1.0.2.1"
ModVersion = "v1.0.0b"
GUIFlashVer = "0.2.5"

releaseDir = "release/WoT_" + WOTVersion
if not os.path.exists(releaseDir):
    os.makedirs(releaseDir)

releaseFile = "release/WoT_" + WOTVersion + "/mod_MeltyElementSights_" + ModVersion + ".7z"
if os.path.exists(releaseFile):
    os.remove(releaseFile)

py_compile.compile("source/python/mod_ArcadeBattleFlash.py")
py_compile.compile("source/python/mod_ArtyBattleFlash.py")
py_compile.compile("source/python/mod_SniperBattleFlash.py")

prepareDir(releaseDir + "/res_mods/" + WOTVersion + "/scripts/client/gui/mods/")
move("source/python/mod_ArcadeBattleFlash.pyc", releaseDir + "/res_mods/" + WOTVersion + "/scripts/client/gui/mods/" + "mod_ArcadeBattleFlash.pyc")
move("source/python/mod_ArtyBattleFlash.pyc", releaseDir + "/res_mods/" + WOTVersion + "/scripts/client/gui/mods/" + "mod_ArtyBattleFlash.pyc")
move("source/python/mod_SniperBattleFlash.pyc", releaseDir + "/res_mods/" + WOTVersion + "/scripts/client/gui/mods/" + "mod_SniperBattleFlash.pyc")

prepareDir(releaseDir + "/res_mods/" + WOTVersion + "/gui/flash/")
move("source/flash/ArcadeBattleFlash/ArcadeBattleFlash.swf", releaseDir + "/res_mods/" + WOTVersion + "/gui/flash/" + "ArcadeBattleFlash.swf")
move("source/flash/ArtyBattleFlash/ArtyBattleFlash.swf", releaseDir + "/res_mods/" + WOTVersion + "/gui/flash/" + "ArtyBattleFlash.swf")
move("source/flash/SniperBattleFlash/SniperBattleFlash.swf", releaseDir + "/res_mods/" + WOTVersion + "/gui/flash/" + "SniperBattleFlash.swf")

move("source/config/ElementCrosshairSettings.xml", releaseDir + "/res_mods/" + WOTVersion + "/gui/flash/" + "ElementCrosshairSettings.xml")
subprocess.call(['7z', 'a', releaseDir + '/Melty_Element_Fonts.7z', "source/fonts/*.*"])

prepareDir(releaseDir + "/mods/" + WOTVersion + "/")
move("GUIFlash/gambiter.guiflash_0.2.5.wotmod", releaseDir + "/mods/" + WOTVersion + "/gambiter.guiflash_" + GUIFlashVer + ".wotmod")

subprocess.call(['7z', 'a', releaseFile, releaseDir])

os.remove(releaseDir + '/Melty_Element_Fonts.7z')
