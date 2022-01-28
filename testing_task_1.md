### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.:
Thinking that methods should be renamed or should be class level, or using string interpolation etc.

These aren't errors but rather standards that vary from developer to developer.

Only comment on errors that would stop the tests running.

```python

class CardGame:

# On line 21 In if statement instead of = sign there should a == comaparison operator.Line 23 after else ":" (colon) is missing.
  def check_for_ace(self, card):
    # if card.value = 1:
      return True
    # else
      return False

# In this code on line 27 def spell wrong.It should be def.On line 28 there is no indentation. On line 29 instesd of return crd there should be return card1.
  # dif highest_card(self, card1 card2):
  # if card1.value > card2.value:
    # return card
  else:
    return card2
  
# In this the whole function is not indented correctly. Line 35 total should be equal to zero, total = 0. On line 38 return statement string("You have a total of") cannot concatenate with integers unless integers converted into string.

# def cards_total(self, cards):
#   total
  for card in cards:
    total += card.value
    # return "You have a total of" + total

```
