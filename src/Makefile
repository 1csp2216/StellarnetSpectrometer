# Makefile
TOP = ..
include $(TOP)/configure/CONFIG
include $(TOP)/configure/CONFIG.PyDevice
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE

# ----------- ここから
PYTHON_LIB_DIR :=$(shell python -c 'from distutils import sysconfig; print(sysconfig.get_config_var("LIBDIR"))')
PYTHON_VERSION := $(shell python -c "import platform; print(platform.python_version())")
PYTHON_MAJOR_VERSION = $(word 1, $(subst ., ,$(PYTHON_VERSION)))
PYTHON_MINOR_VERSION = $(word 2, $(subst ., ,$(PYTHON_VERSION)))
USR_LDFLAGS += -L$(PYTHON_LIB_DIR) -Wl,-rpath,$(PYTHON_LIB_DIR) -lpython$(PYTHON_MAJOR_VERSION).$(PYTHON_MINOR_VERSION)
pydev_LIBS += Com
pydev_LIBS += dbCore
# ----------- ここまで追加

USR_CXXFLAGS += -std=c++11 -O2 -DUSE_TYPED_RSET
CXXFLAGS += -g -ggdb -O0

LIBRARY_IOC += pydev

DBD += pydev.dbd
DBDINC += pycalcRecord

pydev_DBD += pycalcRecord.dbd

pydev_SRCS += asyncexec.cpp
pydev_SRCS += epicsdevice.cpp
pydev_SRCS += pywrapper.cpp
pydev_SRCS += util.cpp
pydev_SRCS += pydev_ai.cpp
pydev_SRCS += pydev_ao.cpp
pydev_SRCS += pydev_bi.cpp
pydev_SRCS += pydev_bo.cpp
pydev_SRCS += pydev_mbbi.cpp
pydev_SRCS += pydev_mbbo.cpp
pydev_SRCS += pydev_longin.cpp
pydev_SRCS += pydev_longout.cpp
pydev_SRCS += pydev_stringin.cpp
pydev_SRCS += pydev_stringout.cpp
pydev_SRCS += pydev_waveform.cpp
pydev_SRCS += pycalcRecord.cpp
pydev_SRCS += variant.cpp

# 3.15 and above support lsi, lso and printf records  
ifdef BASE_3_15
  DBD += pydev315.dbd
  pydev_SRCS += pydev_lsi.cpp
  pydev_SRCS += pydev_lso.cpp
endif

pydevice_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES

