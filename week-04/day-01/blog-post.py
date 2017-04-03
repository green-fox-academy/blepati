class BlogPost:
    authorName = ""
    title = ""
    text = ""
    publicationDate = ""

blog_post1 = BlogPost
blog_post1.authorName = "John Doe"
blog_post1.title = "Lorem Ipsum"
blog_post1.text = "Lorem bacon ipsum chili pulled pork"
blog_post1.publicationDate = "2010. 06. 28"

print(blog_post1.title + " written by " + blog_post1.authorName + " posted at "+ blog_post1.publicationDate)
print(blog_post1.text)

blog_post2 = BlogPost
blog_post2.authorName = "Jane Moe"
blog_post2.title = "Habanero Mipsum"
blog_post2.text = "Lorem bacon ipsum chili pulled pork, steak and fries dolor"
blog_post2.publicationDate = "2015. 04. 26"

print(blog_post2.title + " written by " + blog_post2.authorName + " posted at "+ blog_post2.publicationDate)
print(blog_post2.text)
