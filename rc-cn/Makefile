FINALPACKAGE=1
TARGET := iphone:clang:16.5:15.0
ARCHS = arm64 arm64e

include $(THEOS)/makefiles/common.mk

TWEAK_NAME = RemoteCompanionCN
RemoteCompanionCN_FILES = RemoteCompanionCN.x
RemoteCompanionCN_CFLAGS = -fobjc-arc -Wno-unused-function
RemoteCompanionCN_FRAMEWORKS = UIKit Foundation

include $(THEOS_MAKE_PATH)/tweak.mk
