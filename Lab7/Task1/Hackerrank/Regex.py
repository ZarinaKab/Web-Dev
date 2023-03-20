regex_integer_in_range = r"_________"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"_________"	# Do not delete 'r'.

import re

regex_integer_in_range = r"^[1-9][0-9]{5}$"
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"

postal_code = input()

print(bool(re.match(regex_integer_in_range, postal_code))
      and len(re.findall(regex_alternating_repetitive_digit_pair, postal_code)) < 2)

