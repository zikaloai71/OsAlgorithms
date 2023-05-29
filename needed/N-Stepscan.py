def NStepScan(requests, head, n):
    seek_count = 0
    direction = 1  # 1 for moving towards higher track numbers, -1 for moving towards lower track numbers
    sequence = [head]
    # Sort the requests in ascending order
    requests.sort()

    # Divide the disk into N sub-sections
    sub_section_size = len(requests) // n
    sub_sections = [requests[i:i + sub_section_size] for i in range(0, len(requests), sub_section_size)]
    print(sub_sections)
    for sub_section in sub_sections:
        # Determine the current direction based on the head position
        if direction == 1 and head >= max(sub_section):
            direction = -1
        elif direction == -1 and head <= min(sub_section):
            direction = 1

        # Scan the current sub-section in the current direction
        if direction == 1:
            for track in range(head, max(sub_section) + 1):
                if track in sub_section:
                    seek_count += abs(track - head)
                    # print(track, head)
                    head = track
                    sequence.append(head)

        else:
            for track in range(head, min(sub_section) - 1, -1):
                if track in sub_section:
                    seek_count += abs(track - head)
                    print(track, head)
                    head = track
                    sequence.append(head)

    return sequence, seek_count

# Example usage
requests = [176, 79, 34, 60, 92, 11, 41, 114]
head = 50
n = 4

sequence, seek_count = NStepScan(requests, head, n)
print("Sequenze: ", sequence)
print("Total number of seek operations =", seek_count)
