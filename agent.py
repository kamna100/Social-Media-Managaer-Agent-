from content_generator import generate_content
from scheduler import schedule_post

print("📱 SOCIAL MEDIA MANAGER AGENT")
print("-----------------------------")

topic = input("Enter post topic: ")

caption, hashtags = generate_content(topic)

schedule_post(caption, hashtags)

print("\n✅ Post Generated Successfully!\n")
print("Caption:")
print(caption)
print("\nHashtags:")
print(hashtags)
