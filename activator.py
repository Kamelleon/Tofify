import os
import sys
import threading
import time
import tkinter.ttk
from tkinter import *
from tkinter import messagebox


client_id = ""
client_secret = ""


class FrameChanger:
    @staticmethod
    def close_current_frame_and_show_new(current_frame, new_frame):
        print("raising")
        current_frame.pack_forget()
        new_frame.pack()


class StartFrame(tkinter.ttk.Frame):
    def __init__(self, container, width=411, height=577):
        super().__init__(container, width=width, height=height)

        self.background_image = "activation_start_screen/background.png"
        self.button_image = "activation_start_screen/img0.png"

        self.canvas = Canvas(
            bg="#ffffff",
            height=577,
            width=411,
            bd=0,
            highlightthickness=0,
            relief="ridge")

        self.background_photo_image = PhotoImage(file=self.background_image)

        self.canvas.create_image(205.0, 288.5, image=self.background_photo_image)

        self.canvas.place(x=0, y=0)

        self.next_button_photo_image = PhotoImage(file=self.button_image)

        self.next_button = Button(
            image=self.next_button_photo_image,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=lambda: FrameChanger.close_current_frame_and_show_new(self, BeforeActivationFrame(window)))

        self.next_button.place(
            x=51, y=384,
            width=307,
            height=94)

        self.pack()

