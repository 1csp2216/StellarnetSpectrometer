#!../../bin/linux-x86_64/pydevioc

< envPaths

# PYTHONPATH points to folders where Python modules are.
epicsEnvSet("PYTHONPATH","$(TOP)/python")

cd ${TOP}

## Register all support components
dbLoadDatabase "${TOP}/dbd/pydevioc.dbd"
pydevioc_registerRecordDeviceDriver pdbbase

## Load record instances
dbLoadRecords("${TOP}/db/StellarNet.db","P=StellarNet1")

cd ${TOP}/iocBoot/${IOC}

pydev("from StellarNet import StellarNetSpectrometer")
pydev("sns = StellarNetSpectrometer()")


iocInit
