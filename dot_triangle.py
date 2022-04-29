import logging
import math


def main():
    logging.basicConfig(
        level=logging.DEBUG,
        filename="dot_log.log",
        format="%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
        datefmt='%H:%M:%S',
    )

    with open('dot_input.txt', 'r') as file_in:
        d = int(file_in.readline().strip())
        x, y = (int(x) for x in file_in.readline().strip().split())

    if 0 <= x <= d and 0 <= y <= d and x + y <= d:
        result = 0
        logging.info(f'result inside = {result}')
    else:
        ax = math.sqrt(x**2 + y**2)
        bx = math.sqrt((x - d)**2 + y**2)
        cx = math.sqrt(x**2 + (y - d)**2)
        distances = list(enumerate([ax, bx, cx], 1))
        min_distance = min(distances, key=lambda i: i[1])
        result = min_distance[0]
        logging.info(f'distances = {distances}')
        logging.info(f'result outside = {result}, min_dist = {min_distance}')

    with open('dot_output.txt', 'w') as file_out:
        file_out.write(str(result))


main()
