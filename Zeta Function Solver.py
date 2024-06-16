import mpmath as mp

# Set the precision (number of decimal places)
mp.mp.dps = 50  # Adjust this value based on the desired precision level

# Define the functional equation of the Riemann zeta function


def zeta_functional_equation(s):
    # The functional equation components
    pi_term = mp.pi**(s - 1)
    sin_term = mp.sin(mp.pi * s / 2)
    gamma_term = mp.gamma(1 - s)
    zeta_term = mp.zeta(1 - s)

    # Calculate the right-hand side of the equation
    rhs = 2**s * pi_term * sin_term * gamma_term * zeta_term
    return rhs

# Function to evaluate the zeta function at a given complex number and compare both sides of the functional equation


def evaluate_and_compare(s):
    # Evaluate the zeta function at s
    lhs = mp.zeta(s)

    # Evaluate the functional equation's RHS
    rhs = zeta_functional_equation(s)

    # Return both sides for comparison
    return lhs, rhs


# Example complex number
# First non-trivial zero
s_val = mp.mpc('0.5', '14.134725141734693790457251983562')

# Evaluate the functional equation
lhs, rhs = evaluate_and_compare(s_val)

# Print the results with high precision
print("Zeta(s) =")
print(mp.nstr(lhs, n=50))
print("\nFunctional Equation RHS =")
print(mp.nstr(rhs, n=50))
