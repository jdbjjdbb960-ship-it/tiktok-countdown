[app]

title = TikTok Countdown
package.name = tiktokcountdown
package.domain = org.sawit

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0

requirements = python3,kivy,pyjnius

orientation = portrait

fullscreen = 0

android.api = 35
android.minapi = 23

android.archs = arm64-v8a, armeabi-v7a

android.allow_backup = True

[buildozer]

log_level = 2
warn_on_root = 1
