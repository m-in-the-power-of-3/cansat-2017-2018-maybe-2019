from settings import *
import threading
import os
import struct
import serial
import i2cdev

import ads1115
import bmp180
import buzzer
import socket_data
import tsl2561
import nrf24l01
import inav
import motor
import fuse
import trigger


class Send_manager():
    def __init__(self):
        self.data = None
        self.stop_flag = False

    def init(self):
        self.rc_hardware = []
        self.rc_hardware.append(Socket_interface(IP, PORT))
        self.rc_hardware.append(Nrf24l01_interface([CE_PIN, CHANNEL, PIPES,
                                                    NRF24_FREQ, ADDRESS_WIDTH,
                                                    DATA_RATE, CRC_LEN]))
        for hardware in self.rc_hardware:
            hardware.init()

        self.thread = threading.Thread(target=self.send_data)
        self.thread.daemon = True
        self.lock_stop_flag = threading.Lock()
        self.lock_data = threading.Lock()

    def start(self):
        self.thread.start()

    def add_data(self, data):
        self.lock_data.acquire()
        self.data = data
        self.lock_data.release()

    def send_data(self):
        self.lock_stop_flag.acquire()
        if self.stop_flag:
            self.lock_stop_flag.release()
            return
        self.lock_stop_flag.release()

        self.lock_data.acquire()
        data = self.data
        self.data = None
        self.lock_data.release()

        for hardware in self.rc_hardware:
            if data is not None:
                hardware.send(data)

            if hardware.control_client is None:
                hardware.init()

    def stop(self):
        self.lock_stop_flag.acquire()
        self.stop_flag = True
        self.lock_stop_flag.release()
        self.thread.join()


class Inav_interface():
    def __init__(self, bus):
        self.control_client = None
        self.bus = bus
        self.data = [None, None, None, None, None, None, None, None, None]
        self.attitude = [None, None, None]
        self.gps_data = [None, None, None, None, None, None, None, None]

    def init(self):
        try:
            self.control_client = inav.Inav_control_client(self.bus)
            self.control_client.setup()
        except Exception as e:
            print (e)
            self.control_client = None

    def update(self):
        if self.control_client is not None:
            try:
                self.control_client.update_data()
                self.control_client.update_attitude()
                self.control_client.update_gps_data()
                self.data = self.control_client.get_data()
                self.attitude = self.control_client.get_attitude()
                self.gps_data = self.control_client.get_gps_data()
            except Exception as e:
                print (e)
                self.data = [None, None, None, None, None, None, None, None, None]
                self.attitude = [None, None, None]
                self.gps_data = [None, None, None, None, None, None, None, None]
                self.control_client = None

    def get_data(self):
        return self.data

    def get_attitude(self):
        return self.attitude

    def get_gps_data(self):
        return self.gps_data

    def deinit(self):
        if self.control_client is not None:
            try:
                self.control_client.close()
            except Exception as e:
                print (e)
                pass
            self.control_client = None


class Ads1115_interface():
    def __init__(self, bus):
        self.control_client = None
        self.bus = bus
        self.data = [None, None, None, None]

    def init(self):
        try:
            self.control_client = ads1115.Ads1115_control_client(self.bus)
            self.control_client.setup()
        except Exception as e:
            print (e)
            self.control_client = None

    def update(self):
        if self.control_client is not None:
            try:
                self.data = self.control_client.read_pins_voltage()
            except Exception as e:
                print (e)
                self.data = [None, None, None, None]
                self.control_client = None

    def get_data(self):
        return self.data[:-1]

    def deinit(self):
        if self.control_client is not None:
            try:
                self.control_client.close()
            except Exception as e:
                print (e)
                pass
            self.control_client = None


class Bmp180_interface():
    def __init__(self, bus):
        self.control_client = None
        self.bus = bus
        self.data = [None, None]

    def init(self):
        try:
            self.control_client = bmp180.Bmp180_control_client(self.bus)
            self.control_client.setup()
        except Exception as e:
            print (e)
            self.control_client = None

    def update(self):
        if self.control_client is not None:
            try:
                self.control_client.update_data()
                self.data[0] = self.control_client.get_pressure()
                self.data[1] = self.control_client.get_temperature()
            except Exception as e:
                print (e)
                self.data = [None, None]
                self.control_client = None

    def get_data(self):
        return self.data

    def deinit(self):
        if self.control_client is not None:
            try:
                self.control_client.close()
            except Exception as e:
                print (e)
                pass
            self.control_client = None


