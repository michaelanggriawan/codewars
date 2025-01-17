# Your website is divided vertically in sections, and each can be of different size (height).
# You need to establish the section index (starting at 0) you are at, given the scrollY and sizes of all sections.
# Sections start with 0, so if first section is 200 high, it takes 0-199 "pixels" and second starts at 200.

# Example:
# getSectionIdFromScroll( 300, [300,200,400,600,100] )

# will output number 1 as it's the second section.

# getSectionIdFromScroll( 1600, [300,200,400,600,100] )

# will output number -1 as it's past last section.

# Given the scrollY integer (always non-negative) and an array of non-negative integers (with at least one element), calculate the index (starting at 0) or -1 if scrollY falls beyond last section (indication of an error).

def get_section_id(scroll, sizes):
    c = 0
    for idx, s in enumerate(sizes):
        c += s
        if scroll < c: return idx
    return -1
