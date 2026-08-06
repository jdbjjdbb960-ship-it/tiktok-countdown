from kivy.app import App
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from jnius import autoclass

# GANTI DENGAN LINK VIDEO TIKTOK KAMU
TIKTOK_URL = "https://vt.tiktok.com/ZS49v92c3/"


class CountdownApp(App):

    def build(self):
        self.count = 3

        self.label = Label(
            text="3",
            font_size="100sp"
        )

        layout = BoxLayout(
            orientation="vertical"
        )

        layout.add_widget(self.label)

        Clock.schedule_interval(self.countdown, 1)

        return layout

    def countdown(self, dt):
        if self.count > 0:
            self.label.text = str(self.count)
            self.count -= 1
        else:
            Clock.unschedule(self.countdown)
            self.label.text = "Membuka TikTok..."
            self.open_tiktok()

    def open_tiktok(self):
        PythonActivity = autoclass(
            "org.kivy.android.PythonActivity"
        )

        Intent = autoclass(
            "android.content.Intent"
        )

        Uri = autoclass(
            "android.net.Uri"
        )

        intent = Intent(
            Intent.ACTION_VIEW,
            Uri.parse(TIKTOK_URL)
        )

        PythonActivity.mActivity.startActivity(intent)


if __name__ == "__main__":
    CountdownApp().run()
