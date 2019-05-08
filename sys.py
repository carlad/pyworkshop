import sys

arguements = sys.argv
print(f"We received the following arguements:")

for arg in arguements:
    print(f" - {arg}")

print(f"we are running on a {sys.platform} machine.")