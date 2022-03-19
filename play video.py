import cv2 as cv


def img2ascii(img):
    DENSITY = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
    img = cv.resize(img, (226, 40), interpolation=cv.INTER_LINEAR) # (226, 40) for python terminal
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    for rows in img:
        line = ""
        for element in rows:
            line += (DENSITY[int((len(DENSITY)-1) * element/255)])

        with open("ascii.txt", "a") as file:
            file.write(line + "\n")


def printImg():
    print("\n"*38)
    with open("ascii.txt", "r") as f:
        for line in f.readlines():
            print(line.strip())

    with open("ascii.txt", "w") as f:
        f.write("")



def main():
    vid = cv.VideoCapture('bad apple.mp4')

    while vid.isOpened():
        ret, frame = vid.read()
        if ret:
            # cv.imshow("Frame", frame)
            # cv.waitKey(17)
            img2ascii(frame)
            printImg()

        if cv.waitKey(25) & 0xFF == ord('q'):
            break

    vid.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
