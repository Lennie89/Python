childstr = str('[[Text] object with text "491", [Text] object with text "10", [Text] object with text "481", [Text] object with text "10", [Text] object with text "471", [Text] object with text "10"]]')


childlist = childstr.split(",")

print(childlist)

while len(childlist) > 0:
    print(childlist)
    childlist.pop()