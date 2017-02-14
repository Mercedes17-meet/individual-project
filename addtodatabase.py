from database import *



outfits = [
    
{'name':'My outfit', 'description':'fresh,comfy and pretty', 'photo':'https://s-media-cache-ak0.pinimg.com/736x/6a/2c/ef/6a2cef8d8a1cbbd574f3e0c4153dbae0.jpg', 'category':'summer','season': 'summer' , 'gender':'female'},
{'name':'Summer eve', 'description':'beautiful', 'photo':'https://s-media-cache-ak0.pinimg.com/736x/b8/b4/40/b8b440789b199b253e1cda60fe3fcc2a.jpg', 'category':'fancy', 'season': 'summer', 'gender':'female'},
{'name':'Sparkles ', 'description':'the star of the night', 'photo':'http://thestylespy.com/wp/wp-content/uploads/SequinDress.jpg', 'category':'party', 'season': 'summer' , 'gender':'female'},
{'name':'YOLO', 'description':'just be', 'photo':'https://s-media-cache-ak0.pinimg.com/736x/86/7d/67/867d67cd85b123a748244f660cfaf4de.jpg', 'category':'casual', 'season': 'summer', 'gender':'female'},

]

for outfit in outfits:
	newOutfit = Outfit(name=outfit['name'], photo=outfit['photo'], gender=outfit['gender'], category= outfit['category'], description= outfit['description'])
	session.add(newOutfit)
	session.commit()