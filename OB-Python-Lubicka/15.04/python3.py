from abc import ABC, abstractmethod
class RemoteControl(ABC):
    def __init__(self, device):
        self._device = device

    def togglePower(self):
        if self._device.isEnabled():
            self._device.disable()
        else:
            self._device.enable()

    def volumeDown(self):
        self._device.setVolume(self._device.getVolume() - 10)

    def volumeUp(self):
        self._device.setVolume(self._device.getVolume() + 10)

    def channelDown(self):
        self._device.setChannel(self._device.getChannel() - 1)

    def channelUp(self):
        self._device.setChannel(self._device.getChannel() + 1)

class AdvancedRemoteControl(RemoteControl):
    def mute(self):
        self._device.setVolume(0)

class Device(ABC):
    @abstractmethod
    def isEnabled(self):
        pass

    @abstractmethod
    def enable(self):
        pass

    @abstractmethod
    def disable(self):
        pass

    @abstractmethod
    def getVolume(self):
        pass

    @abstractmethod
    def setVolume(self, percent):
        pass

    @abstractmethod
    def getChannel(self):
        pass

    @abstractmethod
    def setChannel(self, channel):
        pass

class TV(Device):
    def isEnabled(self):
        pass

    def enable(self):
        # Logika włączania telewizora
        pass

    def disable(self):
        # Logika wyłączania telewizora
        pass

    def getVolume(self):
        # Logika pobierania głośności telewizora
        pass

    def setVolume(self, percent):
        # Logika ustawiania głośności telewizora
        pass

    def getChannel(self):
        # Logika pobierania aktualnego kanału telewizora
        pass

    def setChannel(self, channel):
        # Logika ustawiania kanału telewizora
        pass

class Radio(Device):
    def isEnabled(self):
        # Logika sprawdzająca czy radio jest włączone
        pass

    def enable(self):
        # Logika włączania radia
        pass

    def disable(self):
        # Logika wyłączania radia
        pass

    def getVolume(self):
        # Logika pobierania głośności radia
        pass

    def setVolume(self, percent):
        # Logika ustawiania głośności radia
        pass

    def getChannel(self):
        # Logika pobierania aktualnego kanału radia
        pass

    def setChannel(self, channel):
        # Logika ustawiania kanału radia
        pass

# Przykład użycia
tv = TV()
remote = RemoteControl(tv)
remote.togglePower()

radio = Radio()
advanced_remote = AdvancedRemoteControl(radio)
advanced_remote.mute()
