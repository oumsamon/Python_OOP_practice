# # https://www.codewars.com/kata/54c27a33fb7da0db0100040e/train/python

# # A square of squares
# # You like building blocks. You especially like building blocks that are squares. And what you even like more, is to arrange them into a square of square building blocks!

# # However, sometimes, you can't arrange them into a square. Instead, you end up with an ordinary rectangle! Those blasted things! If you just had a way to know, whether you're currently working in vain… Wait! That's it! You just have to check if your number of building blocks is a perfect square.

# # Task
# # Given an integral number, determine if it's a square number:

# # In mathematics, a square number or perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself.

# # The tests will always use some integral number, so don't worry about that in dynamic typed languages.

# import math
# def is_square(n):
#     return n > -1 and math.sqrt(n) % 1 == 0;

# def is_square(n):    
#     if n>=0:
#         if int(n**.5)**2 == n:
#             return True
#     return False

# #the above didnt count since i had to UNLOCK SOLUTIONS


# https://www.codewars.com/kata/54edbc7200b811e956000556/train/python
# Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).

# def count_sheeps(sheep):
#     def count_sheeps(sheep):
#     true_count = sum(sheep)
#     return(true_count)
# #   # TODO May the force be with you
# #   pass

# array1 = [True,  True,  True,  False,
#           True,  True,  True,  True ,
#           True,  False, True,  False,
#           True,  False, False, True ,
#           True,  True,  True,  True ,
#           False, False, True,  True ];
              
# test.assert_equals(result := count_sheeps(array1), 17, "There are 17 sheeps in total, not %s" % result)
# Test Results:
# Test Passed
# You have passed all of the tests! :)



# https://www.codewars.com/kata/555086d53eac039a2a000083/train/python

# Timmy & Sarah think they are in love, but around where they live, they will only know once they pick a flower each. If one of the flowers has an even number of petals and the other has an odd number of petals it means they are in love.

# Write a function that will take the number of petals of each flower and return true if they are in love and false if they aren't.

def lovefunc( flower1, flower2 ):
    if flower1 % 2 != 0 and flower2 % 2 != 0:
        return(False)
    elif flower1 % 2 == 0 and flower2 % 2 == 0:
        return(False)
    elif flower1 % 2 == 0 and flower2 % 2 != 0:
        return(True)
    else:
        return(True)

# Test Results:
# Fixed Tests
# Basic Test Cases (4 of 4 Assertions)
# import codewars_test as test
# from solution import lovefunc

# @test.describe("Fixed Tests")
# def fixed_tests():
#     @test.it('Basic Test Cases')
#     def basic_test_cases():
#         test.assert_equals(lovefunc(1,4), True)
#         test.assert_equals(lovefunc(2,2), False)
#         test.assert_equals(lovefunc(0,1), True)
#         test.assert_equals(lovefunc(0,0), False)