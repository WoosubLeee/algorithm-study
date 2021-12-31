import java.util.*

fun main() = with(System.`in`.bufferedReader()) {
    val token = StringTokenizer(readLine().toString())
    val A = token.nextToken().toInt()
    val B = token.nextToken().toInt()
    val C = token.nextToken().toInt()

    print(calculate(A, B, C))
}

fun calculate(A: Int, B: Int, C: Int): Int {
    if (B >= C) {
        return -1
    }
    return A / (C-B) + 1
}