func twoSum(nums []int, target int) []int {
    
	// record the indexes for each number seen
	f := make(map[int][]int)
	for i, n := range nums {
		if f[n] == nil {
			f[n] = make([]int, 0)
		}
		f[n] = append(f[n], i)
	}

	for i, n := range nums {
		// target
		t := target-n

		idxs, ok := f[t]

		if !ok {
			continue
		}

		// we want to make sure that i isn't in idxs
		for j := range idxs {
			if i == idxs[j] {
				continue
			}
			if i<idxs[j] {
				return []int{i, idxs[j]}
			} else {
				return []int{idxs[j], i}
			}

		}
	}
	return []int{}
}
