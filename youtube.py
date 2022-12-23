from tkinter import *
from tkinter import filedialog
from pytube import YouTube
import shutil
import threading

def select_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)

def high_q():
    download_status.config(text = "Checking Status....")
    url = link_entry.get()
    path = path_label.cget("text")
    video = YouTube(url)
    download_status.config(text = video.title)
    download_status1.config(text="Download Started.....")
    try:
        video.streams.get_highest_resolution().download()
        download_status1.config(text = "Download Complete")
    except:
        download_status.config(text = "Failed To Download !")


def low_q():
    download_status.config(text = "Checking Status....")
    url = link_entry.get()
    path = path_label.cget("text")
    video = YouTube(url)
    download_status.config(text = video.title)
    download_status1.config(text="Download Started.....")
    try:
        video.streams.get_lowest_resolution().download()
        download_status1.config(text = "Download Complete")
    except:
        download_status.config(text = "Failed To Download !")


# def download_video():
#     link = link_entry.get()
#     path = path_label.cget("text")
#     video = YouTube(link)
#     video.streams.get_lowest_resolution()
def download_video():
    pass


root = Tk()
root.title("Youtube Video Downloader")
root.geometry("500x600")

img_frame = Frame(root)
img_frame.pack()

img_canvas = Canvas(img_frame,width = 550, height=90,bg="lightpink")
img_canvas.pack()

logo_img = PhotoImage(file="yt1.png")
logo_img = logo_img.subsample(4,4)
img_canvas.create_image(250,40,image = logo_img)


# Frame 1
frame1 = Frame(root)
frame1.pack()


# Link Entery 
text = Label(frame1, text="Enter Link of Youtube Video")
text.pack(pady=12)
link_entry = Entry(frame1,width=40)
link_entry.pack()

# path button
path_label = Label(root,text=" ")
path_label.place(x=170,y=180)
path_button = Button(root, text="Select Path to Save Video", command=select_path)
path_button.place(x=180,y=210)

# # Download Button
# download_button = Button(root, text="Start Download", command=download_video)
# download_button.place(x=200,y=240)


# Quality Buttons
quality_label = Label(root,text="Select Video Quality",font="arial 13",bg="lightblue")
quality_label.place(x=170,y=300)

# max_quality = Button(root, text="Maximum Quality")
max_quality = Button(root, text="Highest Quality", command=threading.Thread(target=high_q).start)
max_quality.place(x=50,y=340)

low_quality = Button(root, text="Low Quality", command=threading.Thread(target=low_q).start)
low_quality.place(x=200,y=340)

audio_quality = Button(root, text="Audio Only")
audio_quality.place(x=330,y=340)

# Download Status 
download_status = Label(root, text=" ")
download_status.place(x=50, y=470)

download_status1 = Label(root, text=" ")
download_status1.place(x=200, y=500)


# Footer 
footer = Label(root,text="Software by @KuldeepSaini65",font="arial 11")
footer.pack(side=BOTTOM)

root.mainloop()