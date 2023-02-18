# def caesarCipher(s, k):
#     # Write your code here
#     a="abcdefghijklmnopqrstuvwxyz"
#     A="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     cap_alphabets=[i for i in A]
#     aplhabets=[i for i in a]
#     new_s=""
#     for i in s:
#         if i in aplhabets:
#             indx=aplhabets.index(i)
#             if (indx+k) <26:
#                 new_s+=aplhabets[indx+k]
#             else:
#                 m=(indx+k)-26
#                 while m>25:
#                     m=m-26
#                 new_s+=aplhabets[m]
#         elif i in cap_alphabets:
#             indx=cap_alphabets.index(i)
#             if (indx+k) <26:
#                 new_s+=cap_alphabets[indx+k]
#             else:
#                 m=(indx+k)-26
#                 while m>25:
#                     m=m-26
#                 new_s+=cap_alphabets[m]
#         else:
#             new_s+=i
#     return new_s
#
# def test():
#     a = "jnfenbibh-bdejenfbh"
#     b = 5
#     c = "asdfghjk-lopinbfgf"
#     d = 9
#
#     print(caesarCipher(a,b))
#     print(caesarCipher(a,b))
#     print(caesarCipher(c,d))
#
#
# test()
#
# def underpaid():
#     dict = {"manager one":100, "manager twp": 200, "manager": 10}
#
#     while dict < 60:
#         print("is underpaod")
#
#     if dict > 100:
#         return True
#
# underpaid()

# class Manager:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
# class BST:
#     def __init__(self):
#         self.root = None
#
#     def is_underpaid(self, threshold):
#         underpaid_managers = []
#         def traverse(node):
#             if node is None:
#                 return
#             if node.salary < threshold:
#                 underpaid_managers.append(node.name)
#             traverse(node.left)
#             traverse(node.right)
#         traverse(self.root)
#         return underpaid_managers
#
# bst = BST()
#
# # insert managers into the BST
# bst.root = Manager("John", 100000)
# bst.root.left = Manager("Mike", 90000)
# bst.root.right = Manager("Sarah", 120000)
#
# # find underpaid managers
# threshold = 95000
# underpaid_managers = bst.is_underpaid(threshold)
#
# # print the names of the underpaid managers
# for manager in underpaid_managers:
#     print(manager)
#
#     def test_underpaid_manager():
# # Create the binary search tree
#         bst = BST()
#
#     # Insert managers into the BST
#         bst.root = Manager("John", 100000)
#         bst.root.left = Manager("Mike", 90000)
#         bst.root.right = Manager("Sarah", 120000)
#         bst.root.left.left = Manager("Alex", 85000)
#         bst.root.left.right = Manager("Jane", 95000)
#
#         # Test 1: Test with a threshold that no manager is underpaid
#         threshold = 100000
#         assert bst.is_underpaid(threshold) == []
#
#         # Test 2: Test with a threshold that all managers are underpaid
#         threshold = 50000
#         assert bst.is_underpaid(threshold) == ["John", "Mike", "Sarah", "Alex", "Jane"]
#
#         # Test 3: Test with a threshold that some managers are underpaid
#         threshold = 92000
#         assert bst.is_underpaid(threshold) == ["Mike", "Alex", "Jane"]
#
#         # Test 4: Test with a threshold that only one manager is underpaid
#         threshold = 90000
#         assert bst.is_underpaid(threshold) == ["Mike"]
#
#         # Test 5: Test with a threshold that no manager exists in the BST
#         threshold = 200000
#         assert bst.is_underpaid(threshold) == []


# test_underpaid_manager()

# def manager():
#
#     dict = {"joe":200,"jose":100,"john":60}
#     for i in dict:
#         if i < 100:
#             return dict[i]
#
#         elif i > 100:
#             return dict[i]
#
#
#
# # dict = ["joe":200,"jose":100,"john":60]
# print(dict["joe"])
#
# manager()

def manager():

    thisdict =	{
      "brad": 200,
      "mod": 100,
      "year": 60
    }
    x = thisdict.keys()
    for i in thisdict:
        #print(thisdict.get(i))
        if thisdict.get(i) < 100:
            print("this person is underpaid")
        else:
            return None

print(manager())
