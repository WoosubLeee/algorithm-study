import java.io.BufferedWriter
import java.io.OutputStreamWriter
import java.util.StringTokenizer

fun main() = with(System.`in`.bufferedReader()) {
    val bw = BufferedWriter(OutputStreamWriter(System.out))

    var token = StringTokenizer(readLine())
    val N = token.nextToken().toInt()
    val X = token.nextToken().toInt()

    token = StringTokenizer(readLine())
    for (i in 1..N) {
        var num = token.nextToken().toInt()
        if (num < X) {
            bw.write("$num ")
        }
    }
    bw.flush()
    bw.close()
}