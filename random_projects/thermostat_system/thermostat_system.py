# You're building a smart thermostat alert system:
# If the device_status is "active"
# And temperature > 35 → Warn: "High temperature alert!"
# Else: "Temperature normal"
# If device is off → "Device is offline"
from dataclasses import dataclass
from unittest import TestCase


@dataclass
class Thermostat:
    __device_status: bool
    __temperature: int

    def __init__(self, status, temperature):
        assert type(status) is str, "Status must be string ('active' or 'inactive')"
        assert status.strip().lower() in ['active','inactive'], "Status must be 'active' or 'inactive' "
        assert type(temperature) is int, "Temperature must be integer value"
        self.__device_status = True if status.strip().lower() == 'active' else False
        self.__temperature = temperature

    @property
    def device_status(self) -> str:
        if self.__device_status:
            if self.__temperature > 35:
                return 'High temperature alert!'
            else:
                return 'Temperature normal'
        return 'Device is offline'

    def turn_on(self):
        self.__device_status = True

    def turn_off(self):
        self.__device_status = False

    def set_temperature(self, value):
        assert type(value) is int, "Temperature must be integer value"
        self.__temperature = value

class TestTermostat(TestCase):

    def test_wrong_init_values(self):
        with self.assertRaises(AssertionError):
            Thermostat(None, 5)
        with self.assertRaises(AssertionError):
            Thermostat('', 5)
        with self.assertRaises(AssertionError):
            Thermostat(0, 5)
        with self.assertRaises(AssertionError):
            Thermostat('active', 5.5)
        with self.assertRaises(AssertionError):
            Thermostat('active', 'five')
        with self.assertRaises(AssertionError):
            Thermostat('active', None)

    def test_device_status_normal(self):
        self.assertEqual(Thermostat('active',15).device_status, 'Temperature normal')
        self.assertEqual(Thermostat('active',0).device_status, 'Temperature normal')
        self.assertEqual(Thermostat('active',-7).device_status, 'Temperature normal')

    def test_device_status_high(self):
        self.assertEqual(Thermostat('active',36).device_status, 'High temperature alert!')
        self.assertEqual(Thermostat('active',40).device_status, 'High temperature alert!')
        self.assertEqual(Thermostat('active',85).device_status, 'High temperature alert!')

    def test_device_status_offline(self):
        self.assertEqual(Thermostat('inactive',-10).device_status, 'Device is offline')
        self.assertEqual(Thermostat('inactive',25).device_status, 'Device is offline')
        self.assertEqual(Thermostat('inactive',85).device_status, 'Device is offline')