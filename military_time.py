
def num_to_word(num):
  num_words = {
      0: "zero",
      1: "one",
      2: "two",
      3: "three",
      4: "four",
      5: "five",
      6: "six",
      7: "seven",
      8: "eight",
      9: "nine",
      10: "ten",
      11: "eleven",
      12: "twelve",
      13: "thirteen",
      14: "fourteen",
      15: "fifteen",
      16: "sixteen",
      17: "seventeen",
      18: "eighteen",
      19: "nineteen",
      20: "twenty",
      30: "thirty",
      40: "forty",
      50: "fifty",
  }

  if num in num_words:
    return "zero " + num_words[num] if num <= 9 else num_words[num]
  else:
    tens = num // 10 * 10
    ones = num % 10
    return num_words[tens] + " " + num_words[ones]

def convert(time):
  ending = time[-2:]

  colon_index = time.index(":") 
  hour = (int(time[:colon_index]) + 12) if ending == "PM" else int(time[:colon_index])
  if hour == 24:
    hour = 12
  elif hour == 12:
    hour = 0

  minutes = int(time[colon_index+1:-2])

  hour_word = num_to_word(hour)
  minute_word = "hundred hours" if minutes == 0 else num_to_word(minutes)

  military_time = hour_word + " " + minute_word

  print(military_time)
  return military_time

assert convert("4:00PM") == "sixteen hundred hours"
assert convert("11:00AM") == "eleven hundred hours"
assert convert("11:23AM") == "eleven twenty three"
assert convert("6:45PM") == "eighteen forty five"
assert convert("7:45AM") == "zero seven forty five"
assert convert("5:05PM") == "seventeen zero five"
assert convert("4:09AM") == "zero four zero nine"
