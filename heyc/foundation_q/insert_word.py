def insert_word_middle(original, to_insert):
    original = original.split()
    insert_pos = len(original)//2
    original.insert(insert_pos,to_insert)

    print(' '.join(original))

insert_word_middle("Hello World","abc")

