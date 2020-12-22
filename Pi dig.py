file_loc = ''

file = open(file_loc)

file_data = file.read()
file.close()


def search_txt(txt):
    loc = file_data.find(txt)
    if loc == -1:
        print('Not Found')
    else:
        loc += 1
        if len(txt) > 1:
            loc = str(loc) + '-' + str(loc + len(txt) - 1)
        print('{} was located at the {} digit of pi (after decimal)'.format(txt, loc))


val = input('Search for: ')
while type(val) != int:
    val = input('please input integer; search for: ')
search_txt(val)
