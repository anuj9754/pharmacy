import threading
import time
from random import randint
from threading import Thread
import asyncio

enter_customer_count = 0
customer_denied = 0
enter_pharm_counter = 0
enter_cash_count = 0
waiting_for_counter = 0


class Pharmacy:

    def enter_pharmacy_counter(self):
        global enter_pharm_counter
        if no_of_counter > enter_pharm_counter and enter_pharm_counter < 0:
            enter_pharm_counter += 1
            time.sleep(randint(1, 3))
            enter_pharm_counter -= 1
        return

    def enter_cash_counter(self):
        global enter_cash_count

        while True:
            if no_of_cash_counter > enter_cash_count:
                enter_cash_count += 1
                time.sleep(randint(1, 3))
                enter_cash_count -= 1
                break
        return

    def check_pharmacy_free(self):
        global enter_pharm_counter, waiting_for_counter
        if no_of_counter > enter_pharm_counter:
            waiting_for_counter -= 1
            return True
        return False

    def check_enter_waiting(self):
        global waiting_for_counter

        waiting_for_counter += 1
        return

    def waiting_list(self):
        global waiting_for_counter

        if waiting_for_counter != waiting_limit:
            return True
        return False

    def enter_customer(self):
        global enter_customer_count, customer_denied

        enter_customer_count += 1
        res = self.waiting_list()
        if res:
            self.check_enter_waiting()
            while True:
                a = self.check_pharmacy_free()
                print(a)
                if a:
                    break
            self.enter_pharmacy_counter()
            self.enter_cash_counter()

        else:
            customer_denied += 1


if __name__ == "__main__":
    # a = Pharmacy()

    while True:
        try:
            no_of_counter = int(input("No of Pharm Counter Present:- "))
            no_of_cash_counter = int(input("No of Cash Counter Counter Present:- "))
            waiting_limit = int(input("Enter Waiting Limit:- "))
            break
        except:
            print("That's not a valid option!")

    while True:
        try:
            enter_user_no = int(input("enter no"))

            if enter_user_no == 0:
                break
            threading.Thread(target=Pharmacy().enter_customer()).start()

        except:
            print("That's not a valid option!")

    print("no more Customer no present")
    print("Today Customer Enter:- {}\nCustomer Denied:- {}".format(enter_customer_count, customer_denied))
