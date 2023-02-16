from datetime import datetime


def exceptions(error):
    with open("exceptions.txt", "a") as f:
        f.write(f"{error}       {now}\n")


format_ = "%H:%M:%S %m/%d/%Y"
now = datetime.now().strftime(format_)