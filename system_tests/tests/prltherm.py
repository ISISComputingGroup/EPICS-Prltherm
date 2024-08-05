import unittest

from utils.channel_access import ChannelAccess
from utils.ioc_launcher import IOCRegister, ProcServLauncher, get_default_ioc_dir
from utils.test_modes import TestModes

DEVICE_PREFIX = "PRLTHERM_01"


IOCS = [
    {
        "name": DEVICE_PREFIX,
        "directory": get_default_ioc_dir("PRLTHERM"),
        "macros": {},
        "pv_for_existence_base_name": "TEMP",
        "number_of_channels": 16,
        "ioc_launcher_class": ProcServLauncher,
    },
]


TEST_MODES = [TestModes.RECSIM]


class PrlthermTests(unittest.TestCase):
    """
    Tests for the Prltherm IOC (PEARL Thermometry device using DAQmx).
    """
   
    def setUp(self):
        self._ioc = IOCRegister.get_running(DEVICE_PREFIX)
        self.ca = ChannelAccess(device_prefix=DEVICE_PREFIX, default_wait_time=0.0)
        self.ca.assert_that_pv_exists("DISABLE", timeout=30)

    def test_WHEN_ioc_is_started_THEN_PVs_for_all_channels_exist(self):
        for i in range(1,IOCS[0]['number_of_channels']+1,1):
            pv_to_check = IOCS[0]['pv_for_existence_base_name']+f"{i:02}"
            self.ca.assert_that_pv_exists(pv_to_check, timeout=30)
