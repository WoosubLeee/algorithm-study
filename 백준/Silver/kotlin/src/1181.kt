fun quickSort(arr: MutableList<String>, start: Int, end: Int) {
    if (start < end) {
        val pivot = start
        var left = start + 1
        var right = end

        while (left <= right) {
            while (left <= end && (arr[left].length < arr[pivot].length || (arr[left].length == arr[pivot].length && arr[left] <= arr[pivot]))) {
                left++
            }
            while (right > start && (arr[right].length > arr[pivot].length || (arr[right].length == arr[pivot].length && arr[right] >= arr[pivot]))) {
                right--
            }

            var temp: String
            if (left <= right) {
                temp = arr[left]
                arr[left] = arr[right]
                arr[right] = temp
            } else {
                temp = arr[right]
                arr[right] = arr[pivot]
                arr[pivot] = temp
            }
        }

        quickSort(arr, start, right-1)
        quickSort(arr, right+1, end)
    }
}

fun main() = with(System.`in`.bufferedReader()) {
    val N = readLine().toInt()
    var words = mutableListOf<String>()
    var word: String
    for (i in 1..N) {
        word = readLine()
        if (!words.contains(word)) words.add(word)
    }
    quickSort(words, 0, words.size-1)
    print(words.joinToString("\n"))
}