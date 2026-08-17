import os, time
from datime import xth_of_month_year

def match_check(search_string, name, excluded_strings=[], caps_sense=False):
    if any(ex_string in name for ex_string in excluded_strings):
        return 0
    match_count = 0
    for word in search_string.split(" "):
        if caps_sense:
            if word in name:
                match_count += 1
        else:
            if word.lower() in name.lower():
                match_count += 1
    return match_count

def sort_and_print(matches, print_full, show_date):
    print(f"{len(matches)} results")
    sort_func1 = lambda ls: ls[1]
    sort_func2 = lambda ls: ls[2]
    if matches:
        if show_date:
            matches = [(match[0], match[1], os.path.getmtime(match[0])) for match in matches]
            matches.sort(key=sort_func2)
        else:
            matches.sort(key=sort_func1)
        curr_match_num = 0
        for match in matches:
            #print(match)
            if match[1] != curr_match_num:
                curr_match_num = match[1]
                print(f"results with {curr_match_num} match:")
            if print_full:
                if show_date:
                    print(f"\n{xth_of_month_year(match[2])}:")
                print("    " + match[0].replace("\\", "/"))
            else:
                print_text = match[0].split("/")[-1]
                print(f"    {print_text}")
    else: 
        print("no matches")

def walk_search(search_string, path, excluded_directories=[], excluded_strings=[], caps_sense=False): # a reimplementation of os.walk, of sorts
    scan = os.scandir(path)
    with scan:
        while True:
            try:
                item = next(scan)
            except StopIteration:
                break
            name = item.name
            _path = item.path.replace("\\", "/")
            try:
                if item.is_dir():
                    #
                    if any(exclude_dir in _path for exclude_dir in excluded_directories):
                    # if an excluded directory is found, find it, remove it from future checks, then skip traversing it
                        excluded_directories.remove([exclude_dir for exclude_dir in excluded_directories if exclude_dir in _path][0])
                        continue
                    else:
                        # recursively yield each unexcluded directory 
                        yield from walk_search(search_string, _path, excluded_directories=excluded_directories, excluded_strings=excluded_strings, caps_sense=caps_sense)
            except Exception as e:
                pass #rint(e)
            num_matches = match_check(search_string, name, caps_sense=caps_sense, excluded_strings=excluded_strings)
            if num_matches: #
                yield _path, num_matches
        

def exclude_search(search_string, path, excluded_directories=[], excluded_strings=[], caps_sense=False):
    matches = []
    jmatches = []
    walk = walk_search(search_string, path, excluded_directories=excluded_directories, excluded_strings=excluded_strings, caps_sense=caps_sense)
    for path_, num_matches in walk:
        matches.append((path_, num_matches))
        jmatches.append(path_)
    return matches, jmatches


def search(search_string, path, excluded_directories=[], excluded_strings=[], caps_sense=False, print_results=True, print_full=True, show_date=False):
    excluded_directories += [
    "C:/Users/Kees/Work/Projects/pokemod/",
    "C:/My Files/Applications/thonny-py38-4.0.2-windows-portable",
    "C:/My Files/Work/Projects/Britain/lava", 
    "C:/My Files/Work/Projects/machine learning/GumPTion-3/openai-quickstart-python/venv", 
    "C:/My Files/Work/Projects/voice control", 
    "C:/My Files/Work/Projects/automaton/micropython/esp32/micropython", 
    "C:/My Files/Work/Projects/automaton/esp/esp8266/deprecated", 
    "C:/My Files/Work/Projects/ebay/upselling/code/TitleUnrequired", 
    "C:/My Files/Studies/Year 3/Android/FirstProject", 
    "C:/My Files/Studies/Year 2/Computer Science/gp16", 
    "C:/My Files/Entertainment/Games/Minecraft/profiles", 
    "C:/My Files/Entertainment/Games/DS/TWiLightMenu", 
    "C:/My Files/Entertainment/Games/DS/Homebrew/Nintendo 3DS", 
    "C:/My Files/Entertainment/Games/DS/backups", 
    "C:/My Files/Archive/Work Archive", 
    "C:/My Files/Archive/Technical/Virtual Envs/Ebay Check/3ds_xl", 
    "C:/My Files/Archive/Technical/Rails", 
    "C:/My Files/Archive/Technical/MinecraftWorkspace", 
    "C:/My Files/Archive/Technical/Android Root", 
    "C:/My Files/Archive/MinecraftWorkspace", 
    "C:/My Files/Archive/brave/brave-core-master",
    "C:/My Files/Applications/thonny-py38-4.0.2-windows-portable",
    "C:/My Files/Applications/stable-diffusion-ui",
    "C:/My Files/Entertainment/Games/DS/_nds/TWiLightMenu", 
    "C:/My Files/Archive/Technical/Websites/ShopSite/virt/Lib",
    "C:/My Files/Archive/Technical/Python/ProjectTest/venv", 
    "C:/My Files/Archive/Technical/django/blogapp/virt", 
    "C:/My Files/Archive/Electrum-4.3.4",
    "C:/My Files/Applications/1. installers"
    ]
    matches, jmatches = exclude_search(search_string, path, excluded_directories=excluded_directories, excluded_strings=excluded_strings, caps_sense=caps_sense)
    if print_results:
        sort_and_print(matches, print_full, show_date)
    return jmatches