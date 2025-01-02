# Number Adder Program

This is a simple Python program that calculates the sum of numbers from 1 to a user-defined number using a loop. It prompts the user for input, iterates over the numbers, and outputs the total sum.

## Features
- Takes user input to specify the upper limit for summing numbers.
- Uses a loop to calculate the sum of numbers from 1 to the input number.
- Includes input validation using the `pyinputplus` library to ensure only valid positive integers are entered.
- Displays the calculated sum.

## Requirements
- Python 3.13.1
- `pyinputplus` library (for input validation)

To install the `pyinputplus` library, run the following:

pip install pyinputplus

## Usage
1. Run the script.
2. The program will ask you: _"What number do you want to add?"_
3. Enter a positive integer (e.g., `5`).
4. The program will output the sum of all numbers from 1 to the entered number.

Example:

Enter a positive integer: 5 The sum of all numbers from 1 to 5 is 15.

## Code Explanation
1. **Input**: The program prompts the user for a number, ensuring it's a valid positive integer.
2. **Loop**: It uses a `for` loop to iterate from 1 to the number provided by the user and calculates the running total.
3. **Output**: The final sum is printed after the loop completes.

## License
This project is licensed under the MIT License.
