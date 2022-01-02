import java.util.StringTokenizer

fun main() = with(System.`in`.bufferedReader()) {
    for (i in 1..readLine().toInt()) {
        var token = StringTokenizer(readLine().toString())
        var H = token.nextToken().toInt()
        var W = token.nextToken().toInt()
        var N = token.nextToken().toInt()

        var h = N - H*((N-1)/H)
        var w = (N-1)/H + 1
        if (w >= 10) {
            println("${h}${w}")
        } else {
            println("${h}0${w}")
        }
    }
}