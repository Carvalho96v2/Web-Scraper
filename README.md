# Web-Scraper
Created this scraper to pull various images of handguns from the Internet Movie Firearms Database, to create a training dataset for a weapon detection ML algorithm.

## Workflow
* Get list of all pistol and revolver names from http://www.imfdb.org/wiki/Category:Gun
* Get list of links to all movies from http://www.imfdb.org/index.php?title=Category:Movie&pagefrom=10+Cloverfield+Lane#mw-pages
* * Be aware, this is paginated to 200 movies per page, so you need to group them and scrap accordingly
* For each link above, get all the h1 and h2 tags that are in the list of pistols, revolvers and machine pistols
* Download all the images under each tag from above into either a "pistol" folder, or "revolver" folder
