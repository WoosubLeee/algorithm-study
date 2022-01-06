import java.io.BufferedWriter
import java.io.OutputStreamWriter
import java.util.*
import kotlin.math.sqrt

fun main() = with(System.`in`.bufferedReader()) {
    val bw = BufferedWriter(OutputStreamWriter(System.out))

    val token = StringTokenizer(readLine().toString())
    val M = token.nextToken().toInt()
    val N = token.nextToken().toInt()

//    val isPrime = Array(N+1) { true }
    val isPrime = BooleanArray(N+1)
    isPrime[1] = false

    var num = 2
    var n: Int
    while (num <= sqrt(N.toDouble())) {
        if (isPrime[num]) {
            n = 2
            while (n*num <= N) {
                isPrime[n*num] = false
                n += 1
            }
        }
        num += 1
    }

    for (i in M..N) {
        if (isPrime[i]) {
            bw.write("${i}\n")
        }
    }
    bw.flush()
    bw.close()
}