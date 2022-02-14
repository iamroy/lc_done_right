
def daily_temperatures_brute_force(temperatures):
    out_arr = [0]*len(temperatures)
    for i in range(len(temperatures)-1):
        for j in range(i+1, len(temperatures)):
            if temperatures[j]>temperatures[i]:
                out_arr[i] = j-i
                break
    return out_arr

def daily_temperatures(temperatures):
    out_arr = [0] * len(temperatures)
    stack = []

    for day, temp in enumerate(temperatures):

        while stack and temperatures[stack[-1]] < temp:
            out_arr[stack[-1]] = day - stack[-1]
            stack.pop()

        stack.append(day)

    return out_arr

if __name__ == '__main__':
    #temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    temperatures = [89, 62, 70, 58, 47, 47, 46, 76, 100, 70]
    print(daily_temperatures(temperatures))