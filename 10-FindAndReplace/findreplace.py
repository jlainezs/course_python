"""
Write a findAndReplace() function that has three parameters: text is the string with text to
be replaced, oldText is the text to be replaced, and newText is the replacement text. Keep in mind
that this function must be case-sensitive: if you are replacing 'dog' with 'fox', then the 'DOG' in
'MY DOG JONESY' won’t be replaced.
"""

def find_and_replace_short_version(text, old_text, new_text):
    return text.replace(old_text, new_text)

def find_and_replace(text, old_text, new_text):
    replaced = ""
    i = 0
    while i < len(text):
        if text[i:i+len(old_text)] == old_text:
            replaced += new_text
            i += len(old_text)
        else:
            replaced += text[i]
            i += 1
    return replaced

assert find_and_replace('The fox', 'fox', 'dog') == 'The dog'
assert find_and_replace('fox', 'fox', 'dog') == 'dog'
assert find_and_replace('Firefox', 'fox', 'dog') == 'Firedog'
assert find_and_replace('foxfox', 'fox', 'dog') == 'dogdog'
assert find_and_replace('The Fox and fox.', 'fox', 'dog') == 'The Fox and dog.'