class Tsl2561_interface():
    def __init__(self, bus):
        self.control_client = None
        self.bus = bus
        self.data = [None]

    def init(self):
        try:
            self.control_client = tsl2561.Tsl2561_control_client(self.bus)
            self.control_client.setup()
        except Exception as e:
            print (e)
            self.control_client = None

    def update(self):
        if self.control_client is not None:
            try:
                self.data[0] = self.control_client.get_lux()
            except Exception as e:
                print (e)
                self.data = [None]
                self.control_client = None

    def get_data(self):
        return self.data

    def deinit(self):
        if self.control_client is not None:
            try:
                self.control_client.close()
            except Exception as e:
                print (e)
                pass
            self.control_client = None


class Trigger_interface():
    def __init__(self, bus):
        self.control_client = None
        self.bus = bus

    def init(self):
        try:
            self.control_client = trigger.Trigger_control_client(self.bus)
            self.control_client.setup()
        except Exception as e:
            print (e)
            self.control_client = None

    def get_data(self):
        if self.control_client is not None:
            try:
                return self.control_client.read()
            except Exception as e:
                print (e)
                self.control_client = None
        return False

    def deinit(self):
        if self.control_client is not None:
            self.control_client = None


class Buzzer_interface():
    def __init__(self, bus):
        self.control_client = None
        self.bus = bus

    def init(self):
        try:
            self.control_client = buzzer.Buzzer_control_client(self.bus)
            self.control_client.setup()
        except Exception as e:
            print (e)
            self.control_client = None

    def control(self, mode):
        if self.control_client is not None:
            try:
                if mode:
                    self.control_client.on()
                else:
                    self.control_client.off()
            except Exception as e:
                print (e)
                self.control_client = None

    def deinit(self):
        if self.control_client is not None:
            try:
                self.control_client.stop()
            except Exception as e:
                print (e)
                pass
            self.control_client = None


class Motor_interface():
    def __init__(self, bus):
        self.control_client = None
        self.bus = bus

    def init(self):
        try:
            self.control_client = motor.Motor_control_client(self.bus)
            self.control_client.setup()
        except Exception as e:
            print (e)
            self.control_client = None

    def control(self, mode):
        if self.control_client is not None:
            try:
                if mode:
                    self.control_client.on()
                else:
                    self.control_client.off()
            except Exception as e:
                print (e)
                self.control_client = None

    def deinit(self):
        if self.control_client is not None:
            self.control_client = None


class Fuse_interface():
    def __init__(self, bus):
        self.control_client = None
        self.bus = bus

    def init(self):
        try:
            self.control_client = fuse.Fuse_control_client(self.bus)
            self.control_client.setup()
        except Exception as e:
            print (e)
            self.control_client = None

    def control(self, mode):
        if self.control_client is not None:
            try:
                if mode:
                    self.control_client.on()
                else:
                    self.control_client.off()
            except Exception as e:
                print (e)
                self.control_client = None

    def deinit(self):
        if self.control_client is not None:
            self.control_client = None


class Socket_interface():
    def __init__(self, ip, port):
        self.control_client = None
        self.ip = ip
        self.port = port

    def init(self):
        try:
            self.control_client = socket_data.Socket_control_client(self.ip, self.port)
            self.control_client.setup()
        except Exception as e:
            print (e)
            self.control_client = None

    def send(self, data):
        if self.control_client is not None:
            try:
                self.control_client.send_data(data)
            except Exception as e:
                print (e)
                self.control_client = None

    def deinit(self):
        pass


class Inav_rc_interface():
    def __init__(self, bus):
        self.control_client = None
        self.bus = bus

    def init(self):
        try:
            self.control_client = socket_data.Inav_rc_i2c_control_client(self.bus)
            self.control_client.setup()
        except Exception as e:
            print (e)
            self.control_client = None

    def cut_data(self, data):
        return self.control_client.cut_data(data)

    def send_data(self, data):
        if self.control_client is not None:
            try:
                self.control_client.send_data(data)
            except Exception as e:
                print (e)
                self.control_client = None

    def send_message(self, message):
        if self.control_client is not None:
            try:
                self.control_client.send_message(data)
            except Exception as e:
                print (e)
                self.control_client = None

    def deinit(self):
        pass


