import serial
import dearpygui.dearpygui as dearpygui


def save_callback(sender, data):
    print("Save clicked")


vriskerPort = "COM13"

class UartCom:
    def __init__(self, port=vriskerPort):
        self.port = port
        self.serialport = None

    def connect(self):
        self.port = str(dearpygui.get_value('##uart_input'))
        self.serialport = serial.Serial(self.port, 115000, timeout=4)

    def disconnect(self):
        if self.serialport is not None:
            self.serialport.close()
    def stop(self):
        self.serialport.write(b'v0 0\n')

    def move(self):
        self.serialport.write(b'v4 8\n')

    def test_left(self):
        self.serialport.write(b'v0 8\n')

    def test_right(self):
        self.serialport.write(b'v8 0\n')

    def reset(self):
        self.serialport.write(b'R\n')





if __name__ == '__main__':
    dearpygui.set_global_font_scale(1.8)
    vrisker_com = UartCom()
    with dearpygui.window(label="Vrisker controll!", width=1400, height=800):
        dearpygui.add_button(callback=vrisker_com.connect, label="connect")
        dearpygui.add_button(callback=vrisker_com.disconnect, label="disconnect")
        dearpygui.add_input_text(id="##uart_input", width=100, default_value=vriskerPort)
        dearpygui.add_button(callback=vrisker_com.stop, label="stop")
        dearpygui.add_button(callback=vrisker_com.test_left, label="test left")
        dearpygui.add_button(callback=vrisker_com.test_right, label="test right")
        dearpygui.add_button(callback=vrisker_com.move, label="run")
        dearpygui.add_button(callback=vrisker_com.reset, label="reset")
    dearpygui.show_documentation()
    dearpygui.start_dearpygui()
    vrisker_com.disconnect()
