import jamo
import pynput
import pyautogui

CHOSUNG = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
JUNGSUNG = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
JONGSUNG = ['ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ','ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

class Chunjiin_Util:
    CONTROLLER = pynput.keyboard.Controller()
    def __init__(self):
        pass

    @staticmethod
    def exe_press_and_release(word_list):
        for word in word_list:
            Chunjiin_Util.CONTROLLER.press(word)
            Chunjiin_Util.CONTROLLER.release(word)

    @staticmethod
    def exe_backspace(idx):
        for i in range(idx):
            Chunjiin_Util.CONTROLLER.press(pynput.keyboard.Key.backspace)
            Chunjiin_Util.CONTROLLER.release(pynput.keyboard.Key.backspace)

    @staticmethod
    def pyautogui_convert_release(word):
        if word == 'ㄱ': pyautogui.write('r')
        elif word == 'ㄲ': pyautogui.write('R')
        elif word == 'ㄴ': pyautogui.write('s')
        elif word == 'ㄷ': pyautogui.write('e')
        elif word == 'ㄸ': pyautogui.write('E')
        elif word == 'ㄹ': pyautogui.write('f')
        elif word == 'ㅁ': pyautogui.write('a')
        elif word == 'ㅂ': pyautogui.write('q')
        elif word == 'ㅃ': pyautogui.write('Q')
        elif word == 'ㅅ': pyautogui.write('t')
        elif word == 'ㅆ': pyautogui.write('T')
        elif word == 'ㅇ': pyautogui.write('d')
        elif word == 'ㅈ': pyautogui.write('w')
        elif word == 'ㅉ': pyautogui.write('W')
        elif word == 'ㅊ': pyautogui.write('c')
        elif word == 'ㅋ': pyautogui.write('z')
        elif word == 'ㅌ': pyautogui.write('x')
        elif word == 'ㅍ': pyautogui.write('v')
        elif word == 'ㅎ': pyautogui.write('g')
        elif word == 'ㅏ': pyautogui.write('k')
        elif word == 'ㅐ': pyautogui.write('o')
        elif word == 'ㅑ': pyautogui.write('i')
        elif word == 'ㅒ': pyautogui.write('O')
        elif word == 'ㅓ': pyautogui.write('j')
        elif word == 'ㅔ': pyautogui.write('p')
        elif word == 'ㅕ': pyautogui.write('u')
        elif word == 'ㅖ': pyautogui.write('P')
        elif word == 'ㅗ': pyautogui.write('h')
        elif word == 'ㅘ': pyautogui.write('hk')
        elif word == 'ㅙ': pyautogui.write('ho')
        elif word == 'ㅚ': pyautogui.write('hl')
        elif word == 'ㅛ': pyautogui.write('y')
        elif word == 'ㅜ': pyautogui.write('n')
        elif word == 'ㅝ': pyautogui.write('nj')
        elif word == 'ㅞ': pyautogui.write('np')
        elif word == 'ㅟ': pyautogui.write('nl')
        elif word == 'ㅠ': pyautogui.write('b')
        elif word == 'ㅡ': pyautogui.write('m')
        elif word == 'ㅢ': pyautogui.write('ml')
        elif word == 'ㅣ': pyautogui.write('l')
        elif word == 'ㄶ': pyautogui.write('sg') #
        elif word == 'ㅀ': pyautogui.write('fg') #
        elif word == 'ㄼ': pyautogui.write('fq')
        elif word == 'ㄽ': pyautogui.write('ft')
        elif word == 'ㄵ': pyautogui.write('sw')
        elif word == 'ㄿ': pyautogui.write('fv') #
        elif word == 'ㄺ': pyautogui.write('fr')
        elif word == 'ㅄ': pyautogui.write('qt')
        elif word == 'ㄻ': pyautogui.write('fa') #
        elif word == 'ㄾ': pyautogui.write('fx') #
        elif word == 'ㄳ': pyautogui.write('rt')
        elif word == 'ㆍ': Chunjiin_Util.exe_press_and_release('ㆍ')
        elif word == '‥' : Chunjiin_Util.exe_press_and_release('‥')
        else: pass

    @staticmethod
    def get_next_word_for_moum(before_word, current_word):
        if current_word == 'ㆍ':
            return Chunjiin_Util.get_next_word_for_moum_midle(before_word)
        elif current_word == 'ㅣ':
            return Chunjiin_Util.get_next_word_for_moum_ei(before_word)
        elif current_word == 'ㅡ':
            return Chunjiin_Util.get_next_word_for_moum_eu(before_word)
        else :
            return current_word

    @staticmethod
    def get_next_word_for_moum_midle(before_word):
        if before_word == 'ㆍ' :
            return '‥'
        elif before_word == 'ㅣ':
            return 'ㅏ'
        elif before_word == 'ㅏ':
            return 'ㅑ'
        elif before_word == 'ㅡ':
            return 'ㅜ'
        elif before_word == 'ㅜ':
            return 'ㅠ'
        elif before_word == 'ㅚ':
            return 'ㅘ'
        elif before_word == 'ㅟ':
            return 'ㅘ'
        else:
            return 'ㆍ'

    @staticmethod
    def get_next_word_for_moum_ei(before_word):
        if before_word == 'ㆍ':
            return 'ㅓ'
        elif before_word == 'ㅓ':
            return 'ㅔ'
        elif before_word == '‥':
            return 'ㅕ'
        elif before_word == 'ㅡ':
            return 'ㅢ'
        elif before_word == 'ㅗ':
            return 'ㅚ'
        elif before_word == 'ㅜ':
            return 'ㅟ'
        elif before_word == 'ㅏ':
            return 'ㅐ'
        elif before_word == 'ㅑ':
            return 'ㅒ'
        elif before_word == 'ㅕ':
            return 'ㅖ'
        elif before_word == 'ㅠ':
            return 'ㅝ'
        elif before_word == 'ㅝ':
            return 'ㅞ'
        elif before_word == 'ㅘ':
            return 'ㅙ'
        else:
            return 'ㅣ'

    @staticmethod
    def get_next_word_for_moum_eu(before_word):
        if before_word == 'ㆍ':
            return 'ㅗ'
        elif before_word == '‥':
            return 'ㅛ'
        else:
            return 'ㅡ'

class Hangle:
    EXIST_ONLY_JUNG = -1
    EMPTY = 0
    EXIST_CHO = 1
    EXIST_JUNG = 2
    EXIST_JONG = 3
    EXIST_DOUBLE_JONG = 4

    CHO_IDX = 0
    JUNG_IDX = 1
    JONG_IDX = 2

    def __init__(self, clone=None):
        if clone == None :
            self.init()
        else:
            self.step = clone.step
            self.cho = clone.get_cho()
            self.jung = clone.get_jung()
            self.jong = clone.get_jong()

    def init(self):
        self.step = Hangle.EMPTY

        self.cho = ''
        self.jung = ''
        self.jong = ''

    def get_cho(self):
        return self.cho

    def get_jung(self):
        return self.jung

    def get_jong(self):
        return self.jong

    def set_cho(self, word):
        self.step = Hangle.EXIST_CHO
        self.cho = word

    def set_jung(self, word):
        if self.get_cho() == '':
            self.step = Hangle.EXIST_ONLY_JUNG
        else:
            self.step = Hangle.EXIST_JUNG
        self.jung = word

    def set_jong(self, word):
        self.step = Hangle.EXIST_JONG
        self.jong = word

    def pop(self):
        if self.step == Hangle.EXIST_CHO:
            self.step = Hangle.EMPTY
            cho = self.cho
            self.cho = ''
            return cho
        elif self.step == Hangle.EXIST_JUNG:
            self.step = Hangle.EXIST_CHO
            jung = self.jung
            self.jung = ''
            return jung
        elif self.step == Hangle.EXIST_JONG:
            self.step = Hangle.EXIST_JUNG
            jong = self.jong
            self.jong = ''
            return jong
        elif self.step == Hangle.EXIST_DOUBLE_JONG:
            return self.pop_doble_jong()
        else:
            return None

    def pop_doble_jong(self):
        if self.step != Hangle.EXIST_DOUBLE_JONG:return None
        jong_sung = self.get_jong()
        if jong_sung == 'ㄶ' :
            self.step = Hangle.EXIST_JONG
            self.set_jong('ㄴ')
            return 'ㅎ'
        elif jong_sung == 'ㅀ':
            self.step = Hangle.EXIST_JONG
            self.set_jong('ㄹ')
            return 'ㅎ'
        elif jong_sung == 'ㄼ':
            self.step = Hangle.EXIST_JONG
            self.set_jong('ㄹ')
            return 'ㅂ'
        elif jong_sung == 'ㄽ':
            self.step = Hangle.EXIST_JONG
            self.set_jong('ㄹ')
            return 'ㅅ'
        elif jong_sung == 'ㄵ':
            self.step = Hangle.EXIST_JONG
            self.set_jong('ㄴ')
            return 'ㅈ'
        elif jong_sung == 'ㄿ':
            self.step = Hangle.EXIST_JONG
            self.set_jong('ㄹ')
            return 'ㅍ'
        elif jong_sung == 'ㄺ':
            self.step = Hangle.EXIST_JONG
            self.set_jong('ㄹ')
            return 'ㄱ'
        elif jong_sung == 'ㅄ':
            self.step = Hangle.EXIST_JONG
            self.set_jong('ㅂ')
            return 'ㅅ'
        elif jong_sung == 'ㄻ':
            self.step = Hangle.EXIST_JONG
            self.set_jong('ㄹ')
            return 'ㅁ'
        elif jong_sung == 'ㄾ':
            self.step = Hangle.EXIST_JONG
            self.set_jong('ㅌ')
            return 'ㅌ'
        elif jong_sung == 'ㄳ':
            self.step = Hangle.EXIST_JONG
            self.set_jong('ㄱ')
            return 'ㅅ'
        else:
            return None

    def get_word(self):
        try:
            if self.step < Hangle.EXIST_JUNG or self.get_jung() not in JUNGSUNG:
                return ''.join(list([self.get_cho(),self.get_jung(),self.get_jong()]))
            word = jamo.j2h(self.get_cho(), self.get_jung(), self.get_jong())
            return word
        except Exception as e:
            print(f'get_word Error. exception:{e}')
            return ''.join(list([self.get_cho(),self.get_jung(),self.get_jong()]))

    def check_and_set_double_jong(self,word):
        if self.step != Hangle.EXIST_JONG : return False
        if self.get_jong() == 'ㄴ' and word == 'ㅎ':
            self.set_jong('ㄶ')
            self.step = Hangle.EXIST_DOUBLE_JONG
            return True
        elif self.get_jong() == 'ㄹ' and word == 'ㅎ':
            self.set_jong('ㅀ')
            self.step = Hangle.EXIST_DOUBLE_JONG
            return True
        elif self.get_jong() == 'ㄹ' and word == 'ㅎ':
            self.set_jong('ㅀ')
            self.step = Hangle.EXIST_DOUBLE_JONG
            return True
        elif self.get_jong() == 'ㄹ' and word == 'ㅂ':
            self.set_jong('ㄼ')
            self.step = Hangle.EXIST_DOUBLE_JONG
            return True
        elif self.get_jong() == 'ㄹ' and word == 'ㅅ':
            self.set_jong('ㄽ')
            self.step = Hangle.EXIST_DOUBLE_JONG
            return True
        elif self.get_jong() == 'ㄴ' and word == 'ㅈ':
            self.set_jong('ㄵ')
            self.step = Hangle.EXIST_DOUBLE_JONG
            return True
        elif self.get_jong() == 'ㄹ' and word == 'ㅍ':
            self.set_jong('ㄿ')
            self.step = Hangle.EXIST_DOUBLE_JONG
            return True
        elif self.get_jong() == 'ㄹ' and word == 'ㄱ':
            self.set_jong('ㄺ')
            self.step = Hangle.EXIST_DOUBLE_JONG
            return True
        elif self.get_jong() == 'ㅂ' and word == 'ㅅ':
            self.set_jong('ㅄ')
            self.step = Hangle.EXIST_DOUBLE_JONG
            return True
        elif self.get_jong() == 'ㄹ' and word == 'ㅁ':
            self.set_jong('ㄻ')
            self.step = Hangle.EXIST_DOUBLE_JONG
            return True
        elif self.get_jong() == 'ㄹ' and word == 'ㅌ':
            self.set_jong('ㄾ')
            self.step = Hangle.EXIST_DOUBLE_JONG
            return True
        else:
            return False

if __name__ == "__main__":
    hangle = Hangle()
    print(hangle.get_word())