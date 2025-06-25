import fonts

import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.properties import BooleanProperty
from kivy.utils import get_color_from_hex
from kivy.clock import Clock
import threading

from utils import prime_count

kivy.require("2.0.0")


class Calculator(App):
    clear_bool = BooleanProperty(False)

    def print_number(self, number):
        if self.clear_bool:
            self.clear_display()
        self.root.ids.display.text += str(number)

    def print_operator(self, operator):
        if self.clear_bool:
            self.clear_bool = False
        self.root.ids.display.text += operator

    def clear_display(self):
        self.root.ids.display.text = ""
        self.clear_bool = False

    def del_char(self):
        self.root.ids.display.text = self.root.ids.display.text[:-1]

    def _safe_eval(self, expr: str) -> str:
        try:
            return str(eval(expr))
        except Exception:
            return "エラー"

    def run_with_timeout(self, func, timeout_seconds=3):
        result_holder = {}
        thread = threading.Thread(
            target=lambda: self._execute_task(func, result_holder), daemon=True
        )
        thread.start()

        def check_result(dt):
            if not thread.is_alive():
                Clock.unschedule(check_result)
                Clock.unschedule(timeout_event)
                text = result_holder.get("result", "エラー")
                self._update_display(text)

        def on_timeout(dt):
            if thread.is_alive():
                Clock.unschedule(check_result)
                self._update_display("タイムアウトです。")

        Clock.schedule_interval(check_result, 0.1)
        timeout_event = Clock.schedule_once(on_timeout, timeout_seconds)

    def _execute_task(self, func, result_holder):
        try:
            result_holder["result"] = func()
        except Exception:
            result_holder["result"] = "エラー"

    def calculate(self):
        expr = self.root.ids.display.text
        self.run_with_timeout(lambda: self._safe_eval(expr))

    def code_change(self):
        expr = self.root.ids.display.text
        self.run_with_timeout(lambda: self._safe_eval(f"{expr}*-1"))

    def exponential_notation(self):
        try:
            val = eval(self.root.ids.display.text)
            self._update_display(f"{val:e}")
        except Exception:
            self._update_display("エラー")

    def prime_judge(self):
        expr = self.root.ids.display.text
        self.run_with_timeout(lambda: prime_count(int(expr)))

    def _update_display(self, text):
        self.root.ids.display.text = text
        self.clear_bool = True


if __name__ == "__main__":
    Window.clearcolor = get_color_from_hex("#FFFFFF")
    Calculator().run()
