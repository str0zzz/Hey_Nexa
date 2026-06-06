[app]
title = Nexa Ultimate
package.name = nexaultimate
package.domain = com.nexa.ultimate
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,html
version = 3.0.0
requirements = python3,kivy==2.3.0,pyjnius,plyer,speechrecognition,android
orientation = portrait
fullscreen = 0
icon.filename = icon.png
presplash.filename = icon.png

[buildozer]
log_level = 2
warn_on_root = 1

[permissions]
android.permissions = RECORD_AUDIO, CAMERA, INTERNET, ACCESS_FINE_LOCATION, ACCESS_COARSE_LOCATION, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, BLUETOOTH, BLUETOOTH_ADMIN, BLUETOOTH_CONNECT, BLUETOOTH_SCAN, ACCESS_WIFI_STATE, CHANGE_WIFI_STATE, ACCESS_NETWORK_STATE, CHANGE_NETWORK_STATE, READ_SMS, SEND_SMS, RECEIVE_SMS, CALL_PHONE, READ_PHONE_STATE, VIBRATE, FLASHLIGHT, WAKE_LOCK, FOREGROUND_SERVICE, SYSTEM_ALERT_WINDOW, REQUEST_INSTALL_PACKAGES, QUERY_ALL_PACKAGES, POST_NOTIFICATIONS, READ_CONTACTS, WRITE_CONTACTS, READ_MEDIA_AUDIO, READ_MEDIA_IMAGES

[android]
# Enforce latest API standard to solve Java/Gradle mismatched environments
android.api = 34
android.minapi = 24
android.ndk_api = 24

# Set to arm64 to properly support devices like Redmi
android.archs = arm64-v8a

android.gradle_dependencies = androidx.core:core:1.9.0
android.accept_sdk_license = True
android.allow_download = True

# P4A specific bindings to prevent build breaks with newer Gradle wrappers
p4a.branch = master
p4a.bootstrap = sdl2

android.icon = icon.png
android.presplash = icon.png
