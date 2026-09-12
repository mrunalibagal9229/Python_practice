def closest_to_zero(numbers):
    closest_pair = None
    closest_sum = float('inf')

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            current_sum = numbers[i] + numbers[j]

            if abs(current_sum) < abs(closest_sum):
                closest_sum = current_sum
                closest_pair = (numbers[i], numbers[j])

    return closest_pair


numbers = [10, -3, 5, -8, 2, 7]

result = closest_to_zero(numbers)

print("Two numbers:", result)
print("Their sum:", sum(result))
