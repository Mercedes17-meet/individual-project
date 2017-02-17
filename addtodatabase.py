from database import *



outfits = [
    
{'name':'My outfit', 'description':'fresh,comfy and pretty', 'photo':'this.jpg', 'category':'summer','season': 'summer' , 'gender':'female'},
{'name':'Summer eve', 'description':'beautiful', 'photo':'this1.jpg', 'category':'fancy', 'season': 'summer', 'gender':'female'},
{'name':'Sparkles ', 'description':'the star of the night', 'photo':'this2.jpg', 'category':'party', 'season': 'summer' , 'gender':'female'},
{'name':'YOLO', 'description':'just be', 'photo':'this3.jpg', 'category':'casual', 'season': 'summer', 'gender':'female'},

]

for outfit in outfits:
	newOutfit = Outfit(name=outfit['name'], photo=outfit['photo'], gender=outfit['gender'], category= outfit['category'], description= outfit['description'])
	session.add(newOutfit)
	session.commit()
