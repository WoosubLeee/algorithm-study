import java.io.BufferedWriter
import java.io.OutputStreamWriter

fun main() = with(System.`in`.bufferedReader()) {
    val bw = BufferedWriter(OutputStreamWriter(System.out))

    val N = readLine().toInt()
    val rads = readLine().toString().split(" ").map { num -> num.toInt() }

    val first = rads[0]
    for (i in 1 until N) {
        val gcd = calcGcd(first, rads[i])
        bw.write("${first/gcd}/${rads[i]/gcd}\n")
    }
    bw.flush()
}

fun calcGcd(a: Int, b: Int): Int {
    if (b == 0) {
        return a
    }
    return calcGcd(b, a % b)
}