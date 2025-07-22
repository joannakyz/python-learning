int_num = 15
float_num = 15.67
string = "My name is Ioanna"

print("String concatenation -> " + str(int_num) + " , " + str(float_num) + " , " + string)
print(f"f strings -> {int_num} , {float_num} , {string}")
print("c method -> Int: %d, float: %f, string: %s" % (int_num, float_num, string)) 
print("format method -> int: {}, float: {}, string: {}".format(int_num, float_num, string))
