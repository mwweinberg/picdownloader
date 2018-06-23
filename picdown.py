#python3

import re
import urllib.request
import glob

#find all of the html files and put their name in  a list
page_names = glob.glob('pages/*.html')
print("Finding all of the files and putting their name in a list")


for name in page_names:
    #open the file and load the contents into the variable "target_contents"
    target = open(name, 'r')
    target_contents = target.read()
    print("openning " + name)
    target.close()


    #find the links
    #https://regexr.com/
    regex = r"src=[\"|\']([^\"|\']+)[\"|\']"

    #finds all of the image sources
    matches = re.findall(regex, target_contents)
    print("finding image sources")

    #start to rewrite the images sources
    #so that each file has a UID
    filecounter = 0

    #for each URL in the file
    for match in matches:
        print("replacing image " + str(filecounter))
        #this is where you generate the new name for the picture
        #remove the /pages/directory reference
        new_name = name.replace("pages/", "")

        #folder + name of post + number for saving
        matchmod_jpg = "images/" + new_name + str(filecounter) + ".jpg"
        matchmod_png = "images/" + new_name + str(filecounter) + ".png"

        #folder + name of post + number for linking
        #I have no idea why this one needs the /
        matchmod_jpg_link = "/images/" + new_name + str(filecounter) + ".jpg"
        matchmod_png_link = "/images/" + new_name + str(filecounter) + ".png"

        #increase the number by one
        filecounter += 1

        #if the file is a jpg
        if 'jpg' in match:
            #downloads the file and saves it at matchmod location
            urllib.request.urlretrieve(match, matchmod_jpg)
            #replace the image link with the matchmod
            newstring = target_contents.replace(match, matchmod_jpg_link)
            #update the string with the change or it won't stick
            target_contents = newstring

        #if it is a png
        if 'png' in match:
            #downloads the file and saves it at matchmod location
            urllib.request.urlretrieve(match, matchmod_png)
            #replace the image link with the matchmod
            newstring = target_contents.replace(match, matchmod_png_link)
            #update the string with the change or it won't stick
            target_contents = newstring



    #open the file and load the updated 'target contents' back in
    target = open(name, 'w')
    target.truncate()
    target.write(target_contents)
    print("rewriting " + name)
    target.close()
