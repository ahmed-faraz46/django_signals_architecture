"""
1. In what order listeners are being executed if multiple attached
2. What will happen with rest of the listeners if one listener fails
3. Are signals being executed in  synchronously or asynchronously
4. Function of dispatch_uuid
"""

from signals.signal import Signal

pre_enroll = Signal()
post_enroll = Signal()


class Student:
    def enroll(self):
        pre_enroll.send()
        print ('Enrolling student')
        post_enroll.send()


def before_enroll_one():
    print ('Before going to enroll do this')


def before_enroll_two():
    print ('Before going to enroll do this as well')


def send_email():
    print ('Sending Email .....')


pre_enroll.dispatch(before_enroll_one)
pre_enroll.dispatch(before_enroll_two)
post_enroll.dispatch(send_email)

std = Student()
std.enroll()

