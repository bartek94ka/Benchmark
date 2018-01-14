import tkinter as tk
import drive_handler
from FileTransferManager import FileTransferManager
from FileCleaner import FileCleaner
from FileGenerator import FileGenerator
import time
import threading
import matplotlib.pyplot as plt


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        self.is_copying = False
        self.copying_speed = []
        self.copying_time = []
        self.copying_avg = 0

        tk.Tk.__init__(self, *args, **kwargs)
        self.om_variable = tk.StringVar(self)
        self.l2_var = tk.StringVar(self)

        self.e1_var = tk.StringVar(self)
        self.e2_var = tk.StringVar(self)

        l0 = tk.Label(self, text="", width=12)
        self.b1 = tk.Button(self, text="Check for drives", width=14, command=self.check_for_drives)
        l1 = tk.Label(self, text="Choose drive letter:", width=14)
        self.l2 = tk.Label(self, textvariable=self.l2_var)

        self.b2 = tk.Button(self, text="Start test", width=14, command=self.on_drive_click)

        self.b3 = tk.Button(self, text="Show figure", width=14, state=tk.DISABLED, command=self.make_plot)

        l3 = tk.Label(self, text="Ammount of files:", width=14)
        e1 = tk.Entry(self, textvariable=self.e1_var)

        l4 = tk.Label(self, text="Test file size:", width=14)
        e2 = tk.Entry(self, textvariable=self.e2_var)

        self.om = tk.OptionMenu(self, self.om_variable, (), command=self.on_drive_click)
        self.om.configure(width=20)
        self.check_for_drives()

        l1.grid(column=0, row=0)
        self.om.grid(column=1, row=0)
        self.b1.grid(column=2, row=0)

        l0.grid(column=0, row=1)

        l3.grid(column=0, row=2)
        e1.grid(column=1, row=2)
        l4.grid(column=0, row=3, sticky=tk.E)
        e2.grid(column=1, row=3)

        l0.grid(column=0, row=4)

        self.b2.grid(column=0, row=5)
        self.l2.grid(column=1, row=5)
        self.b3.grid(column=2, row=5)

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
        self.b1.configure(state=tk.DISABLED)
        self.b2.configure(state=tk.DISABLED)
        self.b3.configure(state=tk.DISABLED)
        self.copying_speed = [0]
        self.copying_time = [0]
        self.copying_avg = 0
        self.thread = threading.Thread(target=self.run_test)
        self.thread.start()

    def measure_space(self):
        wait_time = 0.1
        tmp_total = 0
        free_space = drive_handler.get_transfer_speed(self.om_variable.get())
        while self.is_copying:
            time.sleep(wait_time)
            tmp_total += wait_time
            speed = (free_space - drive_handler.get_transfer_speed(self.om_variable.get()))/tmp_total
            speed = round(speed/1024/1024, 2)
            self.copying_speed.append(speed)
            self.copying_time.append(round(tmp_total, 2))
            self.l2_var.set("Speed: " + str(speed) + "MB/s.")
            print("Speed: " + str(speed) + "MB/s.")
        print(self.copying_speed)

    def run_test(self):
        self.l2_var.set("Generating files. Please wait.")
        source_dir = FileGenerator.GenerateTestFiles("C:", int(self.e1_var.get()), int(self.e2_var.get()))

        self.is_copying = True
        thread2 = threading.Thread(target=self.measure_space)
        thread2.start()
        time.sleep(0.1)
        free_space_before = drive_handler.get_transfer_speed(self.om_variable.get())

        start = time.time()
        target_dir = FileTransferManager.copyFilesFromSpecificDirectory(source_dir, self.om_variable.get())
        end = time.time()
        self.is_copying = False

        free_space_after = drive_handler.get_transfer_speed(self.om_variable.get())

        FileCleaner.RemoveDirectoryWithFiles(source_dir)
        FileCleaner.RemoveDirectoryWithFiles(target_dir)

        time.sleep(1)

        self.l2_var.set("AVG speed: " + str(round((free_space_before - free_space_after) / 1024 / 1024 / (end - start), 2)) + "MB/s")
        self.copying_avg = round((free_space_before - free_space_after) / 1024 / 1024 / (end - start), 2)
        print("AVG speed: " + str(round((free_space_before - free_space_after) / 1024 / 1024 / (end - start), 2)) + "MB/s")
        self.b1.configure(state=tk.NORMAL)
        self.b2.configure(state=tk.NORMAL)
        self.b3.configure(state=tk.NORMAL)

    def make_plot(self):
        while self.thread.is_alive():
            time.sleep(1)
        plt.plot(self.copying_time, self.copying_speed)
        plt.gcf().canvas.set_window_title("Test result")
        plt.xlabel('Time [s]')
        plt.ylabel('Speed [MB/s]')
        plt.title("Drive - " + self.om_variable.get() + " | " + drive_handler.get_drive_info(self.om_variable.get()) +
                  " | Test data files: " + self.e1_var.get() + "x" + self.e2_var.get() + " MB\n" +
                  "Average copying speed: " + str(self.copying_avg) + "MB/s")
        plt.ylim(ymin=0)
        plt.xlim(xmin=0)
        plt.show()

if __name__ == "__main__":
    app = SampleApp()
    app.title('Drive Speed Master')
    app.mainloop()
