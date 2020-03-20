import re
import numpy as np
from collections import Counter

def GetReplaceDict(data):
    bib = bib2dict(data)
    urlbib = GetUrls(bib)
    unique_urls = set([urlbib[key][0] for key in urlbib.keys() if urlbib[key] != []])
    duplicates = {}
    for url in unique_urls:
        duplicates[url] = []
        for key in urlbib.keys():
            try:
                if urlbib[key][0] == url:
                    duplicates[url].append(key)
            except:
                None

    keys = list(duplicates.keys())
    keys.sort()
    for key in keys:
        if len(duplicates[key])==1:
            duplicates.pop(key,None)
    replace_dict = {}
    for key in duplicates.keys():
        value = duplicates[key]
        replace_dict[value[0]] = value[1:]
        for item in value[1:]:
            bib.pop(item, None)
    
    return replace_dict


def bib2dict(data):
    keys    = re.findall(r"@.+?\{(.+?)," , data, flags=re.DOTALL)
    entries = re.findall(r"(@.+?)(?=@|$)", data, flags=re.DOTALL)
    
    bib = {}
    for key, entry in zip(keys, entries):
        bib[key] = entry
    return bib


def GetUrls(bib):
    urlbib = {}
    for key in bib.keys():
        urlbib[key] = re.findall("[Uu]rl[ =\{]+(.+?)[\},]", bib[key], flags=re.DOTALL)
    return urlbib


def GetDOIs(bib):
    urlbib = {}
    for key in bib.keys():
        urlbib[key] = re.findall("[Uu]rl[ =\{]+(.+?)[\},]", bib[key], flags=re.DOTALL)
    return urlbib


def RemoveDuplicatesInBibfile(bibin, bibout=None):
    if bibout == None:
        bibout = bibin
    counter = 0
    with open(bibin, 'r') as file:
        data = file.read()
    replace_dict = GetReplaceDict(data)
    entries = re.findall(r"(@.+?)(?=@|$)", data, flags=re.DOTALL)
    keys    = re.findall(r"@.+?\{(.+?)," , data, flags=re.DOTALL)
    frequency = Counter(keys)

    print("Removing items with the same key...")
    for i in range(len(entries) - 1, -1, -1):
        element = entries[i]
        match = re.findall(r"@.+?\{(.+?)," , element, flags=re.DOTALL)[0]

        if frequency[match] > 1:
            del entries[i]
            frequency[match] = frequency[match] - 1
            print("Removed one duplicate entry: {key}".format(key=match))
            counter = counter + 1
    
    print("Removing items with same url-tag...")
    for key in replace_dict.keys():
        for replacekey in replace_dict[key]:
            for i in range(len(entries) - 1, -1, -1):
                element = entries[i]
                match = re.findall(r"(@.+?{{{key},)".format(key=replacekey), element, flags=re.DOTALL)

                if match != []:
                    del entries[i]
                    print("Removed the following item: {key} (duplicate of {key2})".format(
                        key=replacekey, key2=key))
                    counter = counter + 1
                    break
    keys    = re.findall(r"@.+?\{(.+?)," , data, flags=re.DOTALL)

                
    with open(bibout, 'w') as file:
        file.write(''.join(entries))
    print("Removed a total of {counter} items from the bibfile.\n".format(counter=counter))
    

def ReplaceCiteKeys(bib, filein, fileout=None):
    if fileout == None:
        fileout = filein
    counter = 0
    with open(bib, 'r') as file:
        data = file.read()
    replace_dict = GetReplaceDict(data)
    
    with open(filein, 'r') as file:
        data = file.read()
    print("Updating {file}...".format(file=filein))    
    for key in replace_dict.keys():
        for replacekey in replace_dict[key]:
            pattern = r"\\cite{{(.*?)({key})([, }}])".format(key=replacekey)

            data, n = re.subn(pattern, r"\\cite{{\1{key}\3".format(key=key), data, flags=re.DOTALL)
            counter = counter + n
            if n != 0:
                print(r"""Replaced the tag "{key1}" with "{key2}" {n} times in {file}""".format(
                    key1 = replacekey, key2=key, file=fileout, n=n))
            
    with open(fileout, 'w') as file:
        file.write(data)
    print(r"Updated a total of {counter} citation keys".format(counter=counter))
    
def MakeBackUp(filename):
    with open(filename, 'r') as file:
        data = file.read()
    with open(filename+'.backup', 'w') as file:
        file.write(data)

