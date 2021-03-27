from threading import Thread
from urllib.request import urlopen

def open_website(url):
    return urlopen(url)


if __name__ == "__main__":
    while True:
        try:
            enter_user_no = int(input("enter no"))
            if enter_user_no == 0:
                break
        except:
            print("That's not a valid option!")

        Thread(target=open_website, args=["http://127.0.0.1:8000/enter_store/"]).start()

    print("no more User no present")