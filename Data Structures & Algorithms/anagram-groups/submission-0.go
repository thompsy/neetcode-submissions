import "slices"

func groupAnagrams(strs []string) [][]string {

    // map from the sorted string to the original(s)
    m := make(map[string][]string)

    for _, s := range strs {
        key := sortString(s)

        _, ok := m[key]
        if !ok {
            m[key]  = make([]string, 0)
        }
        m[key] = append(m[key], s)
    }

    result := make([][]string, 0)
    for _, v := range m {
        result = append(result, v)
    }
    return result
}

func sortString(s string) string {
    r := []rune(s)
    slices.Sort(r)
    return string(r)
}
