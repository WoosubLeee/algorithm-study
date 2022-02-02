import kotlin.math.max

fun main() = with(System.`in`.bufferedReader()) {
    val N = readLine().toInt()

    var result = mutableListOf(readLine().toInt())
    var floor: MutableList<Int>
    for (n in 2..N) {
        floor = readLine().split(" ").map { num -> num.toInt() } as MutableList<Int>
        for (i in 0 until n) {
            if (i == 0) {
                floor[i] += result[i]
            } else if (i == n-1) {
                floor[i] += result[i-1]
            } else {
                floor[i] += max(result[i-1], result[i])
            }
        }
        result = floor
    }
    print(result.maxOrNull())
}