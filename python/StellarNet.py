# from stellarnet_driverLibs import stellarnet_driver3 as sn

# # For Windows ONLY: Must be run in administrator mode
# # Only need to run it one time after switch back from the SpectraWiz.
# sn.installDeviceDriver()

# # This resturn a Version number of compilation date of driver
# version = sn.version()
# print(version)	

# # Device parameters to set       
# inttime = 100   # 1-498000 ms
# scansavg = 1   # > 1
# smooth = 1     # 1-4
# xtiming = 3    # 1-4


# #init Spectrometer - Get BOTH spectrometer and wavelength
# spectrometer, wav = sn.array_get_spec(0) # 0 for first channel and 1 for second channel , up to 127 spectrometers
# """
# # Equivalent to get spectrometer and wav separately:
# spectrometer = sn.array_get_spec_only(0) 
# wav = sn.getSpectrum_X(spectrometer)
# """

# print(spectrometer)
# sn.ext_trig(spectrometer, True)

# # Get device ID
# deviceID = sn.getDeviceId(spectrometer)
# print('\nMy device ID: ', deviceID)

# # Get current device parameter
# currentParam = sn.getDeviceParam(spectrometer)

# # Call to Enable or Disable External Trigger to by default is Disbale=False -> with timeout
# # Enable or Disable Ext Trigger by Passing True or False, If pass True than Timeout function will be disable, so user can also use this function as timeout enable/disbale 
# sn.ext_trig(spectrometer,True)

# # Only call this function on first call to get spectrum or when you want to change device setting.
# # -- Set last parameter to 'True' throw away the first spectrum data because the data may not be true for its inttime after the update.
# # -- Set to 'False' if you want to throw away the first data, however your next spectrum data might not be valid.
# sn.setParam(spectrometer, inttime, scansavg, smooth, xtiming, True) 

# # Get spectrometer data - Get BOTH X and Y in single return
# first_data = sn.array_spectrum(spectrometer, wav) 

# # Release the spectrometer before ends the program
# sn.reset(spectrometer)

# # For Windows ONLY: Must be run in administrator mode
# # sn.uninstallDeviceDriver() 


from stellarnet_driverLibs import stellarnet_driver3 as sn
import numpy as np

class StellarNetSpectrometer:
    def __init__(self, channel=0):
        """
        Initializes the spectrometer driver and prepares the device for data collection.
        :param channel: The channel to initialize, default is 0 for the first channel.
        """
        self.channel = channel
        self.spectrometer = None
        self.wav = None
        self.device_id = None
        self._inttime=100
        self._scansavg=1
        self._xtiming = 3

        # Install device driver (Windows only, admin mode required)
        sn.installDeviceDriver()

        # Check driver version
        self.version = sn.version()
        print(f"Driver version: {self.version}")

        # Initialize the spectrometer and wavelength array
        self.spectrometer, self.wav = sn.array_get_spec(self.channel)
        if self.spectrometer is None:
            raise RuntimeError("Failed to initialize the spectrometer.")
        
        print(f"Spectrometer initialized: {self.spectrometer}")
        self.device_id = sn.getDeviceId(self.spectrometer)
        print(f"My device ID: {self.device_id}")
        self.set_parameters()

    def set_parameters(self, discard_first=True):
        """
        Configures the device parameters.
        :param inttime: Integration time in ms (1-498000 ms).
        :param scansavg: Number of scans to average (> 1).
        :param smooth: Smoothing factor (1-4).
        :param xtiming: Timing multiplier (1-4).
        :param discard_first: Whether to discard the first spectrum after parameter changes.
        """
        sn.setParam(self.spectrometer, self._inttime, self._scansavg, 0, self._xtiming, discard_first)

    def enable_external_trigger(self, enable=True):
        """
        Enables or disables the external trigger.
        :param enable: True to enable, False to disable.
        """
        sn.ext_trig(self.spectrometer, enable)

    def release(self):
        """
        Releases the spectrometer and resets the driver.
        """
        if self.spectrometer is not None:
            sn.reset(self.spectrometer)

    @property
    def spectrum(self):
        """
        Retrieves both the wavelength (X) and intensity (Y) data from the spectrometer.
        :return: intensities.
        """
        if self.spectrometer is None or self.wav is None:
            raise RuntimeError("Spectrometer is not initialized.")
        spectrum = sn.array_spectrum(self.spectrometer, self.wav)[:,1]
        return spectrum.tolist()

    @property
    def wavelength(self):
        return self.wav[:,0].tolist()

    @property
    def inttime(self):
        return self._inttime
    

    @inttime.setter
    def inttime(self,VAL):
        self._inttime=int(VAL)
        self.set_parameters()  

    @property
    def scansavg(self):
        return self._scansavg
    

    @scansavg.setter
    def scansavg(self,VAL):
        self._scansavg=int(VAL)
        self.set_parameters()

    @property
    def xtiming(self):
        return self._xtiming
    

    @xtiming.setter
    def xtiming(self,VAL):
        self._xtiming=int(VAL)
        self.set_parameters()