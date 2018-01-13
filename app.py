import tkinter as tk
import drive_handler
from FileTransferManager import FileTransferManager
import os
import time
import threading


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        self.is_copying = False
        tk.Tk.__init__(self, *args, **kwargs)
        self.om_variable = tk.StringVar(self)
        self.l2_var = tk.StringVar(self)

        b1 = tk.Button(self, text="Reset", width=8, command=self.check_for_drives)
        l1 = tk.Label(self, text="Select drive to test:", width=22)
        self.l2 = tk.Label(self, textvariable=self.l2_var)

        b2 = tk.Button(self, text="Check", width=8, command=self.on_drive_click)

        self.om = tk.OptionMenu(self, self.om_variable, (), command=self.on_drive_click)
        self.om.configure(width=20)
        self.check_for_drives()

        b1.grid(column=0, row=0, sticky="W")
        l1.grid(column=1, row=0)
        self.om.grid(column=2, row=0, sticky="W")
        self.l2.grid(column=1, row=1)
        b2.grid(column=0, row=1)

    def _reset_option_menu(self, options, index=None):
        '''reset the values in the option menu

        if index is given, set the value of the menu to
        the option at the given index
        '''
        menu = self.om["menu"]
        menu.delete(0, "end")
        for string in options:
            menu.add_command(label=string, command=lambda value=string: self.om_variable.set(value))
        if index is not None:
            self.om_variable.set(options[index])

    def check_for_drives(self):
        '''Switch the option menu to display colors'''
        self._reset_option_menu(drive_handler.get_drives_list(), 0)

    def on_drive_click(self):
        self.l2_var.set(drive_handler.get_drive_info(self.om_variable.get()))
        thread = threading.Thread(target=self.run_test)
        thread.start()
        thread2 = threading.Thread(target=self.measure_space)
        thread2.start()

    def measure_space(self):
        wait_time = 0.5
        tmp_total = 0
        free_space = drive_handler.get_transfer_speed(self.om_variable.get())
        while self.is_copying:
            time.sleep(wait_time)
            tmp_total += wait_time
            speed = (free_space - drive_handler.get_transfer_speed(self.om_variable.get()))/tmp_total
            print(speed/1024/1024)


    def run_test(self):
        free_space_before = drive_handler.get_transfer_speed(self.om_variable.get())
        self.is_copying = True
        start = time.time()
        sourceFile = os.getcwd() + '\\GeneratedFiles\\File_100_MB.txt'
        destinationPath = self.om_variable.get() + '\\'
        FileTransferManager.copyFile(sourceFile, destinationPath)
        end = time.time()
        self.is_copying = False
        free_space_after = drive_handler.get_transfer_speed(self.om_variable.get())
        print("Speed: " + str((free_space_before-free_space_after)/1024/1024/(end-start)))



if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
