from sympy import solveset, symbols, solve, N
from sympy import sqrt

d, X1, X2, Y1, Y2= symbols("d X1 X2 Y1 Y2")


def calcDistance():
    while True:
        try:
            x1In = input("X1 = ")
            y1In = input("Y1 = ")
            x2In = input("X2 = ")
            y2In = input("Y2 = ")
            print("ayyy")
            expr = sqrt((X2 - X1)**2 + (Y2 - Y1)**2) - d
            expr2 = ((X2 - X1)**2 + (Y2 - Y1)**2)**(1/2) - d
            print("lmao")
            expr = expr.subs(X1, x1In)
            expr = expr.subs(X2, x2In)
            expr = expr.subs(Y1, y1In)
            expr = expr.subs(Y2, y2In)
            expr2 = expr2.subs(X1, x1In)
            expr2 = expr2.subs(X2, x2In)
            expr2 = expr2.subs(Y1, y1In)
            expr2 = expr2.subs(Y2, y2In)
            print("\nResults:")
            sol = N(expr2)
            sol = solve(sol, d)
            expr = solve(expr, d)
            
            print("Bruh moment")
            print("Sqrt: \t\t", expr)
            print("Decimal : \t", str(sol))
            closer = str(input("\nEnter 1 to exit.\n"
            "Press any key to continue.\n"))
            if(closer == '1'):
                return
        except:
            print("Invalid Character")

if __name__ == "__main__":
	calcDistance()

