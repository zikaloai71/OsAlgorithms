size = 8
disk_size = 200


def CSCAN(arr, head, direction):
    seek_count = 0
    distance = 0
    cur_track = 0
    left = []
    right = []
    seek_sequence = [head]

    # Appending end values
    # which have to be visited
    # before reversing the direction
    left.append(0)
    right.append(disk_size - 1)

    # Tracks on the left/right of the
    # head will be serviced based on the direction.
    for i in range(size):
        if arr[i] < head:
            left.append(arr[i])
        if arr[i] > head:
            right.append(arr[i])

    # Sorting left and right vectors
    left.sort()
    right.sort()

    if direction == "left":
        # First service the requests
        # on the left side of the head.
        for i in range(len(left) - 1, -1, -1):
            cur_track = left[i]
            seek_sequence.append(cur_track)
            distance = abs(cur_track - head)
            seek_count += distance
            head = cur_track

        # Once reached the left end,
        # jump to the right end.
        head = disk_size - 1
        # seek_count += disk_size - 1 #not calculated 

        # Now service the requests
        # on the right side of the head.
        for i in range(len(right) - 1, -1, -1):
            cur_track = right[i]
            seek_sequence.append(cur_track)
            distance = abs(cur_track - head)
            seek_count += distance
            head = cur_track

    elif direction == "right":
        # First service the requests
        # on the right side of the head.
        for i in range(len(right)):
            cur_track = right[i]
            seek_sequence.append(cur_track)
            distance = abs(cur_track - head)
            seek_count += distance
            head = cur_track

        # Once reached the right end,
        # jump to the left end.
        head = 0
        # seek_count += disk_size - 1  # not calculated

        # Now service the requests
        # on the left side of the head.
        for i in range(len(left)):
            cur_track = left[i]
            seek_sequence.append(cur_track)
            distance = abs(cur_track - head)
            seek_count += distance
            head = cur_track

    print("Total number of seek operations =", seek_count)
    print("Seek Sequence is")
    for i in range(len(seek_sequence)):
	    print(seek_sequence[i] , "->" , end = " ")

# Driver code

# Request array
arr = [176, 79, 34, 60, 92, 11, 41, 114]
head = 50
direction = "right"  # Specify the direction: "left" or "right"

print("Initial position of head:", head)
print("Direction:", direction)

CSCAN(arr, head, direction)
