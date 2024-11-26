def calculate_love_score(name1, name2):
    combined_name = name1 + name2
    lover_name = combined_name.lower()

    t = lover_name.count("t")
    r = lover_name.count("r")
    u = lover_name.count("u")
    e = lover_name.count("e")
    first_digit = t + r + u + e

    l = lover_name.count("l")
    o = lover_name.count("o")
    v = lover_name.count("v")
    e = lover_name.count("e")
    second_digit = l + o + v + e

    score = int(str(first_digit) + str(second_digit))
    print(score)

calculate_love_score("Kanye West","Kim Kardashian")
