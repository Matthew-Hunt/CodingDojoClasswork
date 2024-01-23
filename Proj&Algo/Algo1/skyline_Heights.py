def get_visible_buildings(buildings):
    visible_buildings = []
    max_height = 0

    for height in buildings:
        if height > max_height:
            visible_buildings.append(height)
            max_height = height

    return visible_buildings

buildings1 = [-1, 1, 1, 7, 3]
print(get_visible_buildings(buildings1))

buildings2 = [0, 4]
print(get_visible_buildings(buildings2))
