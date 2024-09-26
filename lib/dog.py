#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="", breed="Mutt"):
        # Initialize attributes directly
        self._name = None
        self._breed = None
        self.name = name  # Use property setter for validation
        self.breed = breed  # Use property setter for validation

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            print("Name must be a string between 1 and 25 characters.")
    
    @property
    def breed(self):
        return self._breed
    
    @breed.setter
    def breed(self, value):
        if value in APPROVED_BREEDS or value == "Mutt":
            self._breed = value
        else:
            print("Breed must be in list of approved breeds.")

# Example usage
if __name__ == "__main__":
    dog1 = Dog(name="Rex", breed="Pug")  # Valid breed
    print(f"Dog1: Name={dog1.name}, Breed={dog1.breed}")

    dog2 = Dog(name="Rex", breed="Unknown Breed")  # Invalid breed
    print(f"Dog2: Name={dog2.name}, Breed={dog2.breed}")

    dog3 = Dog(name="Buddy")  # Default breed
    print(f"Dog3: Name={dog3.name}, Breed={dog3.breed}")
