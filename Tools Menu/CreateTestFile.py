# coding: utf-8


# *** DISCLAIMER PLEASE READ ***
# please understand, i am a newbie. being a newbie,
# my code may be crap or worse buggy
# i still like to share. it could be useful code.
# or parts of could be useful
# but i like the feedback

# gist = https://gist.github.com/89535a038f5d954d5c6a
# repo = https://github.com/Phuket2/Pythonista

'''
    NOTES:
    meant to be run from the tools menu....
    the idea is to create a .py file
    fast in a known location.

    You can use **my_std_script** var to write some code to the
    file if you like.
    LOL , it would be so nice if markdown worked
    inside python comments :)

    REASON:
    So often i want to test something in a new .py,
    i often create a new file in the project dir i am
    wirking on, called crap.py or test.py or something.
    Pollutes my project directory.

    This is only for those .py files you want to create,
    use and forget.

    Some point you should go back into the target directory all delete
    its contents. the temp file created will not be automactially
    deleted!

'''

import os, sys, tempfile
import editor, console

# assumes this directory will reside in
# the site_packages directory.
_temp_dir_name = 'TestFiles'

# the base dir where the temp_dir_name is
# created if it does exist...
# you will be prompted, before a dir is created
_base_dir = os.path.expanduser('~/Documents/site-packages')

# my_std_script, is written to the new file
# can also set my_std_script = '', nothing will be
# written to the file

my_std_script ='''
# coding: utf-8

import sys, ui


class MyClass(object):
    def __init__(self):
        pass

def main(args):
    print 'in main...'
    # MyClass()
    return 0

if __name__ == '__main__':
    return_code = main(sys.argv[1:])
        if return_code oo c exit(main(sys.argv))
'''

# uncomment the line below, if you want nothing written
# to the temp file...
my_std_script = ''

_target_dir = '{}/{}/'.format(_base_dir, _temp_dir_name)


# make sure the target dir exists
if not os.path.isdir(_target_dir):
    result = console.alert(title = 'Directory Does Not Exist',
                message = 'the target_dir, does not exist!',
                button1 = 'Make Dir')

    # Cancel button exits, so no check required.
    try:
        os.mkdir(_target_dir)
    except OSError as err:
        raise err


try:
    with tempfile.NamedTemporaryFile(mode = 'w',
                                dir = _target_dir,
                                suffix = '.py',
                                delete = False) as f:
        f.write(my_std_script)
        name = f.name

except Exception as err:
    raise Exception(err.message, err.args)


# open in a new tab...
editor.open_file(name, True, False)
