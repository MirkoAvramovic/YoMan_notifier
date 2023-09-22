"""
Title: Windows Toast Notification with winotify

Description:
This script demonstrates how to create and display a Windows toast notification using the winotify library in Python. The notification includes a custom icon and a custom action.

Usage:
1. Make sure you have the winotify library installed:
2. Replace the icon path (icon) with the absolute path to your custom icon file.
3. Customize the app_id, title, msg, and action URL to fit your notification's purpose.
4. Run the script to display the toast notification.

Author: Mirko Avramovic
Date: September 22, 2023
"""
from winotify import Notification, audio

# Create a Notification object
toast = Notification(app_id="YoMan Script", # Application ID for the notification
                     title="Job Offer", # Title of the notification
                     msg="Do you need a Backend Developer Junior?", # Message body of the notification
                     duration="long", # Duration of the notification ("short" or "long")
                     icon=r"C:\Users\MyProjects\YoMan_notifier\bell.png") # Path to the custom icon

# Set audio for the notification
toast.set_audio(audio.SMS, loop=False) # Use SMS audio with no loop

# Add a custom action to the notification
toast.add_actions(label="Hire Me!", # Label for the action button
                  launch="https://www.linkedin.com/in/mirkoavramovic") # URL to launch when the action is clicked

# Display the notification
toast.show()