# Sinusoids and Signals
import numpy as np
import matplotlib.pyplot as plt

def sinusoid_to_phasor(A, w, t, phi):
    phasor = A * np.exp(1j * (w * t + phi))
    return phasor

# Set parameters
A = 3      
w = 2 * np.pi * 50  
t = 1     
phi = np.pi / 4  
phasor = sinusoid_to_phasor(A, w, t, phi)
print("Phasor representation of the sinusoid:")
print(f"Phasor: {phasor:.2f} (Magnitude: {np.abs(phasor):.2f}, Angle: {np.angle(phasor, deg=True):.2f} degrees)" )
print()

# Shows Argand Diagram
plt.figure(figsize=(10,4))
arg_ax = plt.subplot(1, 2, 1)
plt.quiver(0, 0, phasor.real, phasor.imag, angles='xy', scale_units='xy', scale=1, color='r')
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')
plt.xlim(-A-1, A+1)
plt.ylim(-A-1, A+1)
plt.title('Argand Diagram of Phasor')
plt.xlabel('Real Part')
plt.ylabel('Imaginary Part')
plt.grid()
plt.gca().set_aspect('equal', adjustable='box')

# Show graph as a function of time
t_vals = np.linspace(0, 0.1, 1000)
sinusoid_vals = A * np.sin(w * t_vals + phi)
freq_ax = plt.subplot(1, 2, 2)

plt.plot(t_vals, sinusoid_vals)
plt.title('Sinusoid Signal over Time')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid()
plt.show()
