import sys
import os
import shutil

#get extensions
def clear_dir(dir):
    base = dir
    files = []
    for fname in os.listdir(base):
        path = os.path.join(base, fname)
        if os.path.isdir(path):
            # skip directories
            continue
        else:
            files.append(fname)
    print(type(files))
    file_types = []
    for f in files:
        extension = f.split(".")[-1]
        if extension not in file_types:
            file_types.append(extension)
    print("{}".format(file_types))
    #creat folde structure for each found ext
    for i in file_types:
        fExt = "." + i
        # fExt = "'{}'".format(fExt)
        # print(fExt)
        try:
            folders = extension_dict[fExt]
            folders = base + "\\" + folders
            print(folders)
            if not os.path.exists(folders):
                os.makedirs(folders)
            for fname in os.listdir(base):
                path = os.path.join(base, fname)
                if os.path.isdir(path):
                # skip directories
                    continue
                else:
                    if fname.endswith(fExt):
                        print(fname)
                        print(folders + "\\" + fname)
                        shutil.move(base + "\\" + fname, folders + "\\" + fname)
        except:
            pass

#Dic of extensions
extension_dict = {
        # No name
        'noname':  'other\\uncategorized',
        # audio
        '.aif':    'media\\audio',
        '.cda':    'media\\audio',
        '.mid':    'media\\audio',
        '.midi':   'media\\audio',
        '.mp3':    'media\\audio',
        '.mpa':    'media\\audio',
        '.ogg':    'media\\audio',
        '.wav':    'media\\audio',
        '.wma':    'media\\audio',
        '.wpl':    'media\\audio',
        '.m3u':    'media\\audio',
        # text
        '.txt':    'text\\text_files',
        '.doc':    'text\\microsoft\\word',
        '.docx':   'text\\microsoft\\word',
        '.odt ':   'text\\text_files',
        '.pdf':    'text\\pdf',
        '.rtf':    'text\\text_files',
        '.tex':    'text\\text_files',
        '.wks ':   'text\\text_files',
        '.wps':    'text\\text_files',
        '.wpd':    'text\\text_files',
        # video
        '.3g2':    'media\\video',
        '.3gp':    'media\\video',
        '.avi':    'media\\video',
        '.flv':    'media\\video',
        '.h264':   'media\\video',
        '.m4v':    'media\\video',
        '.mkv':    'media\\video',
        '.mov':    'media\\video',
        '.mp4':    'media\\video',
        '.mpg':    'media\\video',
        '.mpeg':   'media\\video',
        '.rm':     'media\\video',
        '.swf':    'media\\video',
        '.vob':    'media\\video',
        '.wmv':    'media\\video',
        # images
        '.ai':     'media\\images',
        '.bmp':    'media\\images',
        '.gif':    'media\\images',
        '.jpg':    'media\\images',
        '.jpeg':   'media\\images',
        '.png':    'media\\images',
        '.ps':     'media\\images',
        '.psd':    'media\\images',
        '.svg':    'media\\images',
        '.tif':    'media\\images',
        '.tiff':   'media\\images',
        '.cr2':    'media\\images',
        # internet
        '.asp':    'other\\internet',
        '.aspx':   'other\\internet',
        '.cer':    'other\\internet',
        '.cfm':    'other\\internet',
        '.cgi':    'other\\internet',
        '.pl':     'other\\internet',
        '.css':    'other\\internet',
        '.htm':    'other\\internet',
        '.js':     'other\\internet',
        '.jsp':    'other\\internet',
        '.part':   'other\\internet',
        '.php':    'other\\internet',
        '.rss':    'other\\internet',
        '.xhtml':  'other\\internet',
        '.html':   'other\\internet',
        # compressed
        '.7z':     'other\\compressed',
        '.arj':    'other\\compressed',
        '.deb':    'other\\compressed',
        '.pkg':    'other\\compressed',
        '.rar':    'other\\compressed',
        '.rpm':    'other\\compressed',
        '.tar.gz': 'other\\compressed',
        '.z':      'other\\compressed',
        '.zip':    'other\\compressed',
        # disc
        '.bin':    'other\\disc',
        '.dmg':    'other\\disc',
        '.iso':    'other\\disc',
        '.toast':  'other\\disc',
        '.vcd':    'other\\disc',
        # data
        '.csv':    'programming\\database',
        '.dat':    'programming\\database',
        '.db':     'programming\\database',
        '.dbf':    'programming\\database',
        '.log':    'programming\\database',
        '.mdb':    'programming\\database',
        '.sav':    'programming\\database',
        '.sql':    'programming\\database',
        '.tar':    'programming\\database',
        '.xml':    'programming\\database',
        '.json':   'programming\\database',
        # executables
        '.apk':    'other\\executables',
        '.bat':    'other\\executables',
        '.com':    'other\\executables',
        '.exe':    'other\\executables',
        '.gadget': 'other\\executables',
        '.jar':    'other\\executables',
        '.wsf':    'other\\executables',
        # fonts
        '.fnt':    'other\\fonts',
        '.fon':    'other\\fonts',
        '.otf':    'other\\fonts',
        '.ttf':    'other\\fonts',
        # presentations
        '.key':    'text\\presentations',
        '.odp':    'text\\presentations',
        '.pps':    'text\\presentations',
        '.ppt':    'text\\presentations',
        '.pptx':   'text\\presentations',
        # programming
        '.c':      'programming\\c&c++',
        '.class':  'programming\\java',
        '.java':   'programming\\java',
        '.py':     'programming\\python',
        '.sh':     'programming\\shell',
        '.h':      'programming\\c&c++',
		'.ipynb':  'programming\\python',
        # spreadsheets
        '.ods':    'text\\microsoft\\excel',
        '.xlr':    'text\\microsoft\\excel',
        '.xls':    'text\\microsoft\\excel',
        '.xlsx':   'text\\microsoft\\excel',


        }

