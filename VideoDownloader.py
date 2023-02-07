import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as msgb
from pytube import YouTube
from threading import Thread


def download_video():
    save_button.config(state="disabled")
    try:
        youtubeObject = YouTube(textbox.get())
        youtubeObject = youtubeObject.streams.get_highest_resolution()
        youtubeObject.download()

    except Exception as e:
        msgb.showerror("Error", f"No se pudo descargar el video: {e}")
        save_button.config(state="normal")
        return
    msgb.showinfo("Info", "Video descargado")
    save_button.config(state="normal")
    textbox.delete(0, "end")


def download_task():
    thread = Thread(target=download_video)
    thread.start()


mainwin = tk.Tk()
mainwin.title("Video Downloader")
mainwin.geometry("500x80")

textbox = tk.Entry(mainwin, font=("TkDefaultFont", 15))
textbox.grid(row=0, column=0, sticky="ew")

save_button = tk.Button(mainwin, text="Guardar", command=download_task, font=("TkDefaultFont", 15))
save_button.grid(row=1, column=0, sticky="ns")

mainwin.columnconfigure(0, weight=1)

try:
    mainwin.mainloop()
except Exception as e:
    msgb.showerror("Error", f"{e}")
