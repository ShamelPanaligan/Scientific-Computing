# Argand Diagram Interactive Plot
# Creates an interactive plot showing complex numbers as points/vectors on the complex plane. 
# Let users input complex numbers and see them plotted with their real and imaginary components. 
# Showsthe modulus (distance from origin) and argument (angle from positive real axis).

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import cmath

def plot_complex_number(z, color='blue'):
    z = complex(z)
    real_z = z.real
    imag_z = z.imag
    arg = cmath.phase(z)
    arg_degrees = np.degrees(arg)
    modulus = abs(z)
    r_radius = modulus * 0.25
    plt.figure(figsize=(8, 8))
    
    arc = patches.Arc((0, 0), 2*r_radius, 2*r_radius,  # width and height
                         angle=0, theta1=0, theta2=arg_degrees, 
                         color='gray', linestyle='--', alpha=0.7)    
    plt.gca().add_patch(arc)
    plt.plot([0, real_z], [0, imag_z], marker='o', color=color, markersize=10)

    plt.annotate(f'z={z}', (real_z, imag_z), 
                 xytext=(15, 15), textcoords='offset points')
    
    plt.annotate(f'Modulus={modulus:.2f}', (real_z/2, imag_z/2), 
                 xytext=(0, 0), textcoords='offset points', color=color)
    
    plt.annotate(f'Arg={arg_degrees:.2f}°', (r_radius, 0), 
                 xytext=(0, 5), textcoords='offset points', color='gray')
    
    plt.axhline(y=0, color='k', linewidth=0.5)
    plt.axvline(x=0, color='k', linewidth=0.5)
    plt.grid(True, alpha=0.3)
    plt.xlabel('Real axis')
    plt.ylabel('Imaginary axis')
    plt.title('Argand Diagram')
    plt.axis('equal')
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.show()

def main():
    while True:
        try:
            Real = input("Enter The Real Part of the Complex Number (eg.3) or type 'exit' to quit: ")
            Imag = input("Enter The Imaginary Part of the Complex Number (inluding the sign and the j, eg. +4j) or type 'exit' to quit: ")
            z = Real + Imag

            if 'j' not in z:
                print("[Please add 'j' to the imaginary part.]")
                raise ValueError
        
            if '+' not in z and '-' not in z[1:]:
                print("[Please include '+' or '-' in the imaginary part.]")
                raise ValueError
            if 'exit' in z.lower():
                print("Goodbye!")
                break
            
        except (IndexError, ValueError,TypeError):
            print()
            print("Invalid format.")
            continue
        
        plot_complex_number(z)
        again = input("\nWould you like to plot another? (y/n): ").lower()
        if again != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    print("Welcome to the Argand Diagram Interactive Plotter!")
    print("Please Enter a complex number in the form a+bj (e.g., 3+4j). Type 'exit' to quit.")
    main()