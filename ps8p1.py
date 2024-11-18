def calculate_balance():
  while True:
      # Input from the user
      principal = float(input("Enter principle amount: $"))
      rate = float(input("Enter interest rate (e.g., 0.10 for 10%): "))

      total_interest = 0.0
      current_principal = principal

      # Output header
      print("\nYear\t\tBeginning Balance\tEnding Balance")

      # Loop for 5 years of calculation
      for year in range(1, 6):
          interest = current_principal * rate
          ending_balance = current_principal + interest
          total_interest += interest
          # Display year, beginning balance, and ending balance
          print(f"{year}\t\t${current_principal:,.2f}\t\t${ending_balance:,.2f}")
          # Update the principal for the next year
          current_principal = ending_balance

      # Display total interest earned
      print(f"\nTotal interest earned: ${total_interest:,.2f}")

      # Ask if the user wants to run the program again
      continue_choice = input("\nDo you want to calculate again? (yes/no): ").strip().lower()
      if continue_choice != 'yes':
          break

# Calling the function
calculate_balance()
