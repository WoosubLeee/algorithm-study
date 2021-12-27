fun main() = with(System.`in`.bufferedReader()) {
    val result = IntArray(26) { -1 }
    var word = readLine().toCharArray()

    for (i in word.indices) {
        var ascii = word[i].code
        if (result[ascii - 97] == -1) {
            result[ascii - 97] = i
        }
    }
    for (num in result) {
        print("$num ")
    }
}