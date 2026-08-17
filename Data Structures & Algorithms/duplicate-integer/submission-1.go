func hasDuplicate(nums []int) bool {
    m := make(map[int]bool)

    for _, n := range nums {
        _, ok := m[n]
        if ok {
            return true
        }
        m[n] = true
    }
    return false
}
