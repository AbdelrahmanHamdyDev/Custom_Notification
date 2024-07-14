from screeninfo import get_monitors
from customtkinter import *
from PIL import Image, ImageTk


def Custom_Notify(img_path=None, header_text="Test", input_text="This is how to the Notification will look like", left=130, up=121, width=400, height=120, duration=5, text_size=20):

  """
  Display a notification window with optional image, header, and text.

    Parameters:\n
    - img_path (str or None): Path to the image file to display beside Text (default: None).
    - header_text (str): Text to display as the header of the notification (default: "Test").
    - input_text (str): Text content to display in the notification body (default: "This is how the Notification will look like").
    - left (float): Horizontal positioning factor relative to screen width, bigger value mean more to left (default: 1.3).
    - up (float): Vertical positioning factor relative to screen height, bigger value mean more to up (default: 1.21).
    - width (int): Width of the notification window (default: 400).
    - height (int): Height of the notification window (default: 120).
    - duration (int): Duration in seconds for which the notification will be displayed (default: 5 sec).
    - text_size (int): Font size for text in the notification (default: 20).

    Notes:\n
    - The notification window is displayed with an animation effect that starts from the right side of the screen.
    - Supports displaying an optional image.
    """

  # region Tkinter_Position

  def Screen_resolution():
    for monitor in get_monitors():
      if monitor.is_primary:
        return monitor.width, monitor.height

  screen_width, screen_height = Screen_resolution()
  x = int(screen_width / left)
  y = int(screen_height / up)

  # endregion

  #region Animation

  def Start(current_x=x+500):
    if current_x >= x:
        root.geometry(f'{width}x{height}+{current_x}+{y}')
        root.after(2, lambda: Start(current_x -1)) #2 mm

  def End(current_x=x):
    if current_x <= x+400:
        root.geometry(f'{width}x{height}+{current_x}+{y}')
        root.after(2, lambda: End(current_x +1)) #2 mm
    else:
      root.destroy()

  #endregion

  #region Tkinter_Code

  root = CTkToplevel()

  # always on top
  root.overrideredirect(True)
  root.wm_attributes("-topmost", True)

  # region image

  try:
    image = Image.open(img_path)
    image = image.resize((150, 150))
    tk_image = ImageTk.PhotoImage(image)

    img_label = CTkLabel(root, text=" ", image=tk_image)
    img_label.grid(row=0, column=0, rowspan=2)
  except:
    pass


  # endregion

  # region Filler

  filler_label = CTkLabel(root, text="", width=20)
  filler_label.grid(row=0, column=1, rowspan=2)

  # endregion

  #region Text

  #header
  headertxt_label = CTkLabel(root, text=header_text, font=("Times New Roman", text_size))
  headertxt_label.grid(row=0, column=2, sticky='n')

  #body
  bodytxt_label = CTkLabel(root, text=input_text, font=("Verdana", text_size-10), wraplength=200)
  bodytxt_label.grid(row=0, column=2, pady=30)

  #endregion

  # animation handle
  Start()
  root.after(duration*1000, End)  # num*1000 --> Seconds

  root.mainloop()

  #endregion
