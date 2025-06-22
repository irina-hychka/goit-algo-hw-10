import random
import scipy.integrate as spi

def f(x):
    """
    Function to integrate: f(x) = x^2
    """
    return x ** 2

def monte_carlo_integration(func, a, b, num_points=1_000_000):
    """
    Estimate the integral of a function using the Monte Carlo method.
    """
    y_max = func(b)
    rect_area = (b - a) * y_max

    points_under_curve = 0
    for _ in range(num_points):
        # Generate a random point inside the rectangle
        rand_x = random.uniform(a, b)
        rand_y = random.uniform(0, y_max)
        # Check if the point lies under the graph of the function
        if rand_y <= func(rand_x):
            points_under_curve += 1

    return (points_under_curve / num_points) * rect_area

def analytical_integral(a, b):
    """
    Calculate the exact integral of f(x) = x^2 analytically.
    """
    return (b**3 / 3) - (a**3 / 3)

def quad_integral(func, a, b):
    """
    Calculate the integral using SciPy's quad method.
    """
    result, _ = spi.quad(func, a, b)
    return result

def main():
    a, b = 0, 2
    num_points = 1_000_000

    # Calculate results
    mc_result = monte_carlo_integration(f, a, b, num_points)
    analytical_result = analytical_integral(a, b)
    scipy_result = quad_integral(f, a, b)

    # Calculate errors
    mc_error = abs(mc_result - analytical_result)
    scipy_error = abs(scipy_result - analytical_result)

    # Print formatted output
    print()
    print("Comparison of Integration Methods:\n")
    print(f"{'Method':<35}{'Value':<15}{'Error'}")
    print("-" * 60)
    print(f"{'Analytical':<35}{analytical_result:<15.8f}{0.0:.8f}")
    print(f"{'SciPy quad':<35}{scipy_result:<15.8f}~0 ({scipy_error:.2e})")
    print(f"{f'Monte Carlo ({num_points:,} points)':<35}{mc_result:<15.8f}{mc_error:.8f}")
    print()

# Usage
if __name__ == "__main__":
    main()
