
def max_area(height):
    max_val = 0
    i, j = 0, len(height)-1

    while i<j:
        area = min(height[i], height[j])*(j-i)

        if area>max_val:
            print(i,j)
            max_val = area

        if height[i]>height[j]:
            j -= 1
        else:
            i += 1

    return max_val



if __name__ == '__main__':
    #height = [1,8,6,2,5,4,8,3,7]
    height = [2,3,1,5,4]
    print(max_area(height))