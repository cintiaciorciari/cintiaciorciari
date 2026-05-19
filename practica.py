
#def most_frequent(items):
    #for item in items:
     #   items.count(item)
      #  return item



def most_frequent(items):

    most = items[0]
    highest = items.count(items[0])

    for item in items:

        count = items.count(item)

        if count > highest:
            highest = count
            most = item

    return most


print(most_frequent(["apple", "banana", "apple", "cherry", "apple", "banana"]))
print(most_frequent([3, 1, 4, 1, 5, 9, 2, 6, 1]))
print(most_frequent(["Berlin", "Hamburg", "Berlin", "Munich"]))