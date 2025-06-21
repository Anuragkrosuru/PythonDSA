# stacks and queues

# def is_valid_post_format(posts):
#     stack  = []
#     if not posts:
#         return False
#     if posts[0] == ')' or posts[0] == '}' or posts[0] == ']':
#         return False
#     for i in posts:
#         if i == '(' or i == '[' or i == '{': 
#             stack.append(i)
#         elif i == ')':
#             if stack:
#                 if stack[-1]== '(':
#                     stack.pop()
#             else:
#                 return False
#         elif i == ']':
#             if stack:
#                 if stack[-1] == '[':
#                     stack.pop()
#             else:
#                 return False
#         elif i == '}':
#             if stack:
#                 if stack[-1] == '{':
#                     stack.pop()
#             else:
#                 return False
#         else:
#             return False
#     if len(stack) == 0:
#         return True
#     return False
        
# print(is_valid_post_format(""))
# print(is_valid_post_format("())"))
# print(is_valid_post_format(")"))
# print(is_valid_post_format("()"))
# print(is_valid_post_format("()[]{}")) 
# print(is_valid_post_format("(]"))




















def is_valid_post_format(posts):
    stack = []

    set = {'(', "[", "{"}

    for i in posts:
        if i in set:
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == "(":
                stack.pop()
        elif i == ']':
            if stack and stack[-1] == "[":
                stack.pop()
        elif i == '}':
            if stack and stack[-1] == "{":
                stack.pop()
        else:
            return False
        
    return len(stack) == 0


print(is_valid_post_format("()"))
print(is_valid_post_format("()[]{}")) 
print(is_valid_post_format("(]"))


def reverse_comments_queue(comments):
    stack = []
    reverse = []

    for comment in comments:
        stack.append(comment)

    while stack:
        reverse.append(stack.pop()) 

    return reverse 
print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))

print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))


def is_symmetrical_title(title):
    title = title.lower()
    left = 0
    right = len(title) - 1

    while left <= right:
        if title[left] == " ":
            left += 1
        if title[right] == " ":
            right -= 1
        if title[left] == title[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

print(is_symmetrical_title("A Santa at NASA"))
print(is_symmetrical_title("Social Media")) 


def engagement_boost(engagements):
    squared_engagements = []
    
    # squaring numbers and appending to lsit
    for i in range(len(engagements)):
        squared_engagement = engagements[i] * engagements[i]
        squared_engagements.append((squared_engagement, i))
    
    # sorting by reversing
    squared_engagements.sort(reverse=True)
    
    # resizing
    result = [0] * len(engagements)
    position = len(engagements) - 1
    

    for square, original_index in squared_engagements:
        result[position] = square
        position -= 1
    
    return result

def engagement_boost2(engagements):
    left =0
    right = len(engagements) - 1

    for i in range(len(engagements)):
        engagements[i] = engagements[i] * engagements[i]

    while left < right:
        #print(engagements)
        if engagements[left] >= engagements[right]:
            engagements[left], engagements[right] = engagements[right], engagements[left]
        right -= 1
    return engagements

# print(engagement_boost([-4, -1, 0, 3, 10]))
# print(engagement_boost([-7, -3, 2, 3, 11]))


# -10, 4, 3, 8, 9
# 100, 9, 16, 9, 64,81
# 100 >= 81
# 81, 16, 9, 64,100
# 81 >= 64
# 64, 16, 81, 100

print(engagement_boost2([-4, -1, 0, 3, 10]))
print(engagement_boost2([-7, -3, 2, 3, 11]))
print(engagement_boost2([0, 2, 3, 11]))


def clean_post(post):
    stack = []

    for c in post:
        if c == c.lower():
            stack.append(c)
        else:
            if c == c.upper():
                if stack:
                    if stack[-1] == c.lower():
                        stack.pop()
    return stack

print(clean_post("poOost")) 
print(clean_post("abBAcC")) 
print(clean_post("s")) 

# abBAcC
# a
# ab
# a
# 
# c
# 


def post_compare(draft1, draft2):
    stack = []
    stack2 = []

    for c in draft1:
        if c != "#":
            stack.append(c)
        else:
            stack.pop()
    for c in draft2:
        if c != "#":
            stack2.append(c)
        else:
            stack2.pop()
    return stack == stack2

print(post_compare("ab#c", "ad#c"))
print(post_compare("ab##", "c#d#")) 
print(post_compare("a#c", "b")) 


def edit_post(post):
    stack = []

    reverse = ""
    for c in post:
        if c != " ":
            stack.append(c)
        else:
            while stack:
                reverse += stack.pop()
            reverse += " "
    return reverse

print(edit_post("Boost your engagement with these tips")) 
print(edit_post("Check out my latest vlog")) 