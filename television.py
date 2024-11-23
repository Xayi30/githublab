class Television:
    """
    A class representing a television object with basic controls.
    """
    # Class variables (constants)
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3
    
    def __init__(self) -> None:
        """
        Initialize a new Television instance with default settings.
        All instance variables are private.
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL
    
    def power(self) -> None:
        """
        Toggle the power status of the TV between on and off.
        """
        self.__status = not self.__status
    
    def mute(self) -> None:
        """
        Toggle the mute status if the TV is on.
        If TV is muted, volume will display as 0.
        Only works when TV is powered on.
        """
        if self.__status:
            self.__muted = not self.__muted
            
    def channel_up(self) -> None:
        """
        Increase TV channel by 1 if TV is on.
        If at maximum channel (3), wraps around to minimum channel (0).
        Only works when TV is powered on.
        """
        if self.__status:
            if self.__channel == self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel += 1
                
    def channel_down(self) -> None:
        """
        Decrease TV channel by 1 if TV is on.
        If at minimum channel (0), wraps around to maximum channel (3).
        Only works when TV is powered on.
        """
        if self.__status:
            if self.__channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """
        Increase TV volume by 1 if TV is on and volume is not at maximum.
        If TV is muted, unmutes first.
        Maximum volume is 2.
        Only works when TV is powered on.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Decrease TV volume by 1 if TV is on and volume is not at minimum.
        If TV is muted, unmutes first.
        Minimum volume is 0.
        Only works when TV is powered on.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Return a string representation of the TV status.
        
        Returns:
            str: Status string in format "Power = [status], Channel = [channel], Volume = [volume]"
        """
        displayed_volume = 0 if self.__muted else self.__volume
        return f"Power = [{self.__status}], Channel = [{self.__channel}], Volume = [{displayed_volume}]"