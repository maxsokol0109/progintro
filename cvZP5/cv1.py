import math

def main():
    print(round(tube_mass(0.060, 0.050, 6), 2), "kg")
    print(round(tube_mass(0.060, 0.050, 6, density=2700), 2), "kg") 



def circle_area(d):
    obsah = (d/2)**2 * math.pi
    return obsah

def tube_cross_section(d_out, d_in):
    cross_section = circle_area(d_out) - circle_area(d_in)
    return cross_section

def tube_mass(d_out, d_in, length, density=7850):
    return tube_cross_section(d_out,d_in) * length * density




print(f"{'Tloušťka (mm)':<15} | {'Hmotnost (kg)':<15}")

d_out = 0.06   
length = 6.0

for t_mm in range(1, 6):
    t_m = t_mm / 1000  
    d_in = d_out - 2 * t_m

    mass = tube_mass(d_out, d_in, length)
    
    print(f"{t_mm:<15} | {mass:<15.2f}")
