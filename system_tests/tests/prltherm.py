import unittest

from utils.channel_access import ChannelAccess
from utils.ioc_launcher import get_default_ioc_dir
from utils.test_modes import TestModes
from utils.testing import get_running_lewis_and_ioc


DEVICE_PREFIX = "PRLTHERM_01"


IOCS = [
    {
        "name": DEVICE_PREFIX,
        "directory": get_default_ioc_dir("PRLTHERM"),
        "macros": {},
        "pv_for_existence": "TEMP01"
    },
]


TEST_MODES = [TestModes.RECSIM]


class PrlthermTests(unittest.TestCase):
    """
    Tests for the Prltherm IOC (PEARL Thermometry device using DAQmx).
    """
    def setUp(self):
        self._lewis, self._ioc = get_running_lewis_and_ioc("Prltherm", DEVICE_PREFIX)
        self.ca = ChannelAccess(device_prefix=DEVICE_PREFIX)

    def test_WHEN_ioc_is_started_THEN_PV_exists(self):
        self.ca.assert_that_pv_exists(IOCS[0]['pv_for_existence'], timeout=30)
