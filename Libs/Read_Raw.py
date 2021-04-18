import glob
def raw(url):
    return r'%s' %url
def Get_All_From_Folder(url,extension):
    Search = glob.glob(raw(url + "*" + extension))
    Files = []
    for x in Search:
        Files += [x]
    return Files