import sqlite3

CSV_FILE = "vocab_CSV.csv"
SQL_DB = "Medium.db"
STRUCT_FILE = "structs.csv"

def main():

    wordList = []

    with open(CSV_FILE, "r") as csv_file:
        words = csv_file.readlines()
        for word in words:
            line = word.split(",")
            wordList.append(line)
    # get data from csv file.

    connection = sqlite3.connect(SQL_DB)
    cursor = connection.cursor()
    # open connection and create cursor.

    cursor.execute("""DROP TABLE IF EXISTS vocabulary;""")
    cursor.execute("""DROP TABLE IF EXISTS sentenceStructures;""")
    # clear old tables if they exist.

    cursor.execute("""CREATE TABLE vocabulary (""" +
                   """  word TEXT NOT NULL,""" +
                   """  noun INTEGER NOT NULL,""" +
                   """  pronoun INTEGER NOT NULL,""" +
                   """  verb INTEGER NOT NULL,""" +
                   """  adjective INTEGER NOT NULL,""" +
                   """  adverb INTEGER NOT NULL,""" +
                   """  preposition INTEGER NOT NULL,""" +
                   """  conjunction INTEGER NOT NULL""" +
                   """);""")
    # create vocabulary table.

    cursor.execute("""CREATE TABLE sentenceStructures (""" +
                   """structure TEXT NOT NULL);""");
    # create sentence struct table.

    for word in wordList:
        is_noun = 0
        is_pronoun = 0
        is_verb = 0
        is_adjective = 0
        is_adverb = 0
        is_preposition = 0
        is_conjunction = 0
        # reset flags and iter over wordList.

        if word[1] == "True":
            is_noun = 1
        if word[2] == "True":
            is_pronoun = 1
        if word[3] == "True":
            is_verb = 1
        if word[4] == "True":
            is_adjective = 1
        if word[5] == "True":
            is_adverb = 1
        if word[6] == "True":
            is_preposition = 1
        if word[7] == "True":
            is_conjunction = 1
        # set flags accordingly.

        if is_noun == 0 and is_pronoun == 0 and is_verb == 0 and \
           is_adjective == 0 and is_adverb == 0 and is_preposition == 0 and \
           is_conjunction == 0:
            continue
        # skip unused words.
        
        if not str.isalpha(word[0]):
            clean_word = ""
            for character in word[0]:
                if str.isalpha(character):
                    clean_word += character
            word[0] = clean_word
        # remove invalid characters from word. 

        cursor.execute("""INSERT INTO vocabulary""" +
                       """(word, noun, pronoun, verb, adjective, adverb, preposition, conjunction)""" +
                       """VALUES""" +
                       f"""('{word[0]}',{is_noun},{is_pronoun},{is_verb},{is_adjective},{is_adverb},{is_preposition},{is_conjunction});""")
        # insert record into vocabulary table. 

    with open(STRUCT_FILE, "r") as struct_file:
        lines = struct_file.readlines()
        for line in lines:
            cursor.execute("""INSERT INTO sentenceStructures""" +
                           """(structure)""" +
                           """VALUES""" +
                          f"""('{line}');""")
    # fill with sentence structs. 

    connection.commit()
    cursor.close()
    connection.close()
    # commit changes and close connection.

main()