class Nrf24l01_interface():
    def __init__(self, settings):
        self.control_client = None
        self.freq = settings[3]
        self.ce_pin = settings[0]
        self.channel = settings[1]
        self.addr_wight = settings[4]
        self.data_rate = settings[5]
        self.crc_len = settings[6]
        self.pipes = settings[2]

    def init(self):
        try:
            self.control_client = nrf24l01.Nrf24l01_control_client(self.freq, self.ce_pin, self.channel,
                                                                   self.addr_wight, self.data_rate,
                                                                   self.crc_len, self.pipes)
            self.control_client.setup()
        except Exception as e:
            print (e)
            self.control_client = None

    def send(self, data):
        if self.control_client is not None:
            try:
                i = 0
                while len(data) > 30:
                    i = i + 1
                    self.control_client.send_data(struct.pack('<B', *[i]) + data[:30])
                    data = data[30:]
                if i == 0:
                    self.control_client.send_data(data)
                else:
                    self.control_client.send_data(struct.pack('<B', *[i+1]) + data)
            except Exception as e:
                print (e)
                self.control_client = None

    def deinit(self):
        pass


class Observer():
    def __init__(self):
        pass

    def init_lux_observer(self, multiplier=0.5):
        self.lux_min = 65537
        self.lux_max = 0
        self.lux_level_multiplier = multiplier

    def find_lux_min(self, lux):
        if lux is not None:
            if (lux < self.lux_min):
                self.lux_min = lux

    def find_lux_max(self, lux):
        if lux is not None:
            if (lux > self.lux_max):
                self.lux_max = lux

    def compare_lux(self, lux):
        if lux is not None:
            level = self.lux_level_multiplier * (self.lux_max - self.lux_min)
            level = level + self.lux_min
            if (lux > level):
                return True
        return False

    def init_height_observer(self, pressure):
        self.pressure_at_start = pressure

    def find_height(self, pressure):
        if pressure is not None:
            x = pressure / pressure_at_start
            return 44330 * (1.0 - pow(x, 0.1903))
        return None

    def compare_height(self, pressure, height):
        if pressure is not None:
            height_now = find_height(pressure)
            if (height >= height_now):
                return True
            else:
                return False
        return False

    def init_gps_observer(self, lat_min, lon_min, lat_max, lon_max):
        self.lat_min = lat_min
        self.lon_min = lon_min
        self.lat_max = lat_max
        self.lon_max = lon_max

    def compare_gps(self, lat, lon):
        if (lat is not None) and (lon is not None):
            if (lat >= lat_min) and (lat <= lat_max) and (lon >= lon_min) and (lon <= lon_max):
                return True
            else:
                return False
        return False



# ================================================================
# Deinit
# ================================================================
def deinit_i2c(i2c):
    try:
        i2c.close()
    except Exception as e:
        print (e)
        pass


def deinit_uart(uart):
    try:
        uart.close()
    except Exception as e:
        print (e)
        pass


def deinit_internet():
    try:
        os.system(r'./internet_off.sh')
    except Exception as e:
        print (e)
        pass


# ================================================================
# Init
# ================================================================
def init_i2c():
    try:
        i2c = i2cdev.I2C(PORT_I2C)
        i2c.set_timeout(I2C_TIMEOUT)
    except Exception as e:
        print (e)
        deinit_i2c(i2c)
        return None

    return i2c


def init_uart():
    uart = None
    try:
        uart = serial.Serial(PORT_INAV,
                             BAUDRATE_INAV,
                             timeout=TIMEOUT_INAV)
    except Exception as e:
        print (e)
        deinit_uart(uart)
        return None

    if not (uart.isOpen()):
        deinit_uart(uart)
        return None

    return uart


def init_internet():
    try:
        os.system(r'./internet_on.sh')
    except Exception as e:
        print (e)
        pass


# ================================================================
# Actions
# ================================================================
def hide_none(buf):
    for i in range(len(buf)):
        if buf[i] is None:
            buf[i] = 0
    return buf


def pack_data(buf):
    try:
        data = struct.pack(FORMAT, *buf)
    except Exception as e:
        print (e)
        return None
    return data
