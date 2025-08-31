[app]
title = 屏幕画面调整工具
package.name = screenadjuster
package.domain = org.myapp
version = 0.1
source.dir = .
source.include_exts = py,kv,jpg,png
source.exclude_exts = pyc,pyo,pyd
source.exclude_dirs = venv,env,bin
requirements = python3,kivy==2.3.1,pillow
android.api = 31
android.minapi = 21
android.buildTools = 31.0.0
android.ndk = 25b
android.permissions = INTERNET
android.orientation = landscape,portrait
log_level = 2
warn_on_root = 1
ios = False
osx = False
windows = False
linux = False
orientation = portrait
fullscreen = 0
[buildozer]
log_level = 2
warn_on_root = 1
android.accept_sdk_license = True