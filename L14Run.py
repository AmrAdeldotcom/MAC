parts_of_speech  = ["PLACE", "PERSON", "PLURALNOUN", "NOUN"]
test_string = """This is PLACE, no NOUN named PERSON, We have so many PLURALNOUN around here."""
def word_in_pos(word, parts_of_speech):
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None
def play_game(ml_string, parts_of_speech):
    replaced = []
    # your code here
    ml = ml_string.split()
    for w in ml:
        r = (word_in_pos(w, parts_of_speech))
        if r != None:
            #w = w.replace(r,"corgi")
            #'''
            user_input = raw_input("Type in a:"+r+" ")
            w = w.replace(r,user_input)
            #'''
            replaced.append(w)
        else:
            replaced.append(w)
    replaced = ' '.join(replaced)
    return replaced

print play_game(test_string, parts_of_speech)
