# picdownloader
Part of a tumblr -> jekyll conversion process. Downloads the tumblr images to a local copy.

I used the instructions (https://import.jekyllrb.com/docs/tumblr/) to import my tumblr-based blog into jekyll. It worked great, except that it did not download the images as well.

This script takes assumes there is a directory called "pages" filled with the HTML files of your blog.  It also assumes there is a "images" directory to place all of the downloaded images.

For each file the script:
1. Identifies the images links
2. Downloads the files
3. Renames the files "[name_of_blog_post} + incrementing number + [.jpg/.png]"
4. Saves the renamed files in the /images directory
5. Updates the file links so that they now point to the image in /images instead of the tumblr image.  

This should work for images hosted anywhere that you want to save locally.
