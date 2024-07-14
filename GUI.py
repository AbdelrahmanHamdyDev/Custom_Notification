from customtkinter import *
from pystray import MenuItem as item
import pystray
from PIL import Image, ImageTk
from Notification import Custom_Notify

def Main():

  global img_path
  img_path = ""

  app = CTk()

  app.geometry('410x500')
  app.resizable(width=False, height=False)

  app.title("Customize your Notification")
  app.iconbitmap("Assets/notification.ico")

  #region cus_Notify

  #region Parameters

  # region img_path

  def browse_file():
    global img_path
    filename = filedialog.askopenfilename(initialdir="/", title="Select an Image")
    if filename:
      img_path = filename
      browse_button.destroy()
      Img_label.configure(text="Selected Image: ")
      image = Image.open(img_path)
      image = image.resize((100, 100))
      tk_image = ImageTk.PhotoImage(image)

      img_label = CTkLabel(app, text="", image=tk_image)
      img_label.grid(row=0,column=1,pady=10)

  Img_label = CTkLabel(app,text="Choose Image (if Need): ")
  Img_label.grid(row=0,column=0,padx=40,pady=10)

  browse_button = CTkButton(app, text="Select Image", command=browse_file)
  browse_button.grid(row=0,column=1,pady=10)

  #endregion

  # region header_text

  header_label = CTkLabel(app, text="Enter Header Text:")
  header_label.grid(row=1, column=0, pady=5)

  header_textbox = CTkEntry(app, width=130)
  header_textbox.grid(row=1, column=1, pady=5)

  # endregion

  # region input_text

  body_label = CTkLabel(app, text="Enter Body Text:")
  body_label.grid(row=2, column=0, pady=5)

  body_textbox = CTkEntry(app, width=130)
  body_textbox.grid(row=2, column=1, pady=5)

  #endregion

  # region left

  def on_left_slider_move(value):
    left = float(value)
    left_value_label.configure(text=str(format(left, ".2f")))

  left_label = CTkLabel(app, text="Choose Left Value:")
  left_label.grid(row=3, column=0, pady=5)

  left_value_label = CTkLabel(app, text="1.3")
  left_value_label.grid(row=3, column=2, pady=5)

  left_slider = CTkSlider(app,from_=1.1,to=20,width=100,orientation=HORIZONTAL,command=on_left_slider_move)
  left_slider.grid(row=3, column=1, pady=5)
  left_slider.set(1.3)
  #endregion

  # region up

  def on_up_slider_move(value):
    up = float(value)
    up_value_label.configure(text=str(format(up, ".2f")))

  up_label = CTkLabel(app, text="Choose up Value:")
  up_label.grid(row=4, column=0, pady=5)

  up_value_label = CTkLabel(app, text="1.21")
  up_value_label.grid(row=4, column=2, pady=5)

  up_slider = CTkSlider(app,from_=1.15,to=10,width=100,orientation=HORIZONTAL,command=on_up_slider_move)
  up_slider.grid(row=4, column=1, pady=5)
  up_slider.set(1.21)


  #endregion

  # region width

  width_label = CTkLabel(app, text="Enter Width Value (4 numbers):")
  width_label.grid(row=5, column=0, pady=5)

  width_textbox = CTkEntry(app, width=50)
  width_textbox.grid(row=5, column=1, pady=5)

  #endregion

  # region height

  height_label = CTkLabel(app, text="Enter height Value (4 numbers):")
  height_label.grid(row=6, column=0, pady=5)

  height_textbox = CTkEntry(app, width=50)
  height_textbox.grid(row=6, column=1, pady=5)

  #endregion

  # region duration

  duration_label = CTkLabel(app, text="Enter duration Time (In Seconds):")
  duration_label.grid(row=7, column=0, pady=5)

  duration_textbox = CTkEntry(app, width=130)
  duration_textbox.grid(row=7, column=1, pady=5)

  #endregion

  # region text_size

  text_size = 0

  def on_size_slider_move(value):
    text_size = int(value)
    size_value_label.configure(font=("Arial", text_size))

  size_label = CTkLabel(app, text="Choose Text size Value:")
  size_label.grid(row=8, column=0, pady=5)

  size_value_label = CTkLabel(app, text="Aa")
  size_value_label.grid(row=8, column=2, pady=5)

  size_slider = CTkSlider(app, from_=1, to=24,width=100, orientation=HORIZONTAL, command=on_size_slider_move)
  size_slider.grid(row=8, column=1, pady=5)

  #endregion

  #endregion

  #region Test

  def Test():
    global img_path

    header_text = header_textbox.get() if header_textbox.get() != '' else "Test"
    input_text = body_textbox.get() if body_textbox.get() != '' else "This is Test"
    left = left_slider.get()
    up = up_slider.get()
    width = int(width_textbox.get()) if width_textbox.get() != '' else 400
    height = int(height_textbox.get()) if height_textbox.get() != '' else 120
    duration = int(duration_textbox.get()) if duration_textbox.get() != '' else 5
    text_size = size_slider.get() if size_slider else 18

    Custom_Notify(img_path, header_text, input_text, left, up, width, height, duration, text_size)

  Test_button = CTkButton(app, text="Test", command=Test)
  Test_button.grid(row=10, column=1, pady=5)

  #endregion

  #endregion

  app.mainloop()


Main()
