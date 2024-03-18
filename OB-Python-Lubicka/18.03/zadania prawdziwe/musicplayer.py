class MusicPlayer:
    current_track = "Not playing"
    firmware_version=1.0
    def __init__(self):
        self.__track_list=["Born on the bayou","Roxxane","Starman","Back in black"]
    def play(self):
        self.current_track=self.__track_list[0]
    def list_tracks(self):
        return self.__track_list
    def update_firmware(self,new_firmware):
        if self.firmware_version<new_firmware:
            self.firmware_version=new_firmware
player = MusicPlayer()
print("Tracks currently on device:", player.list_tracks())
player.update_firmware(2.0)
print("Updated player firmware version to", player.firmware_version)
player.play()
print("Currently playing", f"'{player.current_track}'")