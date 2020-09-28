"""Given an IVP, we use initial x and y, with a calculated slope of
x0 and y0 to recursively solve n solutions at an h interval


print(initY<<1 + initY) In operations it stays to equal 2 for both variables."""


def dydx(t, v):
    return 9.8 - (.1 * v)


def problem5(initX=0.0, initY=0, h=0.25, xn=1.5, newX=0.0):
    """

    :param initX: recursive param
    :param initY: recursive param
    :param h: factor for number of computations
    :param xn: Last desired output. New Y is computed right before this. The next row, only real calculation is dydx, the requirements are already supplied.
    :param newX: Rarest case, once this equals Xn, we stop the process
    :return:


    Rarest case is newX(default, but not constant)= xn(default constant). Thus the method will return current x and y values
    """
    if newX >= xn or newX > (xn - 0.000111111):
        print("X at %f = %f" % (xn, initX))
        print("Y when X = %f :%f" % (initX, initY))
        return initX, initY

    derivative = dydx(initX, initY)
    Yn = initY + h * derivative
    Xn = (initX + h)
    newX = Xn
    print("X = %f" % (Xn))
    print("Y = %f" % Yn)
    problem5(Xn, Yn, h, xn, newX)


problem5()
