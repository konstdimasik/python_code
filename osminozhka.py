activities = {
    'sport': 4,
    'photo tech': 7,

}
print('1')
for activity, quality in activities.items():
    boxes = ''
    i = 0
    while i < 20:
        if i < quality:
            boxes += 'X'
        else:
            boxes += '_'
        i += 1
    print(f'{activity: >30}',boxes)


