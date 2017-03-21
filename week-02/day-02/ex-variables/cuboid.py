cub_height = 12
cub_length = 33
cub_width = 20

surface = ((cub_height * cub_length) + (cub_length * cub_width) + (cub_height * cub_width)) * 2
volume = cub_height * cub_length * cub_width

print("Surface area: " + str(surface))
print("volume: " + str(volume))
