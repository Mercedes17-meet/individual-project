from database import *



outfits = [
    
{'name':'My outfit', 'description':'fresh,comfy and pretty', 'photo':'https://i5.walmartimages.com/asr/f6bbc322-83c3-49d9-a9b6-35f05aea0226_1.e37e538746a60bad395e7a0b19ab4f6c.jpeg?odnHeight=450&odnWidth=450&odnBg=FFFFFF', 'category':'summer','season': 'summer' , 'gender':'female'},
{'name':'Summer eve', 'description':'beatiful', 'photo':'https://i5.walmartimages.com/asr/859eac0f-f23f-4bf3-b190-91a97d495bbe_1.1376acaadf8d89cb4a12f42fd0318b53.jpeg?odnHeight=450&odnWidth=450&odnBg=FFFFFF', 'category':'fancy', 'season': 'summer', 'gender':'female'},
{'name':'Sparkles ', 'description':'the star of the night', 'photo':'http://cdn6.bigcommerce.com/s-vs756cw/products/1114/images/1739/Tower_Root_Beer__34890.1448901409.1280.1280.png?c=2', 'category':'party', 'season': 'summer' , 'gender':'female'},
{'name':'YOLO', 'description':'just be', 'photo':'http://texaslegacybrands.com/media/catalog/product/cache/1/image/800x/9df78eab33525d08d6e5fb8d27136e95/n/e/nesbitt-040190.jpg', 'category':'casual', 'season': 'summer', 'gender':'female'},

]

for outfit in outfits:
	newOutfit = Outfit(name=outfit['name'], photo=outfit['photo'], gender=outfit['gender'], category= outfit['category'], description= outfit['description'])
	session.add(newOutfit)
	session.commit()