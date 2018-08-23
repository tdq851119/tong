# -*- coding: utf-8 -*-
import random
class Random():
    def randomPhone(self):
        list = ["137", "157","186","177","137","166"]
        str = "0123456789"
        phoneNo=random.choice(list) + "".join(random.choice(str) for i in range(8))
        return phoneNo
