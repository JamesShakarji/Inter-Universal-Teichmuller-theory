# takes as input an IUT Galois representation (given as a dictionary mapping element names to angles) and a complex number s, and returns the value of the 
# L-function of the Galois representation at s. The L-function is computed by looping over the elements of the Galois representation and multiplying the current 
# value of the L-function by the contribution of each element to the L-function. The contribution of an element is computed using the angle associated with the element.

def L_function_IUT_Galois_rep(Galois_rep, s):
    """Computes the L-function of an inter-universal Teichmuller (IUT) Galois representation."""
    # Initialize the L-function value to 1
    L = 1
    # Loop over the elements of the Galois representation
    for g, angle in Galois_rep.items():
        # Compute the contribution of this element to the L-function
        L *= 1 / (1 - complex(cos(angle), sin(angle)) * s)
    # Return the L-function value
    return L

# Example usage: Compute the L-function of an IUT Galois representation
Galois_rep = {'a': 2*pi, 'b': 3*pi}  # Example IUT Galois representation
s = complex(-1, 0.5)  # Example complex number
L = L_function_IUT_Galois_rep(Galois_rep, s)
print(f'L-function of IUT Galois representation: {L}')

