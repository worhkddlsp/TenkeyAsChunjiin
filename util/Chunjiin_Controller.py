import time
import pynput

from util.Chunjiin_util import Chunjiin_Util, Hangle
from config.constant import tenkey_num_code_list, tenkey_num_code_dict

class Chunjiin_Controller :
    CONST_SERIAL_CHECK_TIME = 0.7

    def __init__(self
                 , numpad_press_listener = None
                 , numpad_release_listener = None
                 , hangle_listener = None):
        self.numpad_press_listener = numpad_press_listener
        self.numpad_release_listener = numpad_release_listener
        self.hangle_listener = hangle_listener

        self.__init_param()
        self.listener = None

    def __init_param(self):
        self.before_han = Hangle()
        self.current_han = Hangle()
        self.__call_hangle_listener()

        self.__last_press_keycode = 0
        self.__last_press_time = 0.0

    def start(self):
        print(f'Chunjiin_Controller start.')
        if self.listener is None :
            self.listener = pynput.keyboard.Listener(
                on_press=self.__on_press
                , on_release=self.__on_release
                , win32_event_filter=self.__numpad_evnet_filter
                , suppress=False
            )

        self.listener.start()


    def start_stand_alone(self):
        self.start()
        self.listener.join()

    def stop(self):
        print(f'Chunjiin_Controller stop.')
        self.__init_param()
        self.listener.stop()
        self.listener = None

    def reset(self):
        print(f'Chunjiin_Controller config and buffer reset.')
        self.__init_param()

    # param : msg, data{dwExtraInfo, flags, scanCode, time, vkCode}
    def __numpad_evnet_filter(self, msg, data):
        if data.vkCode in tenkey_num_code_list:
            self.listener._suppress = True
        elif data.vkCode == 110:
            self.listener._suppress = True
        else:
            self.listener._suppress = False
        return True

    def __call_numpad_press_listener(self,vk_code):
        if self.numpad_press_listener != None :
            self.numpad_press_listener(vk_code)

    def __call_hangle_listener(self):
        if self.hangle_listener != None :
            self.hangle_listener(self.before_han.get_word(), self.current_han.get_word())

    def __on_press(self, key):
        keyCode = None
        if isinstance(key, pynput.keyboard.Key):
            if key in [
                pynput.keyboard.Key.space
                , pynput.keyboard.Key.enter
                , pynput.keyboard.Key.esc
            ]:
                self.reset()
            keyCode = key.value
        else: keyCode = key


        if keyCode.vk in tenkey_num_code_list:
            self.__call_numpad_press_listener(keyCode.vk)
            self.__proccess_numpad(keyCode.vk)
        else :
            if keyCode.char in [',', '.', '\'', '"', ':', '-']:
                self.reset()
            if keyCode.vk == 110:
                Chunjiin_Util.exe_press_and_release(' ')


    def __call_numpad_release_listener(self, vk_code):
        if self.numpad_release_listener != None :
            self.numpad_release_listener(vk_code)

    def __on_release(self, key):
        keyCode = None
        if isinstance(key, pynput.keyboard.Key):
            keyCode = key.value
        else: keyCode = key

        if keyCode.vk in tenkey_num_code_list:
            self.__call_numpad_release_listener(keyCode.vk)

    def __reset_current_hangel(self):
        self.before_han = Hangle(clone=self.current_han)
        self.current_han.init()
        self.__call_hangle_listener()

    def __proccess_numpad(self, vk_code):
        current_press_time = time.time()
        time_since_last_press = current_press_time - self.__last_press_time

        if 96 <= vk_code and vk_code <= 102 :
            if time_since_last_press < Chunjiin_Controller.CONST_SERIAL_CHECK_TIME and self.__last_press_keycode == vk_code :
                self.__process_jaum_double_tap(vk_code, current_press_time)
                return
            self.__process_jaum_tap(vk_code, current_press_time)
        else :
            self.__process_moum_tap(vk_code, current_press_time)

    def __process_jaum_tap(self, vk_code, current_press_time):
        chunjiin_word = tenkey_num_code_dict[vk_code]['cji'][0]
        if self.current_han.step == Hangle.EMPTY:
            self.current_han.set_cho(chunjiin_word)
            self.__call_hangle_listener()
            Chunjiin_Util.exe_press_and_release(self.current_han.get_word())
        elif self.current_han.step == Hangle.EXIST_JUNG:
            Chunjiin_Util.exe_backspace(1)
            self.current_han.set_jong(chunjiin_word)
            self.__call_hangle_listener()
            Chunjiin_Util.exe_press_and_release(self.current_han.get_word())
        elif self.current_han.step == Hangle.EXIST_JONG and self.current_han.check_and_set_double_jong(chunjiin_word):
            Chunjiin_Util.exe_backspace(1)
            Chunjiin_Util.exe_press_and_release(self.current_han.get_word())
            self.__call_hangle_listener()
        else:
            self.__reset_current_hangel()
            self.current_han.set_cho(chunjiin_word)
            self.__call_hangle_listener()
            Chunjiin_Util.exe_press_and_release(self.current_han.get_word())

        self.__last_press_keycode = vk_code
        self.__last_press_time = current_press_time


    def __process_moum_tap(self, vk_code, current_press_time):
        chunjiin_word = tenkey_num_code_dict[vk_code]['cji'][0]
        if self.current_han.step == Hangle.EMPTY :
            self.current_han.set_cho(chunjiin_word)
            self.__call_hangle_listener()
            Chunjiin_Util.exe_press_and_release(self.current_han.get_word())
            self.__reset_current_hangel()
        elif self.current_han.step == Hangle.EXIST_CHO :
            Chunjiin_Util.exe_backspace(1)
            self.current_han.set_jung(chunjiin_word)
            self.__call_hangle_listener()
            Chunjiin_Util.exe_press_and_release(self.current_han.get_word())
        elif self.current_han.step == Hangle.EXIST_JUNG :
            moum_convert_word = Chunjiin_Util.get_next_word_for_moum(self.current_han.get_jung(), chunjiin_word)
            if chunjiin_word == moum_convert_word :
                self.__reset_current_hangel()
                self.current_han.set_jung(chunjiin_word)
                self.__call_hangle_listener()
                Chunjiin_Util.exe_press_and_release(self.current_han.get_word())
                self.__last_press_keycode = vk_code
                self.__last_press_time = current_press_time
                return

            if self.current_han.get_cho() != '' and self.current_han.get_jung() in ['ㆍ','‥']:
                Chunjiin_Util.exe_backspace(2)
            else:
                Chunjiin_Util.exe_backspace(1)

            self.current_han.set_jung(moum_convert_word)
            self.__call_hangle_listener()
            Chunjiin_Util.exe_press_and_release(self.current_han.get_word())

        elif self.current_han.step in [Hangle.EXIST_JONG, Hangle.EXIST_DOUBLE_JONG] :
            Chunjiin_Util.exe_backspace(1)
            jong_sung = self.current_han.pop()
            self.__reset_current_hangel()
            self.current_han.set_cho(jong_sung)
            self.current_han.set_jung(chunjiin_word)
            self.__call_hangle_listener()
            Chunjiin_Util.exe_press_and_release(self.before_han.get_word())
            Chunjiin_Util.exe_press_and_release(self.current_han.get_word())
        else:
            self.__reset_current_hangel()
            self.current_han.set_jung(chunjiin_word)
            self.__call_hangle_listener()
            Chunjiin_Util.exe_press_and_release(self.current_han.get_word())


        self.__last_press_keycode = vk_code
        self.__last_press_time = current_press_time

    def __process_jaum_double_tap(self, vk_code, current_press_time):
        if self.current_han.step == Hangle.EMPTY and self.before_han.EXIST_DOUBLE_JONG:
            last_word = self.before_han.pop()
            before_chunjiin_word_idx = tenkey_num_code_dict[vk_code]['cji'].index(last_word)
            if before_chunjiin_word_idx == len(tenkey_num_code_dict[vk_code]['cji']) - 1 :
                before_chunjiin_word_idx = -1
            chunjiin_word = tenkey_num_code_dict[vk_code]['cji'][before_chunjiin_word_idx+1]
            self.current_han.set_cho(chunjiin_word)
            self.__call_hangle_listener()
            Chunjiin_Util.exe_backspace(1)
            Chunjiin_Util.exe_press_and_release(self.before_han.get_word())
            Chunjiin_Util.exe_press_and_release(self.current_han.get_word())

        elif self.current_han.step == Hangle.EXIST_CHO :
            before_chunjiin_word_idx = tenkey_num_code_dict[vk_code]['cji'].index(self.current_han.get_cho())
            if before_chunjiin_word_idx == len(tenkey_num_code_dict[vk_code]['cji']) - 1 :
                before_chunjiin_word_idx = -1
            chunjiin_word = tenkey_num_code_dict[vk_code]['cji'][before_chunjiin_word_idx+1]

            if self.before_han.step == Hangle.EXIST_JONG and self.before_han.check_and_set_double_jong(chunjiin_word):
                Chunjiin_Util.exe_backspace(2)
                self.current_han.init()
                self.__call_hangle_listener()
                Chunjiin_Util.exe_press_and_release(self.before_han.get_word())
            else :
                Chunjiin_Util.exe_backspace(1)
                self.current_han.set_cho(chunjiin_word)
                self.__call_hangle_listener()
                Chunjiin_Util.exe_press_and_release(self.current_han.get_word())
        elif self.current_han.step == Hangle.EXIST_JONG:
            before_chunjiin_word_idx = tenkey_num_code_dict[vk_code]['cji'].index(self.current_han.get_jong())
            if before_chunjiin_word_idx == len(tenkey_num_code_dict[vk_code]['cji']) - 1 :
                before_chunjiin_word_idx = -1
            chunjiin_word = tenkey_num_code_dict[vk_code]['cji'][before_chunjiin_word_idx+1]

            Chunjiin_Util.exe_backspace(1)
            self.current_han.set_jong(chunjiin_word)
            self.__call_hangle_listener()
            Chunjiin_Util.exe_press_and_release(self.current_han.get_word())
        elif self.current_han.step == Hangle.EXIST_DOUBLE_JONG:
            double_jong_last_obj = self.current_han.pop_doble_jong()
            before_chunjiin_word_idx = tenkey_num_code_dict[vk_code]['cji'].index(double_jong_last_obj)
            if before_chunjiin_word_idx == len(tenkey_num_code_dict[vk_code]['cji']) - 1 :
                before_chunjiin_word_idx = -1
            chunjiin_word = tenkey_num_code_dict[vk_code]['cji'][before_chunjiin_word_idx+1]

            Chunjiin_Util.exe_backspace(1)
            self.__reset_current_hangel()
            self.current_han.set_cho(chunjiin_word)
            self.__call_hangle_listener()
            Chunjiin_Util.exe_press_and_release(self.before_han.get_word())
            Chunjiin_Util.exe_press_and_release(self.current_han.get_word())
        else:
            print(f'__process_jaum_double_tap - 예상못한 케이스!!!!!!!')

        self.__last_press_keycode = vk_code
        self.__last_press_time = current_press_time

    def __process_moum_double_tap(self):
        print('moum double tap')

if __name__ == "__main__":
    controller = Chunjiin_Controller()
    controller.start_stand_alone()

