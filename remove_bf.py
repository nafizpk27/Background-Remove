from rembg import remove

input_path="./input_02.jpg"
output_path="./output_02.png"

# remove backgroud using rembg
# input = open(input_path, 'rb').read()
# print(input)
# output = remove(input)
# print(output)
# with open(output_path, 'wb') as f:
#     f.write(output)
#     print("Done")

# first open file in binary
input_fh=open(input_path,"rb")
binary_content = input_fh.read()
# print(binary_content)
output_binary_content = remove(binary_content)
output_fh= open(output_path,"wb")

output_fh.write(output_binary_content)
print("done")