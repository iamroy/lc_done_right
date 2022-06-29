def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ""

    if len(strs) == 1:
        return strs[0]

    common_prefix = ''
    strs_sorted= sorted(strs)

    for i in range(len(strs_sorted[0])):
        c = strs_sorted[0][i]
        j = 1

        while j<len(strs):
            if c == strs_sorted[j][i]:
                j += 1
            else:
                return common_prefix

        common_prefix += c

    return common_prefix