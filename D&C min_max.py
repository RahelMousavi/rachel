def min_max(A, low, high, depth=0):
    indent = "  " * depth
    print(f"{indent}📌 Entering min_max(low={low}, high={high})")

    if low == high:
        print(f"{indent}✅ Base case (single element): [{A[low]}]")
        print(f"{indent}🔄 Returning: min={A[low]}, max={A[low]}")
        return (A[low], A[low])

    elif high - low == 1:
        if A[low] < A[high]:
            print(f"{indent}✅ Base case (two elements): {A[low]} < {A[high]}")
            print(f"{indent}🔄 Returning: min={A[low]}, max={A[high]}")
            return (A[low], A[high])
        else:
            print(f"{indent}✅ Base case (two elements): {A[high]} < {A[low]}")
            print(f"{indent}🔄 Returning: min={A[high]}, max={A[low]}")
            return (A[high], A[low])

    else:
        mid = (low + high) // 2
        print(f"{indent}✂️ Splitting to: [{low}-{mid}] and [{mid + 1}-{high}]")

        print(f"{indent}🔍 Processing left half [{low}-{mid}]:")
        min1, max1 = min_max(A, low, mid, depth + 1)

        print(f"{indent}🔍 Processing right half [{mid + 1}-{high}]:")
        min2, max2 = min_max(A, mid + 1, high, depth + 1)

        final_min = min(min1, min2)
        final_max = max(max1, max2)

        print(f"{indent}📊 Comparing results:")
        print(f"{indent}   Left half: min={min1}, max={max1}")
        print(f"{indent}   Right half: min={min2}, max={max2}")
        print(f"{indent}🔑 Final result: min={final_min}, max={final_max}")
        return (final_min, final_max)


# Example execution
A = [3, 1, 4, 6, 2]
print("\n🌳 Starting execution for list:", A)
min_val, max_val = min_max(A, 0, len(A) - 1)
print("\n🎉 Final result:")
print(f"Min: {min_val}, Max: {max_val}")