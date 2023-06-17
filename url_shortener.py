import pyshorteners

a=input("Enter your URL: ")
def shorturl(a):
    s=pyshorteners.Shortener()
    print("Your shortened URL: ",s.tinyurl.short(a))

shorturl(a)

