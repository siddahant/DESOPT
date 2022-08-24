from scipy.optimize import minimize

# define objective function
fun = lambda x: (x[0] - x[2]) ** 2 + (x[1] + x[2] - 2) ** 2 + (x[3] - 1) ** 2 + (x[4] - 1) ** 2

# define constraint
const = ({'type': 'eq', 'fun': lambda x: x[0] + 3 * x[1]},
        {'type': 'eq', 'fun': lambda x: x[2] + x[3] - 2 * x[4]},
        {'type': 'eq', 'fun': lambda x: x[1] - x[4]})

# define boundary condition
bnds = ((-10, 10), (-10, 10), (-10, 10), (-10, 10), (-10, 10))


# set initial guesses
x0 = [0, 10, 2, 0, 10]

# main method
res = minimize(fun, x0, method='SLSQP', bounds=bnds, constraints=const)

print(res)
