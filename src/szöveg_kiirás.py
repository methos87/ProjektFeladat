import time


def gépelés(szöveg):
    print('\r')
    for i in szöveg:
        print(i, end='', flush=True)
        time.sleep(0.035)
    time.sleep(0.5)
    return ''
