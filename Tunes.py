import tkinter as tk
from tkinter import filedialog, messagebox
import webbrowser
import os
import subprocess

def select_audio():
    path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav *.flac *.m4a")])
    if path:
        audio_path_var.set(path)

def select_image():
    path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.png")])
    if path:
        image_path_var.set(path)

def create_video_ffmpeg(image_path, audio_path, output_path):
    if os.path.exists(output_path):
        os.remove(output_path)
    if image_path:
        cmd = f'ffmpeg -loop 1 -i "{image_path}" -i "{audio_path}" -vf "drawtext=text=\'github.com/Gh0styTongue\':fontcolor=white:fontsize=24:x=10:y=10" -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -shortest "{output_path}" -y'
    else:
        cmd = f'ffmpeg -i "{audio_path}" -filter_complex "color=c=black:s=1280x720,drawtext=text=\'github.com/Gh0styTongue\':fontcolor=white:fontsize=24:x=10:y=10" -c:v libx264 -c:a aac -b:a 192k -pix_fmt yuv420p -shortest "{output_path}" -y'
    subprocess.run(cmd, shell=True)

def process():
    image_path = image_path_var.get()
    audio_path = audio_path_var.get()
    tweet_text = tweet_text_var.get()
    if not audio_path or not tweet_text:
        messagebox.showerror("Error", "Select an audio file and enter tweet text.")
        return
    output_path = "output_video.mp4"
    create_video_ffmpeg(image_path, audio_path, output_path)
    tweet_url = f"https://twitter.com/compose/tweet?text={tweet_text.replace(' ', '%20')}"
    webbrowser.open(tweet_url)
    messagebox.showinfo("Done", f"Video created: {output_path}\nDrag it into the opened Twitter composer!")

app = tk.Tk()
app.title("TunesToX")

audio_path_var = tk.StringVar()
image_path_var = tk.StringVar()
tweet_text_var = tk.StringVar()

tk.Label(app, text="Select Audio:").pack()
tk.Entry(app, textvariable=audio_path_var, width=50).pack()
tk.Button(app, text="Browse Audio", command=select_audio).pack()

tk.Label(app, text="Select Image (Optional):").pack()
tk.Entry(app, textvariable=image_path_var, width=50).pack()
tk.Button(app, text="Browse Image", command=select_image).pack()

tk.Label(app, text="Tweet Text:").pack()
tk.Entry(app, textvariable=tweet_text_var, width=50).pack()

tk.Button(app, text="Create Video & Open Twitter", command=process).pack(pady=10)

app.mainloop()
