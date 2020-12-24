def partition(elements,start,end):
    pivot_index = end
    while start <= pivot_index:
        while elements[start] <= elements[pivot_index] and start < len(elements):
            start +=1
        i = start +1
        while i<len(elements) and elements[i]> elements[pivot_index]:
            i = i +1
        elements[pivot_index],elements[i] = elements[i],elements[pivot_index]
    return pivot_index

elements = [11,9,29,7,2,15,28]
partition(elements, 0, len(elements)-1)
print(elements)

