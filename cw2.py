header = """THE REWRITE NOVELS & CAFE
123 Paperback Lane
NY 10001
Phone: (555) 019-2834
| rewritenovels.com
Tax ID: EIN-987654321
Register: 02 | Cashier: Alex"""
book_1 = "Python Basics"
price_1 = 450
book_2 = "Data Science Intro"
price_2 = 600
line_1 = "\t{} - ₹{}".format(book_1, price_1)
line_2 = "\t{} - ₹{}".format(book_2, price_2)
total = price_1 + price_2
total_line = "\tTotal: ₹{}".format(total)
thank_you = "\nThank you for shopping with us!"
receipt = header + "\n\n" + line_1 + "\n" + line_2 + "\n" + total_line + thank_you
print(receipt.upper())


