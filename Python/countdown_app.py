import tkinter as tk
import time
import threading
import random

class CountdownApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown App")
        self.root.geometry("300x200")

        # Initialize state variables
        self.countdown_thread = None
        self.is_counting = False

        # Create frames
        self.initial_frame = tk.Frame(self.root)
        self.countdown_frame = tk.Frame(self.root)

        # Initial frame: Start Countdowns and Shut Down buttons
        self.start_button = tk.Button(self.initial_frame, text="Start Countdowns", command=self.start_countdowns)
        self.start_button.pack(pady=20)
        self.initial_shutdown_button = tk.Button(self.initial_frame, text="Shut Down", command=self.shutdown)
        self.initial_shutdown_button.pack(pady=20)

        # Countdown frame: 90-minute countdown label and Shut Down button
        self.countdown_label = tk.Label(self.countdown_frame, text="90:00", font=("Arial", 24))
        self.countdown_label.pack(pady=20)
        self.countdown_shutdown_button = tk.Button(self.countdown_frame, text="Shut Down", command=self.stop_countdowns)
        self.countdown_shutdown_button.pack(pady=20)

        # Show initial frame
        self.initial_frame.pack()

    def start_countdowns(self):
        # Disable start button and switch to countdown frame
        self.start_button.config(state="disabled")
        self.initial_frame.pack_forget()
        self.countdown_frame.pack()

        # Start countdown process
        self.is_counting = True
        self.countdown_thread = threading.Thread(target=self.countdown_loop, daemon=True)
        self.countdown_thread.start()

        # Start updating the 90-minute countdown display
        self.update_90min_countdown(5400)  # 90 minutes in seconds

    def stop_countdowns(self):
        # Stop countdowns and return to initial frame
        self.is_counting = False
        self.countdown_frame.pack_forget()
        self.initial_frame.pack()
        self.start_button.config(state="normal")

    def shutdown(self):
        # Terminate the application
        self.root.quit()

    def update_90min_countdown(self, remaining):
        if self.is_counting and remaining >= 0:
            minutes = remaining // 60
            seconds = remaining % 60
            self.countdown_label.config(text=f"{minutes:02d}:{seconds:02d}")
            self.root.after(1000, self.update_90min_countdown, remaining - 1)

    def countdown_loop(self):
        # Run for 90 minutes (5400 seconds)
        start_time = time.time()
        ninety_minutes = 90 * 60

        while self.is_counting and (time.time() - start_time < ninety_minutes):
            # Random interval between 3 to 5 minutes (180 to 300 seconds)
            interval = random.randint(180, 300)
            # Sleep for the interval, checking periodically to allow interruption
            elapsed = 0
            while elapsed < interval and self.is_counting:
                time.sleep(1)
                elapsed += 1
            if self.is_counting:
                self.root.after(0, self.show_countdown, 10)

        # After 90 minutes, trigger a 20-minute countdown if still counting
        if self.is_counting:
            self.root.after(0, self.show_countdown, 20 * 60)

    def show_countdown(self, seconds):
        # Create a new full-screen window
        countdown_window = tk.Toplevel(self.root)
        countdown_window.attributes("-fullscreen", True)
        countdown_window.configure(bg="black")

        # Label to display the countdown
        label = tk.Label(
            countdown_window,
            text="",
            font=("Arial", 100),
            fg="white",
            bg="black"
        )
        label.pack(expand=True)

        def update_countdown(remaining):
            if remaining >= 0:
                label.config(text=f"{remaining} seconds")
                countdown_window.after(1000, update_countdown, remaining - 1)
            else:
                countdown_window.destroy()
                # If this was the 20-minute countdown, exit the application
                if seconds == 20 * 60:
                    self.root.quit()

        # Start the countdown
        update_countdown(seconds)

        # Allow escape key to exit full-screen (optional, for testing)
        countdown_window.bind("<Escape>", lambda e: countdown_window.destroy())

if __name__ == "__main__":
    root = tk.Tk()
    app = CountdownApp(root)
    root.mainloop()