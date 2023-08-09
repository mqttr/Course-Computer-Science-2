class Television:
    
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3


    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
    
    def power(self):
        self.__status = not self.__status
        return

    def mute(self):
        if self.__status == False: return

        self.__muted = not self.__muted
        return

    def channel_up(self):
        if self.__status == False: return

        self.__channel = self.__channel +1
        if self.__channel > Television.MAX_CHANNEL:
            self.__channel = Television.MIN_CHANNEL
        return

    def channel_down(self):
        if self.__status == False: return

        self.__channel = self.__channel -1
        if self.__channel < Television.MIN_CHANNEL:
            self.__channel = Television.MAX_CHANNEL
        return

    def volume_up(self):
        if self.__status == False: return
        
        if self.__muted == True:
            self.__muted = False
            
        if self.__volume+1 > Television.MAX_VOLUME:
            self.__volume = Television.MAX_VOLUME
        else:
            self.__volume = self.__volume+1

        return

    def volume_down(self):
        if self.__status == False: 
            return
        
        if self.__muted == True:
            self.__muted = False

        if self.__volume -1 < Television.MIN_VOLUME:
            self.__volume = Television.MIN_VOLUME
        else:
            self.__volume = self.__volume -1
        
        return

    def __str__(self):
        if self.__muted == True: trueVolume = 0
        else: trueVolume = self.__volume
        return f"TV status: Power = {self.__status}, Channel = {self.__channel}, Volume = {trueVolume}"