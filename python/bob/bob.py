def response(hey_bob):

    if hey_bob.isspace() or len(hey_bob) == 0:
        return "Fine. Be that way!"

    question = hey_bob.rstrip()[-1] == '?'
    yelling = hey_bob.isupper()

    if question and yelling:
        return "Calm down, I know what I'm doing!"
    elif question:
        return "Sure."
    elif yelling:
        return "Whoa, chill out!"
    else:
        return "Whatever."
