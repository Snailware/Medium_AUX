
CSV_FILE = "vocab_CSV.csv"
SQL_FILE = "medium_script.sql"

def main():

    wordList = []

    with open(CSV_FILE, "r") as csv_file:
        words = csv_file.readlines()
        for word in words:
            line = word.split(",")
            wordList.append(line)

    with open(SQL_FILE, "w") as sql_file:

        records_written = 0

        sql_file.write("INSERT INTO vocabulary\n" +
                       "(word, noun, pronoun, verb, adjective, adverb, preposition, conjunction)\n" +
                       "VALUES\n")

        for word in wordList:
            is_noun = 0
            is_pronoun = 0
            is_verb = 0
            is_adjective = 0
            is_adverb = 0
            is_preposition = 0
            is_conjunction = 0

            if records_written >= 999:
                sql_file.write("\nINSERT INTO vocabulary\n" +
                               "(word, noun, pronoun, verb, adjective, adverb, preposition, conjunction)\n" +
                               "VALUES\n")
                records_written = 0

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

            if is_noun == 0 and is_pronoun == 0 and is_verb == 0 and \
               is_adjective == 0 and is_adverb == 0 and is_preposition == 0 and \
               is_conjunction == 0:
                continue
            
            if not str.isalpha(word[0]):
                clean_word = ""
                for character in word[0]:
                    if str.isalpha(character):
                        clean_word += character
                word[0] = clean_word

            sql_file.write(f"""('{word[0]}',{is_noun},{is_pronoun},{is_verb},{is_adjective},{is_adverb},{is_preposition},{is_conjunction}),\n""")
            records_written += 1

main()