class BeforeActivationFrame(tkinter.ttk.Frame):

    def __init__(self, container, width=944, height=828):
        super().__init__(container, width=width, height=height)
        self.canvas = Canvas(
            window,
            bg="#ffffff",
            height=828,
            width=944,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        self.canvas.place(x=0, y=0)

        self.background_img = PhotoImage(file=f"before_activation/background.png")
        self.canvas.create_image(
            471.5, 421.5,
            image=self.background_img)

        self.button_next_image = PhotoImage(file=f"before_activation/img0.png")
        self.button_next = Button(
            image=self.button_next_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: FrameChanger.close_current_frame_and_show_new(self,ActivationFrame1(window)),
            relief="flat")

        self.button_next.place(
            x=299, y=693,
            width=337,
            height=100)

class ActivationFrame1(tkinter.ttk.Frame):
    def __init__(self, container, width=944, height=828):
        super().__init__(container, width=width, height=height)

        self.background_image = "activation1_screen/aktywacja1_background.png"
        self.button_image = "activation1_screen/aktywacja1_dalej.png"

        self.canvas = Canvas(
            bg="#ffffff",
            height=828,
            width=944,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        self.canvas.place(x=0, y=0)

        self.background_photo_image = PhotoImage(file=self.background_image)
        self.canvas.create_image(
            475.5, 415.5,
            image=self.background_photo_image)

        self.next_button_photo_image = PhotoImage(file=self.button_image)
        self.next_button = Button(
            image=self.next_button_photo_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: FrameChanger.close_current_frame_and_show_new(self, ActivationFrame2(window)),
            relief="flat")

        self.next_button.place(
            x=314, y=703,
            width=315,
            height=98)


class ActivationFrame2(tkinter.ttk.Frame):
    def __init__(self, container, width=944, height=828):
        super().__init__(container, width=width, height=height)

        self.background_image = "activation2_screen/aktywacja2_background.png"
        self.button_image = "activation2_screen/aktywacja2_dalej.png"

        self.canvas = Canvas(
            bg="#ffffff",
            height=828,
            width=944,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        self.canvas.place(x=0, y=0)

        self.background_photo_image = PhotoImage(file=self.background_image)
        self.canvas.create_image(
            471.5, 421.5,
            image=self.background_photo_image)

        self.next_button_photo_image = PhotoImage(file=self.button_image)
        self.next_button = Button(
            image=self.next_button_photo_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: FrameChanger.close_current_frame_and_show_new(self, ActivationFrame3(window)),
            relief="flat")

        self.next_button.place(
            x=314, y=721,
            width=315,
            height=98)


class ActivationFrame3(tkinter.ttk.Frame):
    def __init__(self, container, width=944, height=828):

        super().__init__(container, width=width, height=height)

        self.background_image = "activation3_screen/aktywacja3_background.png"
        self.button_image = "activation3_screen/aktywacja3_dalej.png"
        self.textbox_image_0 = "activation3_screen/aktywacja3_textbox0.png"
        self.textbox_image_1 = "activation3_screen/aktywacja3_textbox1.png"

        self.canvas = Canvas(
            bg="#ffffff",
            height=828,
            width=944,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        self.canvas.place(x=0, y=0)

        self.background_image = PhotoImage(file=self.background_image)
        self.canvas.create_image(
            471.5, 421.5,
            image=self.background_image)

        self.textbox_photo_image_0 = PhotoImage(file=self.textbox_image_0)
        self.canvas.create_image(
            689.5, 433.0,
            image=self.textbox_photo_image_0)

        self.textbox0 = Entry(
            bd=0,
            bg="#d9d9d9",
            highlightthickness=0)

        self.textbox0.place(
            x=467, y=414,
            width=445,
            height=36)

        self.textbox_photo_image_1 = PhotoImage(file=self.textbox_image_1)

        self.canvas.create_image(
            689.5, 625.0,
            image=self.textbox_photo_image_1)

        self.textbox1 = Entry(
            bd=0,
            bg="#d9d9d9",
            highlightthickness=0)

        self.textbox1.place(
            x=467, y=606,
            width=445,
            height=36)

        self.next_button_photo_image = PhotoImage(file=self.button_image)

        self.next_button = Button(
            image=self.next_button_photo_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.check_inputs_and_raise_frame(),
            relief="flat")

        self.next_button.place(
            x=525, y=700,
            width=315,
            height=98)

    def check_inputs_and_raise_frame(self):
        global client_secret, client_id
        if len(self.textbox0.get()) == 0 or len(self.textbox1.get()) == 0:
            messagebox.showerror("Nie uzupełniono wszystkich pól", "Uzupełnij oba pola tekstowe wartościami")
        else:
            client_id = self.textbox0.get()
            client_secret = self.textbox1.get()
            with open('credentials.txt', 'w+') as file:
                file.write(f"{client_id} {client_secret}")
            FrameChanger.close_current_frame_and_show_new(self, ActivationFrame4(window))


class ActivationFrame4(tkinter.ttk.Frame):
    def __init__(self, container, width=944, height=828):
        super().__init__(container, width=width, height=height)

        self.background_image = "activation4_screen/aktywacja4_background.png"
        self.button_image = "activation4_screen/aktywacja4_dalej.png"

        self.canvas = Canvas(
            bg="#ffffff",
            height=828,
            width=944,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        self.canvas.place(x=0, y=0)

        self.background_image = PhotoImage(file=self.background_image)
        self.canvas.create_image(
            471.5, 421.5,
            image=self.background_image)

        self.next_button_photo_image = PhotoImage(file=self.button_image)
        self.next_button = Button(
            image=self.next_button_photo_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: FrameChanger.close_current_frame_and_show_new(self, ActivationFrame5(window)),
            relief="flat")

        self.next_button.place(
            x=298, y=708,
            width=337,
            height=100)
        # sp.next_track()

    # os.system(f"python check.py {client_id} {client_secret}")

class ActivationFrame5(tkinter.ttk.Frame):
    def __init__(self, container, width=944, height=828):
        super().__init__(container, width=width, height=height)

        self.canvas = Canvas(
            window,
            bg="#ffffff",
            height=828,
            width=944,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        self.canvas.place(x=0, y=0)

        self.background_image = PhotoImage(file=f"activation5_screen/background.png")

        self.canvas.create_image(
            471.5, 421.5,
            image=self.background_image)

        self.button_link_image = PhotoImage(file=f"activation5_screen/img0.png")

        self.button_link = Button(
            image=self.button_link_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.generate_activation_link,
            relief="flat")

        self.button_link.place(
            x=351, y=376,
            width=452,
            height=91)

        self.entry_backgound_image = PhotoImage(file=f"activation5_screen/img_textBox0.png")
        self.canvas.create_image(
            577.0, 571.5,
            image=self.entry_backgound_image)

        self.entry = Entry(
            bd=0,
            bg="#c4c4c4",
            highlightthickness=0)

        self.entry.place(
            x=392, y=556,
            width=370,
            height=29)

        self.button_next_photo_image = PhotoImage(file=f"activation5_screen/img1.png")
        self.button_next = Button(
            image=self.button_next_photo_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.test_spotify_playback,
            relief="flat")

        self.button_next.place(
            x=406, y=675,
            width=337,
            height=100)

    def generate_activation_link(self):
            t1 = threading.Thread(target=self._check_credentials)
            t1.start()

    def _check_credentials(self):
            import spotipy

            from spotipy import SpotifyOAuth

            authentication_scope = ['user-read-playback-state', 'user-modify-playback-state', 'user-read-private',
                                    'user-library-read', 'user-read-email', 'playlist-read-private']

            file = open("credentials.txt")
            with file as f:
                first_line = f.readlines()

            credentials = first_line[0].split(" ")

            client_id = credentials[0]
            client_secret = credentials[1]

            sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                           client_secret=client_secret,
                                                           redirect_uri='https://example.com/callback/',
                                                           scope=authentication_scope))
            sp.pause_playback()
            time.sleep(0.3)
            sp.start_playback()

    def test_spotify_playback(self):
        if len(self.entry.get()) == 0:
            messagebox.showerror("Nie uzupełniono wszystkich pól.","Uzupełnij wszystkie pola odpowiednimi wartościami.")
        else:
            uri = str(self.entry.get())
            with open('uri.txt', 'w+') as file:
                file.write(f"{uri}")
            time.sleep(0.5)
            os.remove("uri.txt")
            if os.path.exists(".cache"):
                print("Udalo sie")
                FrameChanger.close_current_frame_and_show_new(self, SuccessFrame(window))
            else:
                print("Nie udalo sie")
                FrameChanger.close_current_frame_and_show_new(self, FailureFrame(window))

class SuccessFrame(tkinter.ttk.Frame):
    def __init__(self, container, width=411, height=577):
        super().__init__(container, width=width, height=height)
        self.canvas = Canvas(
            window,
            bg="#ffffff",
            height=577,
            width=411,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        self.canvas.place(x=0, y=0)

        self.background_img = PhotoImage(file=f"success_screen/background.png")
        self.canvas.create_image(
            205.5, 293.0,
            image=self.background_img)

        self.end_button_image = PhotoImage(file=f"success_screen/img0.png")
        self.end_button = Button(
            image=self.end_button_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.close_program,
            relief="flat")

        self.end_button.place(
            x=64, y=365,
            width=292,
            height=105)

    @staticmethod
    def close_program():
        sys.exit(1)

class FailureFrame(tkinter.ttk.Frame):
    def __init__(self, container, width=946, height=684):
        super().__init__(container, width=width, height=height)
        self.canvas = Canvas(
            window,
            bg="#ffffff",
            height=684,
            width=946,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        self.canvas.place(x=0, y=0)

        self.background_img = PhotoImage(file=f"failure_screen/background.png")
        self.canvas.create_image(
            471.5, 421.5,
            image=self.background_img)

        self.end_button_image = PhotoImage(file=f"failure_screen/img0.png")
        self.end_button = Button(
            image=self.end_button_image,
            borderwidth=0,
            highlightthickness=0,
            command=SuccessFrame.close_program,
            relief="flat")

        self.end_button.place(
            x=331, y=528,
            width=292,
            height=105)

        self.retry_button_image = PhotoImage(file=f"failure_screen/img1.png")
        self.retry_button = Button(
            image=self.retry_button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: FrameChanger.close_current_frame_and_show_new(self, BeforeActivationFrame(window)),
            relief="flat")

        self.retry_button.place(
            x=261, y=367,
            width=431,
            height=110)

if __name__ == "__main__":
    if os.path.exists(".cache"):
        os.remove(".cache")
    window = Tk()
    window.wm_title("Aktywator Tofify")
    window.iconphoto(False, PhotoImage(file='logo.png'))
    window.configure(bg="#ffffff")
    start_frame = StartFrame(window)
    window.resizable(False, False)
    window.mainloop()
