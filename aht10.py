import time

class AHT10:
    def __init__(self, i2c, address=0x38):
        self.i2c = i2c
        self.addr = address
        time.sleep_ms(20)
        self._init_sensor()

    def _init_sensor(self):
        try:
            self.i2c.writeto(self.addr, bytearray([0xE1, 0x08, 0x00]))
            time.sleep_ms(10)
        except OSError:
            pass

    def read_raw_data(self):
        self.i2c.writeto(self.addr, bytearray([0xAC, 0x33, 0x00]))
        time.sleep_ms(80)
        data = self.i2c.readfrom(self.addr, 6)
        return data

    def read(self):
        data = self.read_raw_data()
        if (data[0] & 0x80) == 0:
            hum_raw = ((data[1] << 12) | (data[2] << 4) | (data[3] >> 4))
            temp_raw = (((data[3] & 0x0F) << 16) | (data[4] << 8) | data[5])
            humidity = (hum_raw * 100) / 1048576
            temperature = (temp_raw * 200 / 1048576) - 50
            return temperature, humidity
        else:
            return None, None
