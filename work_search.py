import worksearch

# the substring you're looking to find in the file name:
query = ""
# the folder you're looking to search in: 
folder = "C:/Users/"
# any files or folders containing the substrings in these lists will be excluded from the search:
# it's useful to put things like sql, node_modules, etc in here
exclude_these_files_and_folders = []
# all the possible parameters you can choose from:
# worksearch.search(search_string, path, excluded_directories=[], excluded_strings=[], caps_sense=False, print_results=True, print_full=True, show_date=False
worksearch.search(query, folder, excluded_directories=exclude_these_files_and_folders)