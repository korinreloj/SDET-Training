#create an array of 10 elements and
# remove elements from there and
# add further elements and
# print the final array using for loop

import array as arr


veggies = ['garlic','onion','cabbage','bell pepper','ginger','corn', 'carrot', 'radish','potato','squash','broccoli']
veggies.pop(1)
veggies.remove("ginger")
veggies.append("mushroom")
veggies.insert(0, "celery")
print(veggies)

#create a list of 10 elements
# and add the a new element on 4th position
# and then print the elements using range till that element.
# Also print 2 values based on index and override the last value in the list with new one
mobile = ["apple", "samsung", "huawei", "sony", "vivo", "oppo", "xiaomi", "oneplus", "lg", "google"]
mobile.insert(3, "google")
print(mobile[0:4])
print(mobile[7])
print(mobile[5])
mobile[10] = "motorola"
print(mobile)
mobile.clear()
print(mobile)