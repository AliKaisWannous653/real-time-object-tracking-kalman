import config
import time

import platform
import cv2
import sys
import psutil


def fbsCal ():
    next_time = time.time()
    fps = 1/(next_time - config.pre_time)
    config.FPS.append(fps)
    config.pre_time = next_time
    return fps


def print_system_info(cap):

    print("========== SYSTEM INFORMATION ==========")

    print(f"OS: {platform.platform()}")
    print(f"CPU: {platform.processor()}")
    print(f"Logical CPUs: {psutil.cpu_count(logical=True)}")
    print(f"Physical CPUs: {psutil.cpu_count(logical=False)}")
    print(f"RAM: {psutil.virtual_memory().total / (1024**3):.2f} GB")

    print(f"Python: {sys.version}")
    print(f"OpenCV: {cv2.version}")

    print("\n========== CAMERA INFORMATION ==========")

    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    fps = cap.get(cv2.CAP_PROP_FPS)

    print(f"Resolution: {int(width)} x {int(height)}")
    print(f"Camera FPS: {fps:.2f}")

    print("========================================")