#SKYLINE HEIGHTS
## Lovely Burbank has a breathtaking view of the Los Angeles skyline. Let’s say you are
# given an array with heights of consecutive buildings, starting closest to you and extending
# away. Array [-1,7,3] would represent three buildings: first is actually out of view below
# street level, behind it is second at 7 stories high, third is 3 stories high (hidden behind
# the 7-story). You are situated at street level. Return array containing heights of buildings
# you can see, in order. Given [-1,1,1,7,3] return [1,7]. Given [0,4] return [4]. As always
# with challenges, do not use built-in array functions such as unshift().


def visible_buildings(buildings):
    visible = []
    max_height = 0
    for height in buildings:
        if height > max_height:
            visible.append(height)
            max_height = height
    return visible

buildings1 = [-1, 1, 1, 7, 3]
print(visible_buildings(buildings1))

buildings2 = [0, 4]
print(visible_buildings(buildings2))