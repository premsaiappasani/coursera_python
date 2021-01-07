#Let's create a function that turns text into pig latin: a simple text transformation that modifies each word moving the first character to the end and appending "ay" to the end. For example, python ends up as ythonpay.


def pig_latin(text):
  say = text.split( )
  # Separate the text into words
  temp=""
  for word in say:
    temp+=fun(word)
  return temp
def fun(w):
  w=w[1:]+w[0]+"ay "
  return w
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"
