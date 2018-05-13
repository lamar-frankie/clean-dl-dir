
import os



dry_run = False
docs = ['.ppt', '.xls', '.docx', '.txt', '.pdf', 'epub', '.mobi']
images = ['.png', '.jpeg', ]
archives = ['.zip', '.tar', '.gz', '.dmg', '.xz', 'img']
dl_path = '/Users/fl76at/Downloads'


#get list of files in the downloads directory

def get_dl_files():
    """Returns a list of files in the Downloads Directory"""
    dl_files = os.listdir(dl_path)

    print("The following files were found: \n")
    for file in dl_files:

        print(file)
    return dl_files


#if file is a document powerpoint or excel doc move to Documents directory
def move_files(file_list):
    """Moves files to folder based on filetype"""

    for file in file_list:


        #move documents
        for doc in docs:
            if doc in file:
                current_path = os.path.abspath(dl_path + '/' + file)
                new_path = '/Users/fl76at/Documents/' + file

                if not dry_run:
                    print('Moving {} to {}'.format(file, new_path))
                    os.rename(current_path, new_path)
                    break
                else:
                    print('Moving {} to {}'.format(file, new_path))

        #move images
        for img in images:
            if img in file:
                current_path = os.path.abspath(dl_path + '/' + file)
                new_path = '/Users/fl76at/Pictures/' + file

                if not dry_run:
                    print('Moving {} to {}'.format(file, new_path))
                    os.rename(current_path, new_path)
                    break
                else:
                    print('Moving {} to {}'.format(file, new_path))

        #move_archives
        for archive in archives:
            if archive in file:
                current_path = os.path.abspath(dl_path + '/' + file)
                new_path = '/Users/fl76at/.Trash/' + file

                if not dry_run:
                    print('Moving {} to {}'.format(file, new_path))
                    os.rename(current_path, new_path)
                    break
                else:
                    print('Moving {} to {}'.format(file, new_path))


#run
if __name__ == '__main__':
    move_candidates = get_dl_files()
    move_files(move_candidates)


