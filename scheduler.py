def schedule_post(caption, hashtags):
    with open("posts.txt", "a", encoding="utf-8") as file:
        file.write("Caption: " + caption + "\n")
        file.write("Hashtags: " + hashtags + "\n")
        file.write("=================================\n")
