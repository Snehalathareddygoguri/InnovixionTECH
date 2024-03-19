import tkinter as tk
from tkinter import messagebox
import time

# Defining a class
class AlarmClock:
    def __init__(self, m):
        self.m = m
        # Providing a title
        m.title("Alarm Clock")
        #Creating label for date
        self.date_label = tk.Label(m, text="Set Alarm Date (YYYY-MM-DD):")
        self.date_label.pack()
        #Creating entry
        self.date_entry = tk.Entry(m)
        self.date_entry.pack()
        #Creating Time Label
        self.time_label = tk.Label(m, text="Set Alarm Time (HH:MM):")
        self.time_label.pack()
        #Creating another Entry
        self.time_entry = tk.Entry(m)
        self.time_entry.pack()
        #Creating button which creates Alarm for Specified Time
        self.set_button = tk.Button(m, text="Set Alarm", command=self.set_alarm)
        self.set_button.pack()
 #Another function for input and checking
    def set_alarm(self):
        alarm_date = self.date_entry.get()
        alarm_time = self.time_entry.get()
        #Opening try block for taking input of date and time
        try:
            alarm_year, alarm_month, alarm_day = map(int, alarm_date.split('-'))
            alarm_hour, alarm_minute = map(int, alarm_time.split(':'))
            #Checks our date and time input with current time and date
            current_time = time.localtime()
            current_year, current_month, current_day = current_time.tm_year, current_time.tm_mon, current_time.tm_mday
            current_hour, current_minute = current_time.tm_hour, current_time.tm_min
            #If matches alerts as message defined in another def function below
            if (time.mktime((alarm_year, alarm_month, alarm_day, alarm_hour, alarm_minute, 0, 0, 0, 0)) >
                time.mktime((current_year, current_month, current_day, current_hour, current_minute, 0, 0, 0, 0))):
                time_difference_seconds = time.mktime((alarm_year, alarm_month, alarm_day, alarm_hour, alarm_minute, 0, 0, 0, 0)) - time.mktime((current_year, current_month, current_day, current_hour, current_minute, 0, 0, 0, 0))
                messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_date} {alarm_time}")
                self.m.after(int(time_difference_seconds), self.alert)
            else:
                messagebox.showwarning("Invalid Input", "Please enter a future date and time")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid date in YYYY-MM-DD and time in HH:MM format")
    #Alerts if alarm time matches with current time
    def alert(self):
        messagebox.showinfo("Alarm", "Wake up!")
#Main Function
def main():
    root = tk.Tk()
    alarm_clock = AlarmClock(root)
    root.mainloop()
#Calling main function
if __name__ == "__main__":
    main()