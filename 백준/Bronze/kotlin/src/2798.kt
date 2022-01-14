import java.util.*

fun main() = with(System.`in`.bufferedReader()) {
    val token = StringTokenizer(readLine().toString())
    val N = token.nextToken().toInt()
    val M = token.nextToken().toInt()

    val nums = readLine().split(" ").map { num -> num.toInt() }

    val len = nums.size
    var a: Int
    var b: Int
    var c: Int
    var maxTotal = 0
    for (i in 0 until len-2) {
        a = nums[i]
        if (a >= M-1) {
            continue
        }
        for (j in i+1 until len-1) {
            b = nums[j]
            if (a+b >= M) {
                continue
            }
            for (k in j+1 until len) {
                c = nums[k]
                if (a+b+c in (maxTotal + 1)..M) maxTotal = a+b+c
            }
        }
    }
    print(maxTotal)
}