import java.io.BufferedWriter
import java.io.OutputStreamWriter
import java.util.*

fun main() = with(System.`in`.bufferedReader()) {
    val memo = Array(21) { Array(21) { IntArray(21) { 1 } } }
    for (a in 1..20) {
        for (b in 1..20) {
            for (c in 1..20) {
                if (b in a+1 until c) {
                    memo[a][b][c] = memo[a][b][c-1] + memo[a][b-1][c-1] - memo[a][b-1][c]
                } else {
                    memo[a][b][c] = memo[a-1][b][c] + memo[a-1][b-1][c] + memo[a-1][b][c-1] - memo[a-1][b-1][c-1]
                }
            }
        }
    }

    val bw = BufferedWriter(OutputStreamWriter(System.out))

    var token: StringTokenizer
    var a: Int
    var b: Int
    var c: Int
    var result: String

    while (true) {
        token = StringTokenizer(readLine().toString())
        a = token.nextToken().toInt()
        b = token.nextToken().toInt()
        c = token.nextToken().toInt()

        if (a == -1 && b == -1 && c == -1) {
            break
        }

        result = "w($a, $b, $c) = "
        if (a <= 0 || b <= 0 || c <= 0) {
            result += 1
        } else if (a > 20 || b > 20 || c > 20) {
            result += memo[20][20][20]
        } else {
            result += memo[a][b][c]
        }
        bw.write("$result\n")
    }
    bw.flush()
}