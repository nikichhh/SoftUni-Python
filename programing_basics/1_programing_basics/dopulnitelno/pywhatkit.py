import pywhatkit

text = 'Python is an easy to learn, powerful programming language. It has efficient high-level data '\
 'structures and a simple but effective approach to object-oriented programming.'

pywhatkit.text_to_handwriting(text, rgb=(255, 0, 0))