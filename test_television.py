import pytest
from television import Television

class TestTelevision:
    def test_init(self):
        """Test initial values when TV is created"""
        tv = Television()
        assert str(tv) == "Power = [False], Channel = [0], Volume = [0]"

    def test_power(self):
        """Test power method turns TV on and off"""
        tv = Television()
        tv.power()
        assert str(tv) == "Power = [True], Channel = [0], Volume = [0]"
        tv.power()
        assert str(tv) == "Power = [False], Channel = [0], Volume = [0]"

    def test_mute(self):
        """Test mute functionality with TV on"""
        tv = Television()
        tv.power()
        tv.volume_up()
        assert str(tv) == "Power = [True], Channel = [0], Volume = [1]"
        tv.mute()
        assert str(tv) == "Power = [True], Channel = [0], Volume = [0]"
        tv.mute()
        assert str(tv) == "Power = [True], Channel = [0], Volume = [1]"

    def test_mute_tv_off(self):
        """Test that mute doesn't work when TV is off"""
        tv = Television()
        tv.mute()
        assert str(tv) == "Power = [False], Channel = [0], Volume = [0]"

    def test_channel_up(self):
        """Test channel up with TV on"""
        tv = Television()
        tv.power()
        tv.channel_up()
        assert str(tv) == "Power = [True], Channel = [1], Volume = [0]"
        tv.channel_up()
        tv.channel_up()
        tv.channel_up()
        assert str(tv) == "Power = [True], Channel = [0], Volume = [0]"

    def test_channel_up_tv_off(self):
        """Test channel up doesn't work with TV off"""
        tv = Television()
        tv.channel_up()
        assert str(tv) == "Power = [False], Channel = [0], Volume = [0]"

    def test_channel_down(self):
        """Test channel down with TV on"""
        tv = Television()
        tv.power()
        tv.channel_down()
        assert str(tv) == "Power = [True], Channel = [3], Volume = [0]"
        tv.channel_down()
        assert str(tv) == "Power = [True], Channel = [2], Volume = [0]"

    def test_channel_down_tv_off(self):
        """Test channel down doesn't work with TV off"""
        tv = Television()
        tv.channel_down()
        assert str(tv) == "Power = [False], Channel = [0], Volume = [0]"

    def test_volume_up(self):
        """Test volume up with TV on"""
        tv = Television()
        tv.power()
        tv.volume_up()
        assert str(tv) == "Power = [True], Channel = [0], Volume = [1]"
        tv.volume_up()
        tv.volume_up()  # Try to go past max
        assert str(tv) == "Power = [True], Channel = [0], Volume = [2]"

    def test_volume_up_tv_off(self):
        """Test volume up doesn't work with TV off"""
        tv = Television()
        tv.volume_up()
        assert str(tv) == "Power = [False], Channel = [0], Volume = [0]"

    def test_volume_up_with_mute(self):
        """Test volume up unmutes TV"""
        tv = Television()
        tv.power()
        tv.volume_up()
        tv.mute()
        tv.volume_up()
        assert str(tv) == "Power = [True], Channel = [0], Volume = [2]"

    def test_volume_down(self):
        """Test volume down with TV on"""
        tv = Television()
        tv.power()
        tv.volume_up()
        tv.volume_up()
        tv.volume_down()
        assert str(tv) == "Power = [True], Channel = [0], Volume = [1]"
        tv.volume_down()
        tv.volume_down()  # Try to go past min
        assert str(tv) == "Power = [True], Channel = [0], Volume = [0]"

    def test_volume_down_tv_off(self):
        """Test volume down doesn't work with TV off"""
        tv = Television()
        tv.volume_down()
        assert str(tv) == "Power = [False], Channel = [0], Volume = [0]"

    def test_volume_down_with_mute(self):
        """Test volume down unmutes TV"""
        tv = Television()
        tv.power()
        tv.volume_up()
        tv.mute()
        tv.volume_down()
        assert str(tv) == "Power = [True], Channel = [0], Volume = [0]"