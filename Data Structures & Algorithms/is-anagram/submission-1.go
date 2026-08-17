func isAnagram(s string, t string) bool {

	sMap := make(map[rune]int)
	tMap := make(map[rune]int)

	for _, c := range s {
		sMap[c] += 1
	}

	for _, c := range t {
		tMap[c] += 1
	}

	if len(s) != len(t) {
		return false
	}
	
	for k, v := range sMap {
		tv, ok := tMap[k]
		if !ok {
			return false
		}
		if tv != v {
			return false
		}

	}
	return true
}

