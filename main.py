from winotify import Notification, audio

toast = Notification(app_id="YoMan Script",
                     title="Job Offer",
                     msg="Do you need a Backend Developer Junior?",
                     duration="long",
                     icon=r"C:\Users\mirko\OneDrive\Radna površina\Python projekti\YoMan_notify\bell.png")

toast.set_audio(audio.SMS, loop=False)
toast.add_actions(label="Hire Me!", launch="https://www.linkedin.com/in/mirkoavramovic")

toast.show()