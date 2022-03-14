import kotlin.math.max

fun main() = with(System.`in`.bufferedReader()) {
    val line = readLine().split(" ")
    val K = line[0].toInt()
    val N = line[1].toInt()

    val lines = LongArray(K)
    for (i in 0 until K) {
        lines[i] = readLine().toLong()
    }

    val total = lines.sum()
    var left = max(total / (N+K), 1)
    var right = (total / N)

    while (left <= right) {
        val mid = (left + right) / 2

        if (check(mid, lines, N)) {
            left = mid + 1
        } else {
            right = mid - 1
        }
    }

    print(left - 1)
}

fun check(length: Long, lines: LongArray, target: Int): Boolean {
    var count = 0L
    for (line in lines) {
        count += line / length
    }
    return count >= target
}