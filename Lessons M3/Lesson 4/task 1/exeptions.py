from datetime import datetime


def exceptions_func(error):
    with open("reg.py", "a") as f:
        f.write(f"{error}       {now}\n")


format_ = "%H:%M:%S %m/%d/%Y"
now = datetime.now().strftime(format_)