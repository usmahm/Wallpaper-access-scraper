### **WallpaperAccess walpaper scrapper**

This is a practice **python** project for scrapping walpapers from [wallpaperaccess.com](https://wallpaperaccess.com/ "wallpaperaccess.com"). This is simply for learning purpose.

Steps to get the script running on your computer:
1. Install the required libraries by running:
	`pip install cloudscraper bs4 lxml tqdm`

1. Replace 
	`walpaperaccess_link = 'https://wallpaperaccess.com/4k-art'`
	and
	`base_folder = os.getcwd()`
	with walpaperaccess group link(note the format '...wallpaperaccess.com/{group}')
	and path to desired download destination respectively

1. Run the scrapper.py file
	`python scrapper.py`
	
This may not run due to the website protection by Cloudfare, check that you have the latest version of `cloudscraper` installed and try again
