"""
This module provides functions for calculating BMI and determining BMI category.
"""

import unittest
import subprocess

# Function to calculate BMI
def calculate_bmi(height_feet, height_inches, weight_pounds):
    """Calculate BMI based on height in feet, height in inches, and weight in pounds."""
    height_inches_total = height_feet * 12 + height_inches
    bmi = round((weight_pounds / (height_inches_total ** 2)) * 703, 1)
    return bmi

# Function to determine BMI category
def determine_bmi_category(bmi):
    """Determine BMI category based on BMI value."""
    if 0.1 <= bmi < 18.5:
        return "Underweight"
    if 18.5 <= bmi <= 24.9:
        return "Normal weight"
    if 25 <= bmi <= 29.9:
        return "Overweight"
    if 30 <= bmi:
        return "Obese"
    return "invalid 0 or negative bmi"

class TestBMI(unittest.TestCase):
    """Test class for BMI functions."""
    def test_pylint(self):
        """Test Pylint."""
        result = subprocess.run(['pylint', 'bmi.py'], capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 0, "Pylint found issues in bmi.py:\n" + result.stdout)

    def test_underweight_boundary(self):
        """Test BMI category determination for underweight boundary."""
        self.assertEqual(determine_bmi_category(0), "invalid 0 or negative bmi")
        self.assertEqual(determine_bmi_category(0.1), "Underweight")
        self.assertEqual(determine_bmi_category(9.2), "Underweight")
        self.assertEqual(determine_bmi_category(18.3), "Underweight")
        self.assertEqual(determine_bmi_category(18.4), "Underweight")

    def test_normal_weight_boundary(self):
        """Test BMI category determination for normal weight boundary."""
        self.assertEqual(determine_bmi_category(18.4), "Underweight")
        self.assertEqual(determine_bmi_category(18.5), "Normal weight")
        self.assertEqual(determine_bmi_category(21.5), "Normal weight")
        self.assertEqual(determine_bmi_category(24.9), "Normal weight")
        self.assertEqual(determine_bmi_category(25), "Overweight")

    def test_overweight_boundary(self):
        """Test BMI category determination for overweight boundary."""
        self.assertEqual(determine_bmi_category(24.9), "Normal weight")
        self.assertEqual(determine_bmi_category(25), "Overweight")
        self.assertEqual(determine_bmi_category(27.4), "Overweight")
        self.assertEqual(determine_bmi_category(29.9), "Overweight")
        self.assertEqual(determine_bmi_category(30), "Obese")

    def test_obese_boundary(self):
        """Test BMI category determination for obese boundary."""
        self.assertEqual(determine_bmi_category(29.9), "Overweight")
        self.assertEqual(determine_bmi_category(30), "Obese")

def main():
    """Main function."""
    while True:
        print("Choose an option:")
        print("1. Input height and weight to calculate BMI")
        print("2. Run test cases")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                height_feet = int(input("Enter your height in feet: "))
                height_inches = int(input("Enter your height in inches: "))
                weight_pounds = float(input("Enter your weight in pounds: "))

                bmi = calculate_bmi(height_feet, height_inches, weight_pounds)
                print("Your BMI is:", bmi)
                print("BMI Category:", determine_bmi_category(bmi))
            except ValueError:
                print("Invalid input. Please enter numerical values for height and weight.")
        elif choice == "2":
            suite = unittest.TestLoader().loadTestsFromTestCase(TestBMI)
            unittest.TextTestRunner(verbosity=2).run(suite)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == '__main__':
    main()
