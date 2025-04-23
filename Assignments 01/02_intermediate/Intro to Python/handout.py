# Dictionary with planets and their gravity multipliers
planet_gravity = {
    'Mercury': 37.6,
    'Venus': 88.9,
    'Mars': 37.8,
    'Jupiter': 236.0,
    'Saturn': 108.1,
    'Uranus': 81.5,
    'Neptune': 114.0
}

def main():
    # Get the user's weight on Earth
    earth_weight = float(input("Enter a weight on Earth: "))
    
    # Get the planet name from the user
    planet = input("Enter a planet: ")
    
    # Calculate the equivalent weight on the chosen planet
    if planet in planet_gravity:
        weight_on_planet = earth_weight * (planet_gravity[planet] / 100)
        print(f"The equivalent weight on {planet}: {round(weight_on_planet, 2)}")
    else:
        print("Invalid planet name!")

if __name__ == "__main__":
    main()
