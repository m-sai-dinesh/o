import random

# Step 1: Input number of disk locations
n = int(input("Enter number of locations: "))

# Step 2: Create disk (all blocks initially free)
disk = []
for i in range(n):
    disk.append(False)

# Step 3: Randomly occupy some blocks
for i in range(n):
    if random.random() < 0.4:
        disk[i] = True

# Step 4: Print initial disk state
print("\nInitial Disk State:")
for i in range(n):
    if disk[i] == True:
        print("1", end=" ")
    else:
        print("0", end=" ")
print()

# Step 5: Choose allocation method
print("\nChoose Allocation Method:")
print("1) Sequential Allocation")
print("2) Linked Allocation")
print("3) Indexed Allocation")

choice = int(input("Enter your choice: "))
num_files = int(input("Enter number of files: "))

# Step 6: Allocate files
for f in range(1, num_files + 1):

    print("\n--- Allocating File", f, "---")

    size = random.randint(1, 5)
    print("File size:", size)

    # ==========================
    # 1. Sequential Allocation
    # ==========================
    if choice == 1:

        allocated = False

        for i in range(n - size + 1):

            free = True

            for j in range(i, i + size):
                if disk[j] == True:
                    free = False
                    break

            if free == True:
                for j in range(i, i + size):
                    disk[j] = True

                print("Allocated from block", i, "to", i + size - 1)

                allocated = True
                break

        if allocated == False:
            print("Allocation failed (no contiguous space)")

    # ==========================
    # 2. Linked Allocation
    # ==========================
    elif choice == 2:

        free_blocks = []

        for i in range(n):
            if disk[i] == False:
                free_blocks.append(i)

        if len(free_blocks) < size:
            print("Allocation failed (not enough space)")
        else:
            blocks = random.sample(free_blocks, size)

            for b in blocks:
                disk[b] = True

            print("Allocated blocks (Linked List):")
            for b in blocks:
                print(b, end=" -> ")
            print("NULL")

    # ==========================
    # 3. Indexed Allocation
    # ==========================
    elif choice == 3:

        free_blocks = []

        for i in range(n):
            if disk[i] == False:
                free_blocks.append(i)

        if len(free_blocks) < size + 1:
            print("Allocation failed (need index + data blocks)")
        else:
            index_block = free_blocks[0]

            remaining = []
            for i in range(1, len(free_blocks)):
                remaining.append(free_blocks[i])

            data_blocks = random.sample(remaining, size)

            disk[index_block] = True

            for b in data_blocks:
                disk[b] = True

            print("Index Block:", index_block)
            print("Data Blocks:", data_blocks)
            print(index_block, "->", data_blocks)

    else:
        print("Invalid choice")

    # Step 7: Print updated disk state
    print("Disk State:")
    for i in range(n):
        if disk[i] == True:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()
