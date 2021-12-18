import java.util.StringTokenizer

fun main() = with(System.`in`.bufferedReader()) {
    val N = readLine().toInt()
    val token = StringTokenizer(readLine())

    var minNum = 1000000
    var maxNum = -1000000
    for (i in 1..N) {
        var num = token.nextToken().toInt()
        if (num < minNum) {
            minNum = num
        }
        if (num > maxNum) {
            maxNum = num
        }
    }
    print("$minNum $maxNum")
}