import java.util.*

fun main() = with(System.`in`.bufferedReader()) {
    val memo = Array(21) { Array(21) { IntArray(21) { 1 } } }

    for (i in 1..20) {
        for (j in 1..20) {
            for (k in 1..20) {
                if (j in i+1 until k) {
                    memo[i][j][k] = memo[i][j][k-1] + memo[i][j-1][k-1] - memo[i][j-1][k]
                } else {
                    memo[i][j][k] = memo[i-1][j][k] + memo[i-1][j-1][k] + memo[i-1][j][k-1] - memo[i-1][j-1][k-1]
                }
            }
        }
    }

    var token: StringTokenizer
    var a: Int
    var b: Int
    var c: Int

    while (true) {
        token = StringTokenizer(readLine().toString())
        a = token.nextToken().toInt()
        b = token.nextToken().toInt()
        c = token.nextToken().toInt()

        if (a == -1 && b == -1 && c == -1) {
            break
        }
        var result: Int
        if (a <= 0 || b <= 0 || c <= 0) {
            result = 1
        } else if (a > 20 || b > 20 || c > 20) {
            result = memo[20][20][20]
        } else {
            result = memo[a][b][c]
        }

        println("w($a, $b, $c) = $result")
    }
}
