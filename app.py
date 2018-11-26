import mlab
from movie import Movie

mlab.connect()

m = Movie(title="songoku", year=1996, image="https://genknews.genkcdn.vn/2017/photo-1-1511425238742.jpg")
m.save()

print("Done")