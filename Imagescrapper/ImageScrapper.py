from bs4 import BeautifulSoup as bs
import os

class ImageScrapper:
    def delete_existing_image(self,list_of_images):
        for self.image in list_of_images:
            try:
                os.remove('./static/'+self.image)
            except Exception as e:
                print('error in deleting ' , e)
            return 0