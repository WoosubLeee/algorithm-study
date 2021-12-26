import java.io.BufferedWriter
import java.io.OutputStreamWriter

fun main() = with(System.`in`.bufferedReader()) {
    val bw = BufferedWriter(OutputStreamWriter(System.out))

    val isSelf = Array(10001) { _ -> true }
    var num = 1
    while (num < 10000) {
        var dN = calculateDN(num)
        if (dN <= 10000) {
            isSelf[dN] = false
        }
        num += 1
    }

    for (i in 1..10000) {
        if (isSelf[i]) {
            bw.write("$i\n")
        }
    }
    bw.flush()
    bw.close()
}

fun calculateDN(input: Int): Int {
    var result = input
    var num = input
    while (num > 0) {
        result += num % 10
        num /= 10
    }
    return result
}