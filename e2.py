#import shutil

#we can copy file o extract file from anywhere that we want to do
#shutil.make_archive('output','zip')

import webbrowser

user_term = input('enter search term')

webbrowser.open(f'https://www.google.com/search?client=safari&rls=en&q={user_term}')

