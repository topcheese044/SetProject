import os
import multiprocessing, subprocess
from multiprocessing import Process
import following, PR
from threading import Thread

Thread(target=PR.py).start()
Thread(target=following.py).start()
