import java.util.StringTokenizer

fun main() = with(System.`in`.bufferedReader()) {
    val N = readLine().toInt()
    val token = StringTokenizer(readLine())

    var total = 0.0
    var maxNum = 0.0
    var num: Double

    for (i in 1..N) {
        num = token.nextToken().toDouble()
        total += num
        if (num > maxNum) {
            maxNum = num
        }
    }
    print(total / (N*maxNum) * 100)
}