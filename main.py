import threading
from gtts import gTTS
import os
import playsound
import speech_recognition as sr
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import tkinter.ttk
from tkinter import *
from tkinter import messagebox
from pystray import MenuItem as item
import pystray
from PIL import Image


class MainWindow(tkinter.ttk.Frame):
    def __init__(self, container, width=411, height=388):
        super().__init__(container, width=width, height=height)

        self.canvas = Canvas(
            window,
            bg="#ffffff",
            height=569,
            width=411,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        self.canvas.place(x=0, y=0)

        self.background_img = PhotoImage(file=f"main_screen/background.png")
        self.canvas.create_image(
            205.0, 288.5,
            image=self.background_img)

        self.settings_image = PhotoImage(file=f"main_screen/img0.png")
        self.settings_button = Button(
            image=self.settings_image,
            borderwidth=0,
            highlightthickness=0,
            relief="flat")

        self.settings_button.place(
            x=62, y=385,
            width=286,
            height=77)

        self.pack()


class Assistant:
    awakening_sound = "assistant_sounds/blink.mp3"
    goodbye_sound = "assistant_sounds/done.mp3"
    bad_command_sound = "assistant_sounds/bad.mp3"

    @staticmethod
    def speak(text_to_speech, speech_language="pl", block=True):
        tts = gTTS(text=text_to_speech, lang=speech_language)
        recorded_assistant_voice_filename = "_assistant_voice.mp3"
        tts.save(recorded_assistant_voice_filename)
        playsound.playsound(recorded_assistant_voice_filename, block=block)
        os.remove(recorded_assistant_voice_filename)


class SpeechRecognition:

    @staticmethod
    def recognize_words(speech_language="pl", print_spoken_words=True):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            audio = recognizer.listen(source)
            said = ""

            try:
                said = recognizer.recognize_google(audio, language=speech_language)
                said = said.lower()
                if print_spoken_words:
                    print(said)
            except Exception as e:
                print(e)

            return said


class Tofify(spotipy.Spotify):

    def __init__(self, auth_manager):

        super().__init__(auth_manager)
        self.tofify = spotipy.Spotify(auth_manager=auth_manager)
        self.awakening_commands = ["okej spotify", "open spotify", "określ spotify", "okej spoty", "pokaż spotify",
                                   "okej spoko",
                                   "szukaj spotify", "play spotify"]
        self.next_track_commands = ["następny", "następna", "do przodu"]
        self.previous_track_commands = ["poprzedni", "poprzednia", "do tyłu"]
        self.turn_on_shuffle_commands = ["włącz losowość", "włącz losowy", "włącz losowe", "odtwarzaj losowo",
                                         "włącz losowanie"]
        self.turn_off_shuffle_commands = ["wyłącz losowość", "wyłącz losowe", "wyłącz losowanie",
                                          "wyłącz odtwarzanie losowe"]
        self.pause_playback_commands = ["zatrzymaj", "wstrzymaj", "zapauzuj", "pauza", "czekaj"]
        self.start_playback_commands = ["wznów", "ponów", "włącz muzykę", "znów", "włącz dźwięk", "włącz muzę",
                                        "włącz dźwięki"]
        self.set_volume_commands = ["ustaw", "głośność", "dźwięk", "zmień", "głos"]
        self.search_track_commands = ["znajdź", "poszukaj", "wyszukaj", "znasz"]
        self.search_english_track_commands = ["angielską", "angielski", "angielskiego", "anglika", "anglik",
                                              "angielska"]
        self.search_polish_track_commands = ["polskę", "polska", "polskie", "polskiego", "polską", "polski"]
        self.exit_commands = ["wyjdź", "anuluj", "przestań", "skończ"]

        self.spoken_words = ""
        self.bad_command_invoked = False

    def get_only_numbers_from_string(self, ):
        try:
            numeric_values_from_sentence = [x for x in self.spoken_words if x.isnumeric()]
            full_numeric_value = ''.join(numeric_values_from_sentence)
            return int(full_numeric_value)
        except ValueError:
            return None

    def any_of_spoken_words_in_commands(self, commands: list):
        return any(word in self.spoken_words for word in commands)

    def get_track_search_results(self, spoken_words):
        search_result = self.tofify.search(q=spoken_words, type="track", limit=1, offset=0, market="PL")
        track_url = search_result["tracks"]["items"][0]["external_urls"]["spotify"]
        track_uri = track_url.split("/")[-1]
        return track_uri

    def search_and_start_a_track(self, speech_language):
        if speech_language == "en-US":
            Assistant.speak("Podaj nazwę angielskiego utworu")
        else:
            Assistant.speak("Podaj nazwę polskiego utworu")
        while True:
            try:
                self.spoken_words = SpeechRecognition.recognize_words(speech_language=speech_language)
                track_uri = self.get_track_search_results(self.spoken_words)
                self.tofify.start_playback(uris=[f"spotify:track:{track_uri}"])
                break
            except spotipy.exceptions.SpotifyException as e:
                if "No active device" in str(e):
                    Assistant.speak(
                        "Nie znaleziono aktywnego odtwarzacza Tofify. Włącz odtwarzacz i spróbuj ponownie.")
                    break
                else:
                    print(e)
                    Assistant.speak("Nie znaleziono utworu. Spróbuj ponownie.")
                continue

            except IndexError:
                Assistant.speak("Nie znaleziono utworu. Spróbuj ponownie.")
                continue

    def listen_for_commands(self):
        while True:
            self.spoken_words = SpeechRecognition.recognize_words()

            if self.any_of_spoken_words_in_commands(self.awakening_commands):
                playsound.playsound(Assistant.awakening_sound, block=False)
                while True:
                    try:
                        self.spoken_words = SpeechRecognition.recognize_words()
                        if self.spoken_words == "":
                            continue

                        elif self.any_of_spoken_words_in_commands(self.next_track_commands):
                            self.tofify.next_track()
                            break

                        elif self.any_of_spoken_words_in_commands(self.previous_track_commands):
                            self.tofify.previous_track()
                            break

                        elif self.any_of_spoken_words_in_commands(self.pause_playback_commands):
                            self.tofify.pause_playback()
                            break

                        elif self.any_of_spoken_words_in_commands(self.start_playback_commands):
                            self.tofify.start_playback()
                            break

                        elif self.any_of_spoken_words_in_commands(self.turn_on_shuffle_commands):
                            self.tofify.shuffle(True)
                            break

                        elif self.any_of_spoken_words_in_commands(self.turn_off_shuffle_commands):
                            self.tofify.shuffle(False)
                            break

                        elif self.any_of_spoken_words_in_commands(self.set_volume_commands):
                            volume_value = self.get_only_numbers_from_string()
                            if volume_value is not None:
                                self.tofify.volume(volume_value)
                            break

                        elif self.any_of_spoken_words_in_commands(self.search_track_commands) and \
                                self.any_of_spoken_words_in_commands(
                                    self.search_english_track_commands):
                            self.search_and_start_a_track("en-US")
                            break

                        elif self.any_of_spoken_words_in_commands(self.search_track_commands) and \
                                self.any_of_spoken_words_in_commands(self.search_track_commands):
                            self.search_and_start_a_track("pl")
                            break

                        elif self.any_of_spoken_words_in_commands(self.exit_commands):
                            break
                        else:
                            playsound.playsound(Assistant.bad_command_sound, block=False)
                            self.bad_command_invoked = True
                            break
                    except spotipy.SpotifyException as e:
                        if "No active device" in str(e):
                            messagebox.showerror("Nie znaleziono odtwarzacza Tofify",
                                                 "Nie znaleziono aktywnego odtwarzacza Tofify. Upewnij się, że aplikacja jest włączona oraz odtwarza muzykę.")
                            playsound.playsound(Assistant.bad_command_sound, block=False)
                            self.bad_command_invoked = True
                        break

                if not self.bad_command_invoked:
                    playsound.playsound(Assistant.goodbye_sound, block=False)

                self.bad_command_invoked = False


class FileManager:
    def get_client_id_from_file(self, credentials_file):
        with open(credentials_file) as f:
            first_line = f.readlines()

        credentials = first_line[0].split(" ")
        client_id = credentials[0]
        return client_id

    def get_client_secret_from_file(self, credentials_file):
        with open(credentials_file) as f:
            first_line = f.readlines()

        credentials = first_line[0].split(" ")
        client_secret = credentials[1]
        return client_secret

    @staticmethod
    def check_existance_of_cache_file():
        if not os.path.exists(".cache"):
            messagebox.showerror("Nie znaleziono pliku",
                                 "Nie znaleziono pliku z tokenem uprawniającym do sterowania odtwarzaczem. Upewnij się, że aktywowałeś asystenta Tofify zanim uruchomiłeś tę aplikację.")
            os._exit(1)

    @staticmethod
    def check_existance_of_credentials_file():
        if not os.path.exists("credentials.txt"):
            messagebox.showerror("Nie znaleziono pliku",
                                 "Nie znaleziono pliku zawierającego poświadczenia do logowania. Upewnij się, że aktywowałeś asystenta Tofify zanim uruchomiłeś tę aplikację.")
            os._exit(1)


class SystemTrayHandler:
    @staticmethod
    def quit_window(icon):
        icon.stop()
        window.destroy()
        os._exit(1)

    @staticmethod
    def show_window(icon):
        icon.stop()
        window.after(0, window.deiconify)

    def withdraw_window(self):
        window.withdraw()
        image = Image.open("logo.png")
        menu = (item('Zamknij aplikację', self.quit_window), item('Pokaż okno aplikacji', self.show_window))
        icon = pystray.Icon("name", image, "Asystent Tofify", menu)
        icon.run()

if __name__ == "__main__":
    file_manager = FileManager()
    file_manager.check_existance_of_credentials_file()
    file_manager.check_existance_of_cache_file()
    credentials_file = "credentials.txt"
    client_id = file_manager.get_client_id_from_file(credentials_file)
    client_secret = file_manager.get_client_secret_from_file(credentials_file)

    authentication_scope = ['user-read-playback-state', 'user-modify-playback-state', 'user-read-private',
                            'user-library-read', 'user-read-email', 'playlist-read-private']
    tofify = Tofify(auth_manager=SpotifyOAuth(client_id=client_id,
                                              client_secret=client_secret,
                                              redirect_uri='https://example.com/callback/',
                                              scope=authentication_scope))
    command_listener_thread = threading.Thread(target=tofify.listen_for_commands)
    command_listener_thread.start()

    window = Tk()
    window.wm_title("Asystent Tofify")
    window.iconphoto(False, PhotoImage(file='logo.png'))
    system_tray_handler = SystemTrayHandler()
    window.protocol('WM_DELETE_WINDOW', system_tray_handler.withdraw_window)
    window.configure(bg="#ffffff")

    tofify_window = MainWindow(window)


    window.resizable(False, False)
    window.mainloop()
