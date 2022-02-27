import java.util.*

fun main() = with(System.`in`.bufferedReader()) {
    val token = StringTokenizer(readLine().toString())

    val N = token.nextToken().toInt()
    val K = token.nextToken().toInt()

    val arr = (1..N).toMutableList()

    var front = -1
    var rear = N-1

    val result = mutableListOf<Int>()
    while (front < rear) {
        for (i in 1 until K) {
            front++
            arr.add(arr[front])
            rear++
        }
        front++
        result.add(arr[front])
    }
    print("<${result.joinToString(", ")}>")
}