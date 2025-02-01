# Assignment-5
**Running the Code**
Clone or download the repository.
Open a terminal and navigate to the project directory.
Run the script using the following command:
python QuicksortAnalysisandrandomized.py
The script will generate execution times for different input sizes and distributions, displaying the results in the terminal.

**Summary of Findings**
Deterministic Quicksort: Uses the middle element as the pivot. Performs well on average but can degrade to O(n²) in the worst case.
Randomized Quicksort: Selects a random pivot, reducing the likelihood of worst-case performance and improving consistency.
Performance Comparison: The randomized version consistently outperforms the deterministic version on sorted and reverse-sorted inputs.

**Time Complexity:**
Best/Average Case: O(n log n)
Worst Case: O(n²) (deterministic version on sorted/reverse-sorted inputs)
Space Complexity: O(log n) due to recursive stack calls.
