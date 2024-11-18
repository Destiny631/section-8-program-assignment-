def fibonacci_sequence():
  # Initialize the first two Fibonacci numbers
  a, b = 1, 1

  # Print the first two numbers directly
  print(a, end=" ")
  print(b, end=" ")

  # Use a for loop to compute the next 18 Fibonacci numbers
  for _ in range(18):
      # Compute the next Fibonacci number
      a, b = b, a + b
      print(b, end=" ")

  # Print a newline at the end for formatting
  print()

# Call the function to display the Fibonacci sequence
fibonacci_sequence()
