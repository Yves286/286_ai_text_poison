from tkinter import *
from text_encode import replace_char
import customtkinter

def submit():
    print("This button works!")
    user_input = text_entry.get(0.0,'end')
    output_text = replace_char(user_input)
    encoded_text.delete(0.0, 'end')
    encoded_text.insert(0.0, output_text)



customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("1200x800")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

titleLabel = customtkinter.CTkLabel(master=frame, text="Welcome to the Text Poisoner", font=("Roboto",24))
titleLabel.pack(pady=12, padx=10)

instructLabel = customtkinter.CTkLabel(master=frame, text="Please enter the text you want to enter below:", font=("Roboto",18))
text_entry = customtkinter.CTkTextbox(master=frame,width=500, height=250,wrap="word",activate_scrollbars=True,scrollbar_button_color="silver",scrollbar_button_hover_color="gray",font=("Roboto",14))
text_entry.pack(pady=12,padx=10)

encoded_text = customtkinter.CTkTextbox(master=frame,width=500,height=250,wrap="word",activate_scrollbars=True,scrollbar_button_color="silver",scrollbar_button_hover_color="gray",font=("Roboto",14))
encoded_text.pack(pady=12,padx=10)

encodeButton = customtkinter.CTkButton(master=frame, text="Encode!", command=submit,font=("Roboto",18))
encodeButton.pack(pady=12,padx=10)

root.mainloop()