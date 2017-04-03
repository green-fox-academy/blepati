class PostIt:
    bg_color = ""
    content = ""
    content_color = ""

post_it1 = PostIt
post_it1.bg_color = "green"
post_it1.content = "nyuszi"
post_it1.color = "white"

print("background: " + post_it1.bg_color, "content: " + post_it1.content, "font-color: " + post_it1.color)

post_it2 = PostIt
post_it2.bg_color = "black"
post_it2.content = "muszi"
post_it2.color = "yellow"

print("background: " + post_it2.bg_color, "content: " + post_it2.content, "font-color: " + post_it2.color)
