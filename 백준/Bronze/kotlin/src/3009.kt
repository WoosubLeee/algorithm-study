import java.util.*

fun main() = with(System.`in`.bufferedReader()) {
    var token: StringTokenizer
    val xs = mutableListOf<Int>()
    val ys = mutableListOf<Int>()
    for (i in 0..2) {
        token = StringTokenizer(readLine().toString())
        xs.add(token.nextToken().toInt())
        ys.add(token.nextToken().toInt())
    }
    for (s in arrayOf(xs, ys)) {
        for (i in 0..2) {
            if (s.count { it == s[i] } % 2 == 1) {
                print("${s[i]} ")
                break
            }
        }
    }
}