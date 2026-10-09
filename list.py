# DS
# List
# a = [1,2,3,4,5]
# print(a[2])

# a = 20
# b = a
# b= 40
# print(a)
# print(b)

# a = [22,44,55]
# b= a

# a = [1,2,1,2,3,45,1.5,True, print(),{},()]
# print(a)

# a = [30,20,40]
# a[2] = 30
# print(a)



# a = [10,30,40,50]
# for i in a:
#     print(i)

# append
# a = [20,30,40,50,50,50]
# a.append(60)
# print(a)

# a.insert(3,33)
# print(a)

# print(a.index(30))

# a.extend([10,20,30])
# print(a)

# a.remove(20)
# print(a)

# a.pop()
# print(a)
# print(a.count(50))
# a.sort()
# print(a)
# a.reverse()
# print(a)

# b = a.copy()
# b.append(80)
# print(a)
# print(b)

# a.clear()
# print(a)


# Level 1: Beginner (1–10)
# 1. Create a List: 5 numbers ki list banao aur use print karo.
# a = [1,2,3,4,5]
# print(a)

# 2. Access Elements: List ke first aur last element ko print karo.
# a = [22,33,4,55,6]
# print(a[0], a[-1])

# 3. List Length: List me total kitne elements hain, count karo.

# def total_count(l):
#     count = 0
#     for i in l:
#         count +=1
#     return count

# result = total_count([22,33,1,2,3,4,5])
# print(result)

# 4. Sum of Elements: List [10, 20, 30, 40, 50] ke sabhi numbers ka sum nikalo.
# def sum_of_el(l):
#     sum = 0
#     for i in l:
#         sum +=i
#     return sum

# result = sum_of_el([10, 20, 30, 40, 50])
# print(result)

# 5. Largest Element: List [12, 45, 23, 67, 34] me sabse bada number find karo.
# def largest_num(l):
#     largest = l[0]
#     for i in range(0,len(l)):
#         if largest < l[i]:
#             largest = l[i]
    
#     return largest


# result = largest_num([12, 45, 23, 67, 34])
# print(result)

# 6. Smallest Element: List [18, 5, 29, 3, 14] me sabse chhota number find karo.
# def smallest_num(l):
#     smallest = l[0]
#     for i in range(0,len(l)):
#         if smallest > l[i]:
#             smallest = l[i]
                
    
#     return [smallest]


# result = smallest_num([12, 45, 23, 67, 34])
# print(result)

# 7. Add Element: Ek list banao aur user ke input se ek naya element add karo.

# def add_el(l):
#     num = int(input("Enter a number : "))
#     l.append(num)
#     return l

# result = add_el([22,33,44,55])
# print(result)


# 8. Remove Element: List se kisi particular element ko remove karo.

# def remove_el(l,r):
#     l.remove(r)
#     return l

# result= remove_el([11,22,33,44],44)
# print(result)


# 9. Update Element: List ke second element ko change karke 100 kar do.

# def update_el(l):
#     l[1] = 100
#     return l

# result = update_el([11,22,33,44])
# print(result)

# 10. Check Element: User se ek number lo aur check karo ki woh list me present hai ya nahi.
# def check_el(l):
#     num = int(input("Enter a number : "))
#     for i in range(0,len(l)):
#         if l[i] == num:
#             return f"element found in {i} index"
#     else:
#         print("Element does not exist")

# result = check_el([22,33,44,55,66])
# print(result)



# Level 2: Beginner to Intermediate (11–20)
# 11. Even Numbers: List me se saare even numbers print karo.
# 12. Odd Numbers: List me se saare odd numbers print karo.
# 13. Even-Odd Count: List me kitne even aur kitne odd numbers hain, count karo.
# 14. Positive and Negative: List me positive, negative aur zero elements ko alag-alag count karo.
# 15. Reverse List: List ko reverse order me print karo.
# 16. Sort Ascending: List ke numbers ko ascending order me arrange karo.
# 17. Sort Descending: List ke numbers ko descending order me arrange karo.
# 18. Count Occurrences: List [1, 2, 3, 2, 4, 2, 5] me number 2 kitni baar aaya hai, count karo.
# 19. Copy a List: Ek list ki values ko doosri list me copy karo.
# 20. Remove Duplicates: List [1, 2, 2, 3, 4, 4, 5] se duplicate elements remove karo.
# Level 3: Intermediate (21–30)
# 21. Second Largest: List me se second-largest number find karo.
# 22. Second Smallest: List me se second-smallest number find karo.
# 23. Separate Even and Odd: Ek list ke even aur odd numbers ki do alag lists banao.
# 24. Sum of Even Numbers: List ke sirf even numbers ka sum nikalo.
# 25. Average of List: List ke sabhi numbers ka average calculate karo.
# Python List Practice Worksheet Page 2
# 26. Merge Two Lists: Do lists ko combine karke ek nayi list banao.
# 27. Common Elements: Do lists me common elements find karo. Example: [1, 2, 3, 4] aur [3, 4, 5, 6].
# 28. Move Zeros: List [0, 1, 0, 3, 12, 0, 5] ke saare zeros ko end me move karo; baaki numbers ka order
# same rakho.
# 29. Rotate List: List [1, 2, 3, 4, 5] ko ek position right rotate karo. Output: [5, 1, 2, 3, 4].
# 30. Frequency Counter: List me har element ki frequency print karo. Example: [1, 2, 2, 3, 1, 2] ka output:
# 1: 2, 2: 3, 3: 1.