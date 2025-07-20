from micropython import const
import framebuf
import time

class SH1106_I2C(framebuf.FrameBuffer):
    def __init__(self, width, height, i2c, addr=0x3C):
        self.width = width
        self.height = height
        self.i2c = i2c
        self.addr = addr
        self.pages = self.height // 8
        self.buffer = bytearray(self.width * self.pages)
        super().__init__(self.buffer, self.width, self.height, framebuf.MONO_VLSB)

        time.sleep_ms(100)
        self.init_display()
        self.fill(0)
        self.show()

    def write_cmd(self, cmd):
        try:
            self.i2c.writeto(self.addr, b'\x00' + bytearray([cmd]))
        except Exception as e:
            print("[OLED E/S ERROR]", e)
            raise

    def init_display(self):
        for cmd in (
            0xAE, 0xD5, 0x80,
            0xA8, 0x3F, 0xD3, 0x00,
            0x40, 0xAD, 0x8B,
            0xA1, 0xC8, 0xDA, 0x12,
            0x81, 0xCF, 0xD9, 0xF1,
            0xDB, 0x40, 0xA4, 0xA6,
            0xAF
        ):
            self.write_cmd(cmd)

    def show(self):
        for page in range(self.pages):
            self.write_cmd(0xB0 + page)
            self.write_cmd(0x02)
            self.write_cmd(0x10)
            start = self.width * page
            end = start + self.width
            self.i2c.writeto(self.addr, b'\x40' + self.buffer[start:end])
