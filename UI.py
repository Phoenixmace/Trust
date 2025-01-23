import tkinter as tk
from tkinter import PhotoImage
import os
from win32api import GetSystemMetrics
from PIL import Image, ImageTk


class EmailApp:
    def __init__(self):
        root = tk.Tk()
        self.root = root
        self.root.title("Trust")
        project_path = os.path.dirname(os.path.abspath(__file__))
        self.logo = os.path.join(project_path, "images/logo.png")


        monitor_Width = GetSystemMetrics(0)
        monitor_Height = GetSystemMetrics(1)
        resolution_string = f'{monitor_Width}x{monitor_Height}'
        self.root.geometry(resolution_string)


        # variables
        self.is_collapsed = True
        self.menues_weight = 40
        self.main_field_weight = 240

        # Testing vars
        self.mail_dict = {}
        self.testmail = {
            'day':'23. 01. 2025',
            'time': '19:00',
            'sender':'test@mail.com',
            'target_mail':'mail_1',
            'betreff': 'testing',
            'text': 'hello world\n\n\n\n\nheya'
        }
        self.mail_dict['hash'] = self.testmail

        # Define image paths
        self.write_mail_icon = os.path.join(project_path, "images/write_mail.png")
        self.reload_icon = os.path.join(project_path, "images/reload.png")
        self.collapse_menu_icon = os.path.join(project_path, "images/collapse_menu.png")
        self.account_icon = os.path.join(project_path, "images/account.png")
        self.settings_icon = os.path.join(project_path, "images/settings.png")
        self.back_icon = os.path.join(project_path, "images/back.png")
        self.send_icon = os.path.join(project_path, "images/send.png")

        # format grid
        self.root.grid_columnconfigure(0, weight=self.menues_weight)  # Menu frame: 1/4 of the total width
        self.root.grid_columnconfigure(1, weight=self.menues_weight)  # List frame: 1/4 of the total width
        self.root.grid_columnconfigure(2, weight=self.main_field_weight)  # Display frame: 1/2 of the total width
        self.root.grid_rowconfigure(0, weight=1)  # Make row 0 fill the available heigh

        # Create menu frames
        self.menu_frame = tk.Frame(self.root, bg="lightgray")
        self.menu_frame.grid(row=0, column=0, sticky="nswe")
        self.menu_frame.grid_columnconfigure(0, weight=1)
        self.menu_frame.grid_columnconfigure(1, weight=1)
        self.menu_frame.grid_columnconfigure(2, weight=1)

        self.menu_frame.grid_rowconfigure(0, weight=1)

        for i in range(29):
            self.menu_frame.grid_rowconfigure(i+1, weight=5)
        self.menu_frame.grid_rowconfigure(30, weight=1)

        # Create list frame
        self.list_frame = tk.Frame(self.root, bg="white")
        self.list_frame.grid(row=0, column=1, sticky="nswe")
        self.list_frame.grid_columnconfigure(0, weight=1)
        self.list_frame.grid_columnconfigure(1, weight=1)
        self.list_frame.grid_columnconfigure(2, weight=1)
        for i in range(31):
            self.list_frame.grid_rowconfigure(i+1, weight=5)

        self.writing_frame = tk.Frame(self.root, bg='darkgrey')


        self.example_mail = tk.Button(self.list_frame, text='Example mail', bg="darkgray", relief="flat")
        self.example_mail.grid(row=1, column=0, columnspan = 200,  sticky='nswe')

        # Display frame
        # create display frame
        self.display_frame = tk.Frame(self.root,bg="lightgray")
        self.display_frame.grid(row=0, column=2, sticky="nswe")
        self.display_frame.grid_rowconfigure(0, weight=1)
        self.display_frame.grid_rowconfigure(1, weight=1)
        self.display_frame.grid_rowconfigure(2, weight=30)

        self.display_frame.grid_columnconfigure(0, weight=1)



        self.sender_label = tk.Label(self.display_frame, anchor='w',justify='left', text='sender: ' + self.mail_dict['hash']['sender'])
        self.sender_label.config(font=("Helvetica", 14))
        self.sender_label.grid(row=0, column=0, padx=10, pady=10, sticky="nswe")



        self.betreff_label = tk.Label(self.display_frame, anchor='w',justify='left', text='betreff: ' + self.mail_dict['hash']['betreff'])
        self.betreff_label.config(font=("Helvetica", 14))
        self.betreff_label.grid(row=1, column=0, padx=10, pady=10, sticky="nswe")

        self.text_label = tk.Label(self.display_frame, anchor='nw',justify='left', text=self.mail_dict['hash']['text'])
        self.text_label.config(font=("Helvetica", 14))
        self.text_label.grid(row=2, column=0, padx=10, pady=10,sticky="nsew")

        self.sender_label.grid(row=0, column=0)
        self.betreff_label.grid(row=1, column=0)
        self.text_label.grid(row=2, column=0)


        # account settings frame
        self.account_frame = tk.Frame(self.root, bg="grey")
        self.account_frame.grid_columnconfigure(0, weight=1)  # Display frame: 1/2 of the total width
        self.account_frame.grid_columnconfigure(1, weight=10)  # Display frame: 1/2 of the total width

        # settings frame
        self.settings_frame = tk.Frame(self.root, bg="grey")
        self.settings_frame.grid_columnconfigure(0, weight=1)  # Display frame: 1/2 of the total width
        self.settings_frame.grid_columnconfigure(1, weight=10)  # Display frame: 1/2 of the total width



        # menu buttons
        self.collapse_button = self.add_icon_button(self.menu_frame, self.collapse_menu_icon, self.collapse_menu)
        self.write_mail_button = self.add_icon_button(self.menu_frame, self.write_mail_icon, self.write_mail)
        self.reload_button = self.add_icon_button(self.menu_frame, self.reload_icon, self.reload_inboxes)

        self.all_mails = tk.Button(self.menu_frame, text='all mails', bg="darkgray", relief="flat")

        self.account_settings_button = self.add_icon_button(self.menu_frame, self.account_icon, self.account_settings)
        self.general_settings_button = self.add_icon_button(self.menu_frame, self.settings_icon, self.general_settings)




        self.exit_account_button = self.add_icon_button(self.account_frame, self.back_icon, self.exit_to_main)
        self.login_button = tk.Button(self.account_frame, text='login', bg="darkgray", relief="flat")

        self.exit_settings_button = self.add_icon_button(self.settings_frame, self.back_icon, self.exit_to_main)
        self.example_setting = tk.Button(self.settings_frame, text='Example Setting', bg="darkgray", relief="flat")

        self.collapse_menu()

        # Add labels for menu options



    def resize_icon(self, image_path, target_width):
        image = PhotoImage(file=image_path)
        original_width = image.width()
        scale_factor = original_width // target_width
        resized_image = image.subsample(scale_factor)
        return resized_image

    def add_icon_button(self, frame, image_path, command):
        try:
            icon = self.resize_icon(image_path, 24)
            button = tk.Button(frame, image=icon, command=command, bg="lightgray", relief="flat")
            button.image = icon  # Keep a reference to prevent garbage collection
            return button
        except Exception as e:
            print(f"Error loading icon from {image_path}: {e}")

    # Placeholder functions for button actions
    def write_mail(self):
        self.menu_frame.grid_forget()
        self.list_frame.grid_forget()
        self.display_frame.grid_forget()

        self.writing_frame.grid(row=0, column=0, sticky='nwes', columnspan=3)
        self.empfänger_label = tk.Label(self.writing_frame, text = "Recipient")
        self.betreff_editor_label = tk.Label(self.writing_frame, text = "Subject")

        self.writing_frame.grid_columnconfigure(0, weight=1)
        self.writing_frame.grid_columnconfigure(1, weight=10)
        self.writing_frame.grid_columnconfigure(2, weight=1)


        self.mail_writer = tk.Text(self.writing_frame, height=30)
        self.betreff_writer = tk.Text(self.writing_frame, height=3, width=15)
        self.empfänger_writer = tk.Text(self.writing_frame, height=3, width=15)

        self.add_icon_button(self.writing_frame, self.back_icon, self.exit_to_main).grid(row=0, column=0, sticky='nswe')
        self.add_icon_button(self.writing_frame, self.send_icon, self.send_mail).grid(row=0, column=2, sticky='nswe')

        self.empfänger_label.grid(row=0, column=1, sticky='nwes')
        self.empfänger_writer.grid(row=1, column=1, sticky='nwes')
        self.betreff_editor_label.grid(row=2, column=1, sticky='nwes')
        self.betreff_writer.grid(row=3, column=1, sticky='nwes')
        tk.Label(self.writing_frame, text = "Text").grid(row=4, column=1, sticky='nwes')
        self.mail_writer.grid(row=5, column=1, sticky='nwes')

        print("Write Mail Button Pressed")

    def reload_inboxes(self):
        print("Reload Inboxes Button Pressed")

    def collapse_menu(self):
        print("Collapse Menu Button Pressed")
        if self.is_collapsed:
            self.is_collapsed = False
            self.root.grid_columnconfigure(0, weight=self.menues_weight)

            # move buttons
            self.collapse_button.grid(row=0, column=2, pady=5, sticky='nswe')
            self.reload_button.grid(row=0, column=1, pady=5, sticky='nswe')
            self.write_mail_button.grid(row=0, column=0, pady=5, sticky='nswe')
            self.account_settings_button.grid(row=30, column=0, pady=5, sticky='nswe')
            self.general_settings_button.grid(row=30, column=2, pady=5, sticky='nswe')

            # move inboxes
            self.all_mails.grid(row=1, column=0, columnspan=3, sticky='nswe')
        else:
            self.is_collapsed = True
            self.root.grid_columnconfigure(0, weight=1)

            # destroy buttons
            self.all_mails.grid_forget()
            self.collapse_button.grid(row=0, column=0)
            self.reload_button.grid_forget()
            self.write_mail_button.grid_forget()
            self.account_settings_button.grid_forget()
            self.general_settings_button.grid_forget()


    def account_settings(self):
        print("Account Settings Button Pressed")
        self.menu_frame.grid_forget()
        self.list_frame.grid_forget()
        self.display_frame.grid_forget()
        self.account_frame.grid(row=0, column=0, columnspan=3,sticky="nswe")
        self.exit_account_button.grid(row=0, column=0)
        self.login_button.grid(row=1, column=0, sticky='nswe')


    def general_settings(self):
        print("General Settings Button Pressed")
        self.menu_frame.grid_forget()
        self.list_frame.grid_forget()
        self.display_frame.grid_forget()
        self.settings_frame.grid(row=0, column=0, columnspan=3, sticky="nswe")
        self.exit_settings_button.grid(row=0, column=0)
        self.example_setting.grid(row=1, column=0, sticky='nswe')

    def exit_to_main(self):
        print('exit account pressed')
        self.account_frame.grid_forget()
        self.settings_frame.grid_forget()
        self.writing_frame.grid_forget()
        self.root.grid_columnconfigure(0, weight=self.menues_weight)  # Menu frame: 1/4 of the total width
        self.root.grid_columnconfigure(1, weight=self.menues_weight)  # List frame: 1/4 of the total width
        self.root.grid_columnconfigure(2, weight=self.main_field_weight)  # Display frame: 1/2 of the total width
        self.root.grid_rowconfigure(0, weight=1)  # Make row 0 fill the available heigh$

        self.list_frame.grid(row=0, column=1, sticky="nswe")
        self.display_frame.grid(row=0, column=2, sticky="nswe")
        self.menu_frame.grid(row=0, column=0, sticky="nswe")



    def send_mail(self):
        pass


if __name__ == "__main__":
    app = EmailApp()
    app.root.mainloop()
