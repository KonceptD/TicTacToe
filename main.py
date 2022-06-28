import re

# Milestones
# 1. Ask for the project name and author
# 2. Ask for Project date
# 3. Develop skeleton structure
# 4. Make use of TODO list
# Finish this project
# Better to make the milestones small than too large,
# Milestones: “reduce the number of things you have to think about at any one time”.
# https://robertheaton.com/ppab7-auto-project-builder/

pattern = set(("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-"))

# TODO: Validation - tried regex, and issubset

while True:
        projectName = input("What is the title of your project? ").ljust(40)
        validation = set(projectName)
        validation.issubset(pattern)
        if validation:
            break
        else:
            print("Invalid input, please try again")
            continue




projectAuthor = input("Who is the author of this project? ").ljust(40)


print("## PROJECT DETAILS ##")
print("Project name: "+ projectName)
print("Author: "+ projectAuthor)