import tkinter
from util.Chunjiin_Controller import Chunjiin_Controller
from util.Chunjiin_util import Chunjiin_Util


class Chunjiin_GUI_Controller:
    APP_TITLE = 'TenkeyAsChunjiin'

    WIDTH = 300
    HEIGHT = 360

    CHUNJIIN_OFF = 0
    CHUNJIIN_ON = 1

    def __init__(self):
        self.current_mode = Chunjiin_GUI_Controller.CHUNJIIN_OFF

        self.root = tkinter.Tk()
        self.__init_gui()
        self.__init_chunjiin_controller()

    def __init_gui(self):
        self.root.geometry(f'{Chunjiin_GUI_Controller.WIDTH}x{Chunjiin_GUI_Controller.HEIGHT}')
        self.root.title(Chunjiin_GUI_Controller.APP_TITLE)

        self.hangle_frame = tkinter.Frame(self.root)
        self.before_han_label_title = tkinter.Label(self.hangle_frame, text='이전문자:')
        self.before_han_label = tkinter.Label(self.hangle_frame, text='[ ]')
        self.current_han_label_title = tkinter.Label(self.hangle_frame, text='현재문자:')
        self.current_han_label = tkinter.Label(self.hangle_frame, text='[ ]')
        #self.buffer_title_label = tkinter.Label(self.root, text='======== 최근 입력 ========')
        #self.buffer_label = tkinter.Label(self.root, text='[]')
        self.hangle_frame.grid(row=1, column=0)
        self.before_han_label_title.grid(row=0, column=0, padx=2, pady=2)
        self.before_han_label.grid(row=0, column=1, padx=2, pady=2)
        self.current_han_label_title.grid(row=0, column=2, padx=2, pady=2)
        self.current_han_label.grid(row=0, column=3, padx=2, pady=2)
        #self.buffer_title_label.grid(row=1, column=0)
        #self.buffer_label.grid(row=2, column=0)

        self.config_frame = tkinter.Frame(self.root)
        self.chunjiin_on_off_label = tkinter.Label( self.config_frame, text='TenKey 천지인 사용 :')
        self.chunjiin_on_off_btn = tkinter.Button(self.config_frame, text='OFF', command=self.on_click_chunjiin_on_off_btn)
        self.config_frame.grid(row=0, column=0)
        self.chunjiin_on_off_label.grid(row=0, column=0)
        self.chunjiin_on_off_btn.grid(row=0, column=1)


        self.numpad_frame = tkinter.Frame(self.root,relief='solid', borderwidth=1)
        self.label7 = tkinter.Label(self.numpad_frame, text='7\nㅣ', width=7, height=2, relief='solid', borderwidth=1)
        self.label8 = tkinter.Label(self.numpad_frame, text='8\nㆍ', width=7, height=2, relief='solid', borderwidth=1)
        self.label9 = tkinter.Label(self.numpad_frame, text='9\nㅡ', width=7, height=2, relief='solid', borderwidth=1)
        self.label4 = tkinter.Label(self.numpad_frame, text='4\nㄱㅋ', width=7, height=2, relief='solid', borderwidth=1)
        self.label5 = tkinter.Label(self.numpad_frame, text='5\nㄴㄹ', width=7, height=2, relief='solid', borderwidth=1)
        self.label6 = tkinter.Label(self.numpad_frame, text='6\nㄷㅌ', width=7, height=2, relief='solid', borderwidth=1)
        self.label1 = tkinter.Label(self.numpad_frame, text='1\nㅂㅍ', width=7, height=2, relief='solid', borderwidth=1)
        self.label2 = tkinter.Label(self.numpad_frame, text='2\nㅅㅎ', width=7, height=2, relief='solid', borderwidth=1)
        self.label3 = tkinter.Label(self.numpad_frame, text='3\nㅈㅊ', width=7, height=2, relief='solid', borderwidth=1)
        self.label0 = tkinter.Label(self.numpad_frame, text='0\nㅇㅁ', width=7, height=2, relief='solid', borderwidth=1)
        self.label_period = tkinter.Label(self.numpad_frame, text='.\nspace', width=7, height=2, relief='solid', borderwidth=1)

        self.numpad_frame.place(x=30,y=100,anchor='nw')
        self.label7.grid(row=0, column=0, padx=1, pady=1)
        self.label8.grid(row=0, column=1, padx=1, pady=1)
        self.label9.grid(row=0, column=2, padx=1, pady=1)
        self.label4.grid(row=1, column=0, padx=1, pady=1)
        self.label5.grid(row=1, column=1, padx=1, pady=1)
        self.label6.grid(row=1, column=2, padx=1, pady=1)
        self.label1.grid(row=2, column=0, padx=1, pady=1)
        self.label2.grid(row=2, column=1, padx=1, pady=1)
        self.label3.grid(row=2, column=2, padx=1, pady=1)
        self.label0.grid(row=3, column=1, padx=1, pady=1)
        self.label_period.grid(row=3, column=2, padx=1, pady=1)

        #self.test_btn = tkinter.Button(self.root, text='test_bnt', command= self.test)
        #self.test_btn.grid(row=0, column=1)

    def __init_chunjiin_controller(self):
        self.chunjiin_controller = Chunjiin_Controller(
            numpad_press_callback = self.numpad_press_callback
            , numpad_release_callback = self.numpad_release_callback
            , hangle_callback = self.hangle_callback
            , on_off_callback= self.on_off_callback
            )

    def run(self):
        self.chunjiin_controller_start()
        self.root.mainloop()

    def on_click_chunjiin_on_off_btn(self):
        if self.current_mode == Chunjiin_GUI_Controller.CHUNJIIN_OFF:
            self.chunjiin_controller_start()
        else:
            self.chunjiin_controller_stop()

    def chunjiin_controller_start(self):
        self.current_mode = Chunjiin_GUI_Controller.CHUNJIIN_ON
        self.chunjiin_on_off_btn.config(text='ON', bg='blue')
        self.chunjiin_controller.start()

    def chunjiin_controller_stop(self):
        self.current_mode = Chunjiin_GUI_Controller.CHUNJIIN_OFF
        self.chunjiin_on_off_btn.config(text='OFF', bg='SystemButtonFace')
        self.chunjiin_controller.stop()

    def on_off_callback(self):
        self.on_click_chunjiin_on_off_btn()

    def hangle_callback(self, before_han, current_han):
        if before_han == '':
            self.before_han_label.config(text='[ ]')
        else:
            self.before_han_label.config(text=f'[{before_han}]')

        if current_han == '':
            self.current_han_label.config(text='[ ]')
        else :
            self.current_han_label.config(text=f'[{current_han}]')

    def numpad_press_callback(self, vk_code):
        if vk_code == 96:
            self.label0.config(bg="gray")
        elif vk_code == 97:
            self.label1.config(bg="gray")
        elif vk_code == 98:
            self.label2.config(bg="gray")
        elif vk_code == 99:
            self.label3.config(bg="gray")
        elif vk_code == 100:
            self.label4.config(bg="gray")
        elif vk_code == 101:
            self.label5.config(bg="gray")
        elif vk_code == 102:
            self.label6.config(bg="gray")
        elif vk_code == 103:
            self.label7.config(bg="gray")
        elif vk_code == 104:
            self.label8.config(bg="gray")
        elif vk_code == 105:
            self.label9.config(bg="gray")
        elif vk_code == 110:
            self.label_period.config(bg="gray")

    def numpad_release_callback(self, vk_code):
        if vk_code == 96:
            self.label0.config(bg="SystemButtonFace")
        elif vk_code == 97:
            self.label1.config(bg="SystemButtonFace")
        elif vk_code == 98:
            self.label2.config(bg="SystemButtonFace")
        elif vk_code == 99:
            self.label3.config(bg="SystemButtonFace")
        elif vk_code == 100:
            self.label4.config(bg="SystemButtonFace")
        elif vk_code == 101:
            self.label5.config(bg="SystemButtonFace")
        elif vk_code == 102:
            self.label6.config(bg="SystemButtonFace")
        elif vk_code == 103:
            self.label7.config(bg="SystemButtonFace")
        elif vk_code == 104:
            self.label8.config(bg="SystemButtonFace")
        elif vk_code == 105:
            self.label9.config(bg="SystemButtonFace")
        elif vk_code == 110:
            self.label_period.config(bg="SystemButtonFace")

    def test(self):
        Chunjiin_Util.exe_press_and_release('ㄴ')


if __name__ == "__main__":
    gui_controller = Chunjiin_GUI_Controller()
    gui_controller.run()