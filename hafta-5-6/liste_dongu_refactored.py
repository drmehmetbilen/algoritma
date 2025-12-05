"""
Refactored version of liste_dongu.py
Generates random numbers and performs statistical calculations with improved code structure.
"""

import random
from typing import List, Tuple


class NumberStatistics:
    """A class to handle random number generation and statistical calculations."""
    
    def __init__(self, count: int = 11, min_range: int = 0, max_range: int = 100):
        """
        Initialize the NumberStatistics class.
        
        Args:
            count: Number of unique random numbers to generate
            min_range: Minimum value for random numbers
            max_range: Maximum value for random numbers
        """
        self.count = count
        self.min_range = min_range
        self.max_range = max_range
        self.numbers: List[int] = []
    
    def generate_unique_numbers(self) -> List[int]:
        """
        Generate a list of unique random numbers.
        
        Returns:
            List of unique random numbers
        """
        self.numbers = []
        while len(self.numbers) < self.count:
            new_number = random.randint(self.min_range, self.max_range)
            if new_number not in self.numbers:
                self.numbers.append(new_number)
        return self.numbers
    
    def calculate_sum(self) -> int:
        """Calculate the sum of all numbers."""
        return sum(self.numbers)
    
    def calculate_average(self) -> float:
        """Calculate the average of all numbers."""
        if not self.numbers:
            return 0
        return self.calculate_sum() / len(self.numbers)
    
    def find_min_max(self) -> Tuple[int, int]:
        """
        Find minimum and maximum values in the list.
        
        Returns:
            Tuple of (minimum, maximum) values
        """
        if not self.numbers:
            return (0, 0)
        return (min(self.numbers), max(self.numbers))
    
    def sort_numbers(self) -> List[int]:
        """
        Sort numbers in descending order using bubble sort.
        
        Returns:
            Sorted list of numbers
        """
        numbers_copy = self.numbers.copy()
        n = len(numbers_copy)
        
        for i in range(n - 1):
            for j in range(i + 1, n):
                if numbers_copy[j] > numbers_copy[i]:
                    numbers_copy[i], numbers_copy[j] = numbers_copy[j], numbers_copy[i]
        
        return numbers_copy
    
    def calculate_median(self) -> float:
        """
        Calculate the median value of the numbers.
        
        Returns:
            Median value
        """
        if not self.numbers:
            return 0
        
        sorted_numbers = self.sort_numbers()
        n = len(sorted_numbers)
        
        if n % 2 == 0:
            # Even number of elements
            mid1 = n // 2 - 1
            mid2 = mid1 + 1
            return (sorted_numbers[mid1] + sorted_numbers[mid2]) / 2
        else:
            # Odd number of elements
            mid = n // 2
            return sorted_numbers[mid]
    
    def display_statistics(self) -> None:
        """Display all statistical information about the numbers."""
        print("=" * 50)
        print("RANDOM NUMBER STATISTICS")
        print("=" * 50)
        
        print(f"Generated numbers: {self.numbers}")
        print(f"Number of elements: {len(self.numbers)}")
        print(f"Sum: {self.calculate_sum()}")
        print(f"Average: {self.calculate_average():.2f}")
        
        min_val, max_val = self.find_min_max()
        print(f"Minimum value: {min_val}")
        print(f"Maximum value: {max_val}")
        
        sorted_numbers = self.sort_numbers()
        print(f"Sorted numbers (descending): {sorted_numbers}")
        print(f"Median: {self.calculate_median():.2f}")
        print("=" * 50)


def main():
    """Main function to demonstrate the NumberStatistics class."""
    # Create an instance of NumberStatistics
    stats = NumberStatistics(count=11, min_range=0, max_range=100)
    
    # Generate unique random numbers
    stats.generate_unique_numbers()
    
    # Display all statistics
    stats.display_statistics()


if __name__ == "__main__":
    main()
