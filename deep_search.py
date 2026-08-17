import worksearch.deepsearch as deepsearch


query = ""
folder = "C:/Users/"
# if it's not working, make sure you're searching files with the right extensions

# any files or folders containing the substrings in these lists will be excluded from the search:
# it's useful to put things like sql, node_modules, etc in here
exclude_these_files_and_folders = [] 
temp_exclusions = [] # temporary exclusions (for files you want to temporarily exclude from the search but may add back later)

search_files_with_these_extensions = ["txt", "py", "html"] # leave empty to search all file types

deepsearch.search(query, folder,
	excluded=exclude_these_files_and_folders + temp_exclusions, 
	possible_extensions=search_files_with_these_extensions,
	show_date=True)