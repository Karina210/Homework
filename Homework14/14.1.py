# import argparse
import time

#
# parser = argparse.ArgumentParser()
#
# parser.add_argument('-n', '--name')
# parser.add_argument('-s', '--surname')
# parser.add_argument('-t', '--time', required=True)
# parser.add_argument('-m', '--minutes', required=True)
# parser.add_argument('-s', '--seconds', required=True)
#
#
#
# args = parser.parse_args()
import time
k = 5
while k != 0:
    print("Осталось времени: {} секунд".format(k))
    k -= 1
    time.sleep(1)

if __name__ == '__main__':
    pass
