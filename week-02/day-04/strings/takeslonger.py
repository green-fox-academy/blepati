# When saving this quote a disk error has occured. Please fix it.
# Add "always takes longer than" to the StringBuilder (quote) between the words "It" and "you"

quoteOld = "Hofstadter's Law: It you expect, even when you take into account Hofstadter's Law."

quote = quoteOld[0:20] + " always takes longer than " + quoteOld[21:]

print(quote)
