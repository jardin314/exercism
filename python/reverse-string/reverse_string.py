def reverse(text):
    reverseText = ''
    for i in range(len(text)-1, -1, -1):
        reverseText += text[i]
    return reverseText
