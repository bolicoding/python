# sentence = 'The quick brown fox jumped over the lazy dog'
# sentence_two = sentence.upper()

# (sentence)
# print(sentence_two)

# The quick brown fox jumped
# T => 0
# h => 1
# e => 2
# ' ' => 3

# you cannot change content inside of a string

#starter_sentence = 'The quick brown fox jumped'

#new_sentence = 'Thy' + starter_sentence[3:]

#print(new_sentence)

# Heredoc

content = """
Nullam id dolor id nibh ultricies vehicula ut id elit. Nullam quis risus eget urna mollis ornare vel eu leo.

Vestibulum id ligula porta felis euismod semper. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras justo odio, dapibus ac facilisis in.

Integer posuere erat a ante venenatis dapibus posuere velit aliquet.
""".strip()

print(content)