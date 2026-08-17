import os
import pprint
from datime import xth_of_month_year

def search_bytes(file, search):
    text = open(file, "rb").read()
    return text.count(bytes(search, "UTF-8"))

def search_plain(file, search):
    text = open(file, "r").read().lower()
    return text.count(search.lower())

default_exclusions = ["C:/My Files/Work/Writings/programs/words_by_freq.txt", "C:/My Files/Work/Projects/Britain/lava", "C:/My Files/Work/Projects/machine learning/GumPTion-3/openai-quickstart-python/venv/", "C:/My Files/Work/Projects/brave/brave-core-master", "C:/My Files/Work/Projects/voice control", "C:/My Files/Work/Tools/deep_search.py", "C:/My Files/Archive/Technical/Penetration Testing/wordlist-master/", "C:/My Files/Archive/Python Bkup/Programs/Mine/Syllable Genius/words.txt", "C:/My Files/Archive/Python Bkup/","C:/My Files/Studies/Year 2/Computer Science/Java/The Bank of Question/10-million-password-list-top-100000.txt"]

def search(search_text, path, print_results=True, show_date=False, excluded=[], possible_extensions=[]):
    excluded += default_exclusions
    show_root = 1
    # recursively gets every file in the path
    file_gen = os.walk(path)
    successes = []
    for root, d_names, f_names in file_gen:
        for f_file in f_names:
            #input((root, d_names, f_file))
            fi = os.path.join(root, f_file)
            if any(exclude_dir in fi.replace("\\", "/") for exclude_dir in excluded):
                continue
            if (any("." + possible_ext in f_file for possible_ext in possible_extensions) or not possible_extensions) and "knowledge.txt" != f_file:
                try:
                    byt_num = search_bytes(root + "/" + f_file, search_text)
                except Exception as e:
                    byt_num = 0
                try:
                    num = search_plain(root + "/" + f_file, search_text)
                except Exception as e:
                    num = 0
                if byt_num > 0:
                    successes.append((byt_num, {True : root + "/", False : ""}[show_root] + f_file))
                elif num > 0:
                    successes.append((num, {True : root + "/", False : ""}[show_root] + f_file))
                #print(f"~~~/n{byt_num}, {num}/n~~~")

    successes.sort(key=lambda x: x[0], reverse=True)
    if print_results:
        for success in successes:
            print(f"{success[0]} occurrences in:\n" + success[1].replace("\\", "/"))
            if show_date:
                seconds_since_epoch = os.path.getmtime(success[1])
                print(xth_of_month_year(seconds_since_epoch))
            print()
    return successes

#search("ssh", "C:/My Files/Work/")