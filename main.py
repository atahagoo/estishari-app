from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import joblib

model_diabetes = joblib.load('diabetes_model.pkl')
model_bp = joblib.load('heart_model.pkl')

ADVICE = {"diabetes_high": "سكري مرتفع", "normal": "طبيعي"}
class MainScreen(Screen): pass
class DiabetesScreen(Screen):
    def diagnose(self):
        try:
            glucose = float(self.ids.glucose.text or 0)
            pred = model_diabetes.predict([[6, glucose, 70, 20, 80, 25, 0.5, 33]])[0]
            self.ids.result.text = "مرتفع" if pred == 1 else "طبيعي"
        except: self.ids.result.text = "ادخل ارقام"
class BPScreen(Screen): pass
class EstishariApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(DiabetesScreen(name='diabetes'))
        sm.add_widget(BPScreen(name='bp'))
        return Builder.load_file('estishari.kv')
if __name__ == '__main__': EstishariApp().run()
