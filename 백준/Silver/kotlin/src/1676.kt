fun main() = with(System.`in`.bufferedReader()) {
    val N = readLine().toInt()
    var fiveCount = 0
    for (n in 1..N) {
        var newN = n
        while (newN % 5 == 0) {
            fiveCount++
            newN /= 5
        }
    }
    print(fiveCount)
}