import java.io.BufferedWriter
import java.io.OutputStreamWriter
import java.util.StringTokenizer

fun main() = with(System.`in`.bufferedReader()) {
    val bw = BufferedWriter(OutputStreamWriter(System.out))
    for (i in 1..readLine().toInt()) {
        val token = StringTokenizer(readLine())
        val sum = (token.nextToken().toInt() + token.nextToken().toInt()).toString()
        bw.write("Case #$i: $sum\n")
    }
    bw.flush()
    bw.close()